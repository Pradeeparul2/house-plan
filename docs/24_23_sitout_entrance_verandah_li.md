## 23. Sitout & Entrance Verandah Lighting and Conduit Integration

Following user inspection, the previously missing **Sitout / Entrance Verandah ceiling downlight and electrical conduit connections** were designed and integrated across both floors (**Ground Floor Sitout** and **First Floor Balcony Verandah**):

```carousel
![Ground Floor Top-View Electrical Layout Showing the New Sitout Light Pot and Tri-Conduit Connections](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\gf_sitout_light_top_view.png)
<!-- slide -->
![First Floor Top-View Electrical Layout Showing the Matching Balcony Verandah Light Pot and Conduits](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_sitout_light_top_view.png)
```

### 23.1 Sitout Light Pot Specifications
* **Geometric Location:** Center of the $6'\text{-}0" \times 6'\text{-}0"$ entrance sitout/balcony slab:
  - Coordinates: $(X = 857.0\text{ mm}, Y = 857.0\text{ mm})$
  - **Ground Floor Sitout Ceiling:** $Z = 3962.4 - 4022.4\text{ mm}$ (Deep galvanized junction pot $\varnothing 85\text{ mm}$, height $60\text{ mm}$ in `Electrical_Slab_Light_Pots`).
  - **First Floor Balcony Ceiling:** $Z = 7135.4 - 7195.4\text{ mm}$ (Matching junction pot in `FF_Electrical_Slab_Light_Pots`).
* **Illumination Function:** Accommodates a 9W/12W IP44-rated warm-white LED ceiling downlight, providing ambient entrance illumination for the sitout steps, main door, and shoe-rack area.

### 23.2 Tri-Conduit Circuit Routing
To ensure robust switching control and circuit continuity, 3 dedicated $25\text{ mm}$ rigid PVC conduits were added to the slab networks (`Electrical_Slab_Conduit_Network` and `FF_Electrical_Slab_Conduit_Network`):
1. **Power Feed Conduit (MDB to Sitout Light):**
   - Connects from the Living Room MDB / Entrance drop at $(1600.0, 1943.1\text{ mm})$ to the Sitout Light Pot at $(857.0, 857.0\text{ mm})$.
   - Length: $1315.9\text{ mm}$.
2. **Switching Control Line (Sitout Light to Entrance Switchboard `SB-14`):**
   - Connects from the Sitout Light Pot at $(857.0, 857.0\text{ mm})$ to the Front Entrance Switchboard drop at $(1987.5, 247.5\text{ mm})$.
   - Length: $1284.3\text{ mm}$.
3. **Secondary Switching / 2-Way Line (Sitout Light to Foyer Switchboard `SB-1`):**
   - Connects from the Sitout Light Pot at $(857.0, 857.0\text{ mm})$ to the North Foyer / Staircase Wall Switchboard drop at $(2275.0, 797.5\text{ mm})$.
   - Length: $1419.2\text{ mm}$.
   - Allows convenient 2-way control of the entrance light from either the outer sitout gate or the inner foyer door.





---
