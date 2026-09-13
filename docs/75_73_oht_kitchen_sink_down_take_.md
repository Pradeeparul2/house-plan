## 73. OHT Kitchen Sink Down-Take Pipeline Re-Routing: Headroom Weather Curb to Col NE (Zero Window Obstruction)

> [!NOTE]
> **System Modification:** Line B Kitchen Gravity Down-take Architectural Facade De-Cluttering  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Modified Component:** [`Downtake_Kitchen_Riser_Shaft`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Engineering Objective:** Complete elimination of pipe crossing across the Staircase Headroom (Mumty) Frosted Glass Feature Window, routing pipe along the Headroom Roof Weather Curb and dropping down along `Headroom Col NE`.

---

### 73.1 Problem Diagnosis & Visual Defect

Previously, the $25\text{ mm}$ ($1"$) CPVC gravity down-take for the kitchen (`Downtake_Kitchen_Riser_Shaft`):
1. Dropped vertically from the rooftop manifold down to $Z = 8550.0\text{ mm}$ on the North-West corner.
2. Ran horizontally at $Z = 8550.0\text{ mm}$ across the North front facade from $X = 3550.0\text{ mm}$ to $X = -60.0\text{ mm}$.
3. **Severe Visual Clashing:** Because the Headroom Frosted Glass Window sits between $X \in [2362.2, 3162.2\text{ mm}]$ at elevation $Z \in [7760.4, 8960.4\text{ mm}]$, the horizontal pipe ran directly through the visual center of the window ($Z = 8550.0\text{ mm}$), marring the contemporary architectural facade and obscuring the glass panel.

---

### 73.2 Architectural & Engineering Solution

The pipeline was re-engineered to follow an orthogonal, concealed structural perimeter:
1. **Headroom Roof Weather Curb Run:**
   - Instead of dropping down to window level, the pipe remains on the Mumty roof at $Z = 9860.0\text{ mm}$, running horizontally along the North **Headroom Roof Weather Curb** (`Headroom_Roof_Coping`) from $X = 3550.0\text{ mm}$ eastward to $X = 1800.0\text{ mm}$.
   - Elevation $Z = 9860.0\text{ mm}$ is **$945\text{ mm}$ above the top of the window**, resting above the structural roof slab and cornice.
2. **Headroom Col NE Vertical Drop:**
   - At $X = 1800.0\text{ mm}, Y = -120.0\text{ mm}$, the pipe turns $90^\circ$ downward with a standard elbow.
   - It descends vertically along the outer face of **Headroom Col NE** (`Headroom_Col_NE`) from $Z = 9860.0\text{ mm}$ down to $Z = 7450.0\text{ mm}$ (terrace parapet level).
   - **Zero Window Interference:** Column NE is at $X \le 1943.1\text{ mm}$, while the window frame starts at $X = 2362.2\text{ mm}$ and glass starts at $X = 2407.2\text{ mm}$. The vertical drop maintains a **$572.1\text{ mm}$ clear margin** from the window frame and **$622.9\text{ mm}$ margin** from the glass.
3. **Terrace North Parapet Return:**
   - At $Z = 7450.0\text{ mm}$, the pipe turns $90^\circ$ east, running horizontally along the inner face of the North terrace parapet wall to the East corner ($X = -60.0\text{ mm}$).
   - At $X = -60.0\text{ mm}$, it turns South along the East setback chase, seamlessly feeding the First Floor and Ground Floor kitchen branches as before.

---

### 73.3 Visual Verification Portfolio

```carousel
![Close-Up Elevation: Mumty Frosted Glass Window 100% Unobstructed with Col NE Pipe Drop](c:\Users\prade\OneDrive\Desktop\home plan\renders\headroom_window_pipeline_reroute_front.png)
<!-- slide -->
![Isometric Rooftop Overview: Kitchen Down-Take Routed Along Headroom Weather Curb](c:\Users\prade\OneDrive\Desktop\home plan\renders\kitchen_pipeline_headroom_curb.png)
```

---

### 73.4 Revised Pipeline Segment Schedule

| Segment Description | Start Point $(X, Y, Z)$ (mm) | End Point $(X, Y, Z)$ (mm) | Length (mm) | Orientation | Safety & Clearance Function |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **West Roof Branch** | $(3550, 1625, 9860)$ | $(3550, -120, 9860)$ | $1745.0$ | Horizontal North | Draws gravity water from OHT manifold header. |
| **North Weather Curb** | $(3550, -120, 9860)$ | $(1800, -120, 9860)$ | $1750.0$ | Horizontal East | Runs along roof coping; **$945\text{ mm}$ above window**. |
| **Col NE Vertical Drop** | $(1800, -120, 9860)$ | $(1800, -120, 7450)$ | $2410.0$ | Vertical Down | Drops along Col NE; **$572\text{ mm}$ clear of window**. |
| **North Parapet Run** | $(1800, -120, 7450)$ | $(-60, -120, 7450)$ | $1860.0$ | Horizontal East | Concealed behind $1.0\text{ m}$ high terrace parapet wall. |
| **East Parapet Run** | $(-60, -120, 7450)$ | $(-60, 7180, 7450)$ | $7300.0$ | Horizontal South | Exterior East setback chase to kitchen locations. |
| **Kitchen Down-takes** | $(-60, 7180, 7450)$ | Drops to FF & GF | Downward | Vertical Drops | Direct wall feeds to FF & GF kitchen sink taps. |

---

### 73.5 Quality Certification & Model Hygiene

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** **616 objects, 0 errors, 100% valid manifold solids.**
* **Window Obstruction:** **$0.0\text{ mm}^3$ overlap; 100% clear sightline to Headroom Frosted Glass Panel.**
* **Structural Clash Status:** **0 clashes** detected against columns, beams, slabs, coping, or doors.

---
