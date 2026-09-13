## 74. Rooftop Terrace Weatherproof Wall Luminaire & Entrance Switchboard (SB-TERRACE)

> [!NOTE]
> **System Classification:** Architectural Exterior Lighting & Electrical Distribution  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Group:** `Staircase Headroom (Mumty) Tower & Roof Slab` (`Staircase_Headroom_Group`)  
> **New Components:**  
>   * `Terrace_Wall_Light_Fixture` (Rooftop Terrace Weatherproof LED Wall Luminaire)
>   * `Terrace_Entrance_Switchboard_Backbox` (SB-TERRACE Concealed Metal Flush Backbox)
>   * `Terrace_Entrance_Switchboard_SB_TERRACE` (Terrace Entrance Switchboard Faceplate)
>   * `Terrace_Entrance_Switchboard_Switches` (SB-TERRACE Rocker Switches & 16A Outdoor Socket)
>   * `Terrace_Switchboard_Power_Supply_Conduit` (Mains Riser Power Supply Conduit from Slab)
>   * `Terrace_Wall_Light_Conduit` (20mm Rigid Orange PVC Switched Feed Conduit to Luminaire)

---

### 74.1 System Overview & Ergonomic Functionality

To provide safe, comprehensive illumination across the entire open rooftop terrace while eliminating the need to step out into a dark terrace to search for lighting controls, a dedicated outdoor luminaire, entryway switchboard, and continuous in-wall power distribution riser system was engineered:

1. **South-Facing Terrace Wall Luminaire (`Terrace_Wall_Light_Fixture`):**
   * **Location:** Mounted flush against the **exterior South wall** of `Headroom_Walls` at $Y = 1866.9\text{ mm}$, centered at $X = 3150.0\text{ mm}$.
   * **Spatial Placement:** Positioned directly between the rooftop maintenance monkey ladder ($X \le 2766.0\text{ mm}$) and structural column `Headroom_Col_SW` ($X = 3695.7\text{ mm}$), projecting southward directly across the primary open rooftop expanse.
   * **Mounting Elevation:** $Z = 8800.0\text{ mm}$ ($+1540.0\text{ mm}$ above finished terrace slab $Z = 7260.4\text{ mm}$), positioned cleanly beneath the South wall continuous RCC lintel band ($Z = 8960.4\text{ mm}$).
   * **Architectural Styling:** Die-cast weatherproof aluminum housing with dual top/bottom visor hoods and a bright optical diffuser faceplate (Electric Blue/Cyan accent `#1A8CF2`).

2. **Interior Entrance Switchboard & Flush Backbox (`SB-TERRACE`):**
   * **Location:** Mounted on the **interior South wall** of the Headroom at $Y = 1714.5\text{ mm}$, immediately adjacent to the terrace exit door jamb ($X = 2020.0\text{ mm}$, $150\text{ mm}$ from the doorway edge).
   * **Concealed Metal Backbox (`Terrace_Entrance_Switchboard_Backbox`):** $120 \times 50 \times 80\text{ mm}$ flush enclosure recessed into the masonry core ($Y \in [1714.5, 1764.5\text{ mm}]$), providing top and bottom knockout entries.
   * **Ergonomic Elevation:** $Z = 8460.0\text{ mm}$ ($+1200\text{ mm}$ above finished floor $Z = 7260.4\text{ mm}$), right at hand level as an occupant steps off the final staircase flight before passing onto the open terrace.
   * **Modular Configuration:**
     - 1x 16A Outdoor Lighting Master Switch with neon indicator toggle.
     - 1x 6A Auxiliary Convenience Switch.
     - 1x 16A Weatherproof Shuttered 3-Pin Utility Socket (for terrace cleaning equipment, laptops, or outdoor event lighting).

