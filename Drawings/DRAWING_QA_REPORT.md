# Drawing QA Report — HomeConstruction

**Status:** BLOCKED — full construction set not issued

## Source reviewed

- `HomeConstruction.FCStd` (1,986,432 bytes; updated 2026-09-10 16:39)
- `walkthrough.md`
- Existing PDFs/SVG exports in `Drawings/` and `renders/`

## Existing drawing assets

| Drawing | Status | Notes |
| --- | --- | --- |
| Ground Floor plan | Present | `Drawings/01_GF_Floor_Plan_A3_1-50.pdf` and the documented native TechDraw page `Page_Ground_Floor_Plan`. |
| First Floor plan | Present but unverified | `Drawings/02_FF_Floor_Plan_A3_1-50.pdf` exists but is only 13,173 bytes and requires FreeCAD review before issue. |
| Foundation/site drawing | Partial export | `renders/Site_Plan_Foundation_Layout.pdf` / `.svg` present. |
| Column/beam drawing | Partial export | `renders/Structural_Plan_Columns_Beams.pdf` / `.svg` present. |
| Elevations, sections, roof plan, stair detail, MEP plans, schedules | Not issued as verified editable sheets | No corresponding complete, named TechDraw pages were identified from the supplied project documentation. |

## Dimensions verified from the documentation

- Plot: **5,029.2 × 7,620 mm** (nominal 5.03 × 7.62 m).
- Typical RCC columns: **228.6 × 228.6 mm**.
- Footing base / PCC base: **−1,500 / −1,600 mm** respectively.
- Plinth top: **+914.4 mm**.
- Roof/terrace slab: **7,135.4 to 7,260.4 mm**.
- Ground-floor opening schedule: D1 1,050 × 2,100; D2 914 × 2,134; D4 750 × 2,050; W1 2,100 × 1,295; W2 1,214 × 1,314; V1 600 × 600 mm.

## Material inconsistencies requiring resolution

1. **Ground FFL conflict:** the walkthrough gives both **+914.4 mm** and **+944.88 mm** as the ground finished-floor level.
2. **Stair conflict:** the ground-floor plan schedule describes **two 9-riser flights at 190.5 mm**, while the later stair audit describes **17 uniform risers at 186.65 mm**.
3. **Model inventory conflict:** the documentation reports **492**, **537**, **612**, and **618** model objects at different points. This prevents a traceable issue record without an in-app document audit.
4. **Editable-sheet coverage:** the documentation identifies only `Page_Ground_Floor_Plan` as a native TechDraw page; it also says temporary section planes were deleted. Therefore, issuing the requested section/elevation sheets as model-derived editable drawings would require recreating them in FreeCAD after the conflicts above are resolved.

## Required manual engineering/architect review

- Confirm the controlling datum and finished-floor levels.
- Confirm the final stair geometry and riser count.
- Verify the undersized first-floor PDF against the live model.
- Provide/confirm the site boundary, road position, setbacks, north direction, and any design-released MEP symbols/circuiting absent from the model.
- Engineer to review foundation sizing, member design, reinforcement, plumbing pipe sizing, and electrical circuit protection before construction issue.

## Issue recommendation

Do not issue a construction-ready package until the conflicts are resolved in `HomeConstruction.FCStd`. Once confirmed, create and validate the remaining native TechDraw pages: site/foundation, GF/FF/roof plans, four elevations, A-A/B-B sections, stair detail, structural layouts, door/window schedule, electrical plan, water-supply plan, and drainage plan.
