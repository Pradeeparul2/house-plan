# Construction Copilot

Construction Copilot is the project intelligence layer for the residential construction model and technical documentation in this workspace. It turns the BIM source model, project technical manual, and visual renders into a queryable, chat-based, on-site engineering assistant.

## Purpose

The Copilot is built to help construction teams answer precise field questions with evidence from the model and specification documents instead of memory or guesswork. It serves as a mobile-friendly knowledge and project-control layer for:

- structural layout questions
- staircase and drainage details
- plumbing and sanitary requirements
- electrical MEP coordination
- waterproofing and curing checks
- quantity takeoff and cost estimation
- daily progress tracking and owner reporting

The current app is a Streamlit chat interface. Gemini can provide the natural-language answer, while local retrieval supplies the CAD, specification, and visual evidence used to ground that answer.

## Source of truth

The authoritative model remains the FreeCAD BIM file:

- HomeConstruction.FCStd

The runtime data extracted from the model is stored in the generated CAD database:

- copilot/KB/cad_database.sqlite

The project technical specification is stored in:

- walkthrough.md

The master project spec is stored in:

- CONSTRUCTION_COPILOT_SPEC.md

Generated knowledge indexes are stored in `copilot/KB/`:

- `cad_database.sqlite` - extracted FreeCAD object metadata
- `specs_database.json` - indexed sections from `walkthrough.md`
- `visual_index.json` - indexed assets from `renders/`

## Architecture

The project follows a 3-layer design:

1. CAD database layer
   - stores extracted object metadata
   - includes dimensions, locations, geometry, material and object classification
   - generated from the FreeCAD model

2. Knowledge base layer
   - stores technical guidance and construction standards
   - includes rules, methods, code references and installation sequences

3. Reasoning and app layer
   - combines CAD, specification, and visual retrieval
   - optionally sends grounded evidence to Google Gemini
   - presents answers through the Streamlit chat app

## Folder structure

```text
home plan/
├── HomeConstruction.FCStd
├── walkthrough.md
├── CONSTRUCTION_COPILOT_SPEC.md
├── copilot/
│   ├── README.md
│   ├── KB/
│   │   ├── cad_database.sqlite
│   │   ├── specs_database.json
│   │   └── visual_index.json
│   ├── ai/
│   │   └── reasoning_engine.py
│   └── scripts/
│       ├── extract_cad_to_sqlite.py
│       ├── parse_walkthrough_to_kb.py
│       └── index_visual_assets.py
├── app.py
├── .env
└── ...
```

## Gemini configuration

The app reads `GEMINI_API_KEY` from the project-root `.env` file. Keep this file private; it is excluded by `.gitignore` and must not be committed or shared.

Example `.env` entry:

```text
GEMINI_API_KEY=your_gemini_api_key
```

The reasoning engine first retrieves local evidence from SQLite and the JSON indexes. When Gemini is configured, it receives that evidence in a controlled prompt and produces the conversational response. If the key is missing or the Gemini request fails, the app falls back to the deterministic local summary instead of stopping.

The app logs provider diagnostics to the Streamlit runtime log and shows the current Gemini configuration in the sidebar. Each response also records whether the planner and answer came from `gemini` or `local`.

For Streamlit Cloud, add this secret in **App settings > Secrets**:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
GEMINI_MODEL = "gemini-2.5-flash"
```

If the sidebar shows Gemini as configured but the response status is `local`, check the Cloud logs for `RESOURCE_EXHAUSTED`, `401`, `403`, `404`, or timeout messages. `429 RESOURCE_EXHAUSTED` means the API key has no available quota or has exceeded its rate limit; it is not a retrieval failure, and the local fallback is being used intentionally.

## Run the chat app

From the project root, use the project virtual environment:

```powershell
& ".\.venv\Scripts\python.exe" -m streamlit run ".\app.py" --server.port 8503
```

Then open `http://localhost:8503` in a browser. Use another available port if `8503` is already occupied.

## CAD database workflow

The SQLite database is not the master model. It is a generated runtime artifact derived from the FreeCAD source model.

When the model changes:

1. update the BIM model in FreeCAD
2. run the extraction script
3. regenerate the SQLite database
4. refresh the app and downstream queries

## Regenerate the database

Use FreeCAD's command-line runtime to run the script from the project root:

```powershell
& "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" "C:\Users\prade\OneDrive\Desktop\home plan\copilot\scripts\extract_cad_to_sqlite.py"
```

This script loads the project model, reads object metadata, and writes database rows into:

- copilot/KB/cad_database.sqlite

## Regenerate the complete knowledge base

After changing the model, walkthrough, or renders, refresh the derived data in this order:

1. Extract the FreeCAD model into SQLite.
2. Parse `walkthrough.md` into `copilot/KB/specs_database.json`.
3. Index the `renders/` folder into `copilot/KB/visual_index.json`.
4. Restart Streamlit so the app reloads the generated files.

The two JSON indexes are also generated artifacts. Do not edit them manually; update their source documents or assets and rerun the corresponding script.

## Notes

- The database is intended for lightweight runtime access and querying.
- The model remains the authoritative source for geometry and design changes.
- The app should always read from the generated SQLite DB rather than direct FreeCAD objects.
- Gemini is an answer-generation layer, not the source of truth.
- Never treat a Gemini response as a structural approval; verify critical site decisions with the responsible engineer and current project drawings.

## Goal

The Copilot is designed to turn a complex residential construction model into a practical, field-ready engineering assistant that combines exact CAD data, construction standards, and daily project control.
