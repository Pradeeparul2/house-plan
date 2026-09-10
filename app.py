import sys
from pathlib import Path

import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent))

from copilot.ai.reasoning_engine import answer_query


st.set_page_config(page_title="Construction Copilot", page_icon="🏗️", layout="wide")


def visual_path(item: dict) -> Path:
    relative_path = str(item.get("relative_path") or "").replace("\\", "/")
    return Path(__file__).resolve().parent / relative_path


def render_visual_evidence(items: list[dict]) -> None:
    """Render supported visual assets inside the assistant chat message."""
    image_items = []
    other_items = []
    for item in items:
        path = visual_path(item)
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif"} and path.exists():
            image_items.append((item, path))
        else:
            other_items.append((item, path))

    if image_items:
        columns = st.columns(min(2, len(image_items)))
        for index, (item, path) in enumerate(image_items):
            with columns[index % len(columns)]:
                st.image(str(path), caption=item.get("file_name", path.name), use_container_width=True)

    for item, path in other_items:
        if path.exists():
            st.caption(f"{item.get('file_name', path.name)}: {path}")


def answer_has_no_matching_evidence(answer: str) -> bool:
    """Detect a grounded answer that explicitly says the requested item is absent."""
    normalized = " ".join(answer.lower().split())
    absence_phrases = (
        "no data",
        "no details available",
        "no relevant data",
        "not available",
        "not present",
        "cannot be found",
        "could not find",
        "no evidence",
    )
    return any(phrase in normalized for phrase in absence_phrases)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hi, I am the Site Copilot. Ask about dimensions, plumbing, electrical, stair details, or construction rules.",
        }
    ]

with st.sidebar:
    st.header("🏗️ Project")
    st.write("Residential home construction")
    st.write("Source model: HomeConstruction.FCStd")
    st.write("Data source: SQLite + KB JSON")

    st.markdown("---")
    st.caption("Quick presets")
    for preset in [
        "What is the staircase riser height?",
        "Show the kitchen drainage route.",
        "What are the electrical conduit details?",
        "What is the waterproofing detail for the toilet?",
    ]:
        if st.button(preset, key=preset):
            st.session_state.user_input = preset

    st.markdown("---")
    if st.button("Clear chat"):
        st.session_state.chat_history = [
            {
                "role": "assistant",
                "content": "Chat cleared. Ask me anything about the site, model, or construction guidance.",
            }
        ]

st.title("🏗️ Construction Copilot")
st.caption("Site Worker View • CAD + Standards + Visual Evidence")

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("visual_items"):
            render_visual_evidence(message["visual_items"])

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

user_input = st.chat_input("Type your question for site coordination...")
if user_input is not None:
    st.session_state.user_input = user_input

if st.session_state.user_input:
    prompt = st.session_state.user_input.strip()
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        recent_user_context = "\n".join(
            message["content"]
            for message in st.session_state.chat_history[-6:-1]
            if message.get("role") == "user"
        )
        with st.spinner("Checking CAD, specs, and visuals..."):
            result = answer_query(prompt, limit=5, context=recent_user_context)

        answer = result["summary"]
        cad_items = result["cad_results"]
        spec_items = result["spec_results"]
        visual_items = result["visual_results"]
        if result.get("evidence_status") == "not_found":
            cad_items = []
            spec_items = []
            visual_items = []

        response_blocks = [answer]
        if visual_items:
            response_blocks.append("\n\nI’ve included the relevant visual reference below.")

        assistant_response = "\n".join(response_blocks)
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": assistant_response,
            "visual_items": visual_items,
        })
        with st.chat_message("assistant"):
            st.markdown(assistant_response)
            if visual_items:
                render_visual_evidence(visual_items)

        if cad_items or spec_items or visual_items:
            with st.expander("Evidence details", expanded=False):
                tabs = st.tabs(["CAD", "Specs", "Visuals"])

                with tabs[0]:
                    if cad_items:
                        for item in cad_items:
                            st.json(item)
                    else:
                        st.info("No direct CAD match.")

                with tabs[1]:
                    if spec_items:
                        for item in spec_items:
                            st.json(item)
                    else:
                        st.info("No relevant spec match.")

                with tabs[2]:
                    if visual_items:
                        for item in visual_items:
                            st.json(item)
                            path = visual_path(item)
                            if path.exists() and path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp", ".gif"}:
                                st.caption(f"Asset path: {path}")
                    else:
                        st.info("No visual asset match.")

        st.session_state.user_input = ""