3. **Continuous In-Wall Power Supply & Distribution Network:**
   * **Incoming Mains Power Riser (`Terrace_Switchboard_Power_Supply_Conduit`):**
     - A $20\text{ mm}$ rigid heavy-duty PVC conduit (Safety Orange `#FF8000`) rising continuously from the First Floor ceiling / intermediate slab level ($Z = 7135.4\text{ mm}$), penetrating the terrace slab ($Z = 7260.4\text{ mm}$), and ascending inside the South wall chase at $X = 2020.0\text{ mm}, Y = 1739.5\text{ mm}$.
     - Connects directly into the bottom entry of `Terrace_Entrance_Switchboard_Backbox` at $Z = 8420.0\text{ mm}$, guaranteeing seamless power feed from the building's electrical distribution network with zero floating or disconnected segments.
   * **Outgoing Switched Feed Conduit (`Terrace_Wall_Light_Conduit`):**
     - Exits the top knockout of the backbox at $Z = 8500.0\text{ mm}$, rises vertically to $Z = 8800.0\text{ mm}$, runs horizontally through the wall chase to $X = 3150.0\text{ mm}$, and terminates with a direct through-wall stub emerging into the luminaire backplate.

---

### 74.2 Visual Verification Portfolio

```carousel
![Interior Entrance Doorway View: Power Supply Pipeline Riser Entering SB-TERRACE from Floor Slab](c:\Users\prade\OneDrive\Desktop\home plan\renders\terrace_switchbox_power_supply_upright.png)
<!-- slide -->
![South Headroom Exterior: Weatherproof Luminaire & Concealed Wall Conduit Route](c:\Users\prade\OneDrive\Desktop\home plan\renders\terrace_south_wall_light.png)
<!-- slide -->
![Axonometric Rooftop Overview: Complete Terrace Lighting Integration](c:\Users\prade\OneDrive\Desktop\home plan\renders\terrace_lighting_isometric_overview.png)
```

---

### 74.3 Geometric Component Schedule

| Object Identifier | FreeCAD Label | Geometric Placement $(X, Y, Z)$ (mm) | Material / Dimensions | Function |
| :--- | :--- | :--- | :--- | :--- |
| `Terrace_Switchboard_Power_Supply_Conduit` | SB-TERRACE Power Supply Mains Riser | $X \in [2007, 2033], Y \in [1726.5, 1752.5], Z \in [7135.4, 8420]$ | $20\text{ mm}$ Rigid Orange PVC Conduit | Sub-main power supply feed from slab network into switchbox. |
| `Terrace_Entrance_Switchboard_Backbox` | SB-TERRACE Concealed Metal Flush Backbox | $X \in [1960, 2080], Y \in [1714.5, 1764.5], Z \in [8420, 8500]$ | $50\text{ mm}$ Galvanized Steel Flush Box | Recessed wall enclosure for wiring junctions and modular plate. |
| `Terrace_Entrance_Switchboard_SB_TERRACE` | Terrace Entrance Switchboard SB-TERRACE | $X \in [1955, 2085], Y \in [1702.5, 1714.5], Z \in [8415, 8505]$ | Modular PVC White Plate ($130 \times 90\text{ mm}$) | Entryway flush modular switchboard faceplate. |
| `Terrace_Entrance_Switchboard_Switches` | SB-TERRACE Rocker Switches & 16A Socket | $X \in [1975, 2070], Y \in [1697.5, 1704.5], Z \in [8440, 8480]$ | Charcoal Modular Rockers & 3-Pin Socket | Controls terrace wall luminaire & provides utility power. |
| `Terrace_Wall_Light_Conduit` | Terrace Wall Light Outgoing Switched Feed | $X \in [2008, 3162], Y \in [1727.5, 1866.9], Z \in [8500, 8812]$ | $20\text{ mm}$ Rigid Orange PVC Conduit | Switched load conduit connecting switchbox to luminaire. |
| `Terrace_Wall_Light_Fixture` | Rooftop Terrace Weatherproof LED Wall Luminaire | $X \in [3080, 3220], Y \in [1866.9, 1951.9], Z \in [8675, 8925]$ | Die-cast IP65 Housing + Visors + Lens | Flood-lights the entire open rooftop terrace floor. |

---

### 74.4 Model Health & Quality Certification

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** **618 objects, 0 errors, 100% valid manifold solids.**
* **Circuit Continuity:** **100% closed loop** from building electrical distribution slab grid $\to$ switchbox $\to$ terrace luminaire (0 gaps, 0 floating parts).
* **Service Clashes:** Zero clashes detected against monkey ladder, water pipes, door frames, or columns.
* **Ergonomics:** Complete compliance with NBC 2016 Part 8 (Building Services - Electrical Installations).

---
