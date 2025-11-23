# 🇮🇳 P.R.A.H.A.R.

## Planetary Risk Assessment for Hazardous Asteroid Reentry


> **"प्रहार (Prahaar) - The Strike Before Impact"**

A terminal-based asteroid impact simulator inspired by ISRO's planetary defense initiatives. I built this to explore impact mechanics and make planetary defense calculations accessible. It uses real physics to show what happens when asteroids hit Earth.

### SUBMITTED BY -                                   
### Name- Ishan Shrivas
### Registration number -25BAI10966

---

## What It Does

This program calculates the consequences of asteroid impacts using actual physics formulas. You input the asteroid's size, composition, and speed - it tells you the energy release, crater size, and threat level.

**Key Features:**
- Real physics calculations (kinetic energy, crater formation, seismic effects)
- ISRO observatory simulation (NETRA, Devasthal, Mount Abu, Hanle)
- Hindi-inspired asteroid names (Vajra, Agni, Pralaya, etc.)
- Four-phase threat assessment system
- Historical event comparisons (Tunguska, Chicxulub, Chelyabinsk)
- Color-coded threat levels (🟢 Local → 🟡 Regional → 🔴 Global → 🟣 Extinction)

---

## Getting Started

**Requirements:**
- Python 3.7 or higher
- No external libraries needed (uses only standard library)

**Installation:**
```bash
# Clone the repository
git clone https://github.com/enchanter-coder/VITyarthi-project.git

# Navigate to folder
cd Vityarthi

# Run the program
python PRAHAR.py
```

---

## How to Use

Run the script and follow the prompts:

```bash
python PRAHAR.py
```

The program will ask for:
1. **Diameter** - Size of the asteroid in meters
2. **Type** - Composition (C=Carbonaceous, S=Stony, M=Metallic)
3. **Velocity** - Impact speed in km/s

Then it runs the simulation and shows a detailed impact report.

**Example Session:**
```
🇮🇳 P.R.A.H.A.R. 🇮🇳
Planetary Risk Assessment for Hazardous Asteroid Reentry
🛰️ A scientific initiative by ISRO

⚠️ PHASE 1: DETECTION ⚠️
🚨 ALERT: Detected by NETRA (Network for Space Objects Tracking)
📡 Object: Vajra-3847
⚠️ STATUS: Potential Earth impactor

📏 Enter asteroid DIAMETER (metres): 500

🔬 PHASE 2: SPECTRUM ANALYSIS 🔬
[Shows asteroid type options]
🎯 Select type [C/S/M]: M

🎯 PHASE 3: TRAJECTORY 🎯
⚡ Enter impact VELOCITY (km/s): 25

💥 PHASE 4: IMPACT SIMULATION 💥
🔬 RUNNING PHYSICS SIMULATION...

📊 IMPACT REPORT 📊
Object: Vajra-3847
Energy: 6,375 megatons
Crater: 18.54 km diameter
Threat Level: 🔴 GLOBAL CATASTROPHE
```

---

## Asteroid Types

**C-Type (Carbonaceous)**
- Density: 1,500 kg/m³
- Dark, carbon-rich (like compressed coal)
- Most common (~75% of asteroids)

**S-Type (Stony)**
- Density: 3,000 kg/m³
- Rocky, silicate composition
- Second most common (~17% of asteroids)

**M-Type (Metallic)**
- Density: 7,800 kg/m³
- Iron-nickel core - densest and deadliest
- Rarest (~8% of asteroids)

---

## Threat Levels

**🟢 LOCAL EVENT** (<1 MT)
- Minor regional damage
- Building damage in immediate area
- Example: Small airbursts

**🟡 REGIONAL THREAT** (1-100 MT)
- Can destroy a major city
- Severe damage 50-100 km away
- Example: Tunguska event (1908)

**🔴 GLOBAL CATASTROPHE** (100-10,000 MT)
- Continental devastation
- Impact winter possible
- Agricultural collapse likely

**🟣 EXTINCTION LEVEL EVENT** (>10,000 MT)
- Biosphere collapse
- Mass extinction
- Example: Chicxulub (dinosaur killer)

---

## Physics Behind It

The program uses these formulas:

**Volume (spherical asteroid):**
```
V = (4/3) × π × r³
```

**Mass:**
```
m = ρ × V
(ρ = density in kg/m³)
```

**Kinetic Energy:**
```
KE = (1/2) × m × v²
```

**TNT Equivalent:**
```
E_MT = KE / (4.184 × 10¹⁵ J)
(1 megaton = 4.184 × 10¹⁵ Joules)
```

**Crater Diameter:**
```
D = 1000 × ∛(E_MT) meters
(simplified scaling law)
```

**Richter Magnitude:**
```
M = 0.67 × log₁₀(E_MT) + 5.87
```

**Fireball Radius:**
```
R = 140 × (E_MT)^0.4 meters
```

---

## Try These Scenarios

**Chelyabinsk Meteor (2013)**
```
Diameter: 20 m
Type: S (Stony)
Velocity: 19 km/s
Result: ~0.5 MT (matches real event!)
```

**Tunguska Event (1908)**
```
Diameter: 60 m
Type: S (Stony)
Velocity: 15 km/s
Result: ~10 MT (flattened 2,000 km² of forest)
```

**City Killer**
```
Diameter: 300 m
Type: M (Metallic)
Velocity: 25 km/s
Result: ~1,000 MT regional catastrophe
```

**Dinosaur Extinction**
```
Diameter: 10,000 m (10 km)
Type: S (Stony)
Velocity: 20 km/s
Result: 100+ million MT extinction event
```

---

## Technical Details

**Language:** Python 3.7+

**Standard Library Modules:**
- `math` - Mathematical calculations
- `time` - Animation delays
- `random` - Observatory/name selection

**Performance:**
- Instant calculations (sub-second)
- No internet required
- Memory footprint <1 MB

**Code Structure:**
- Physics functions for all calculations
- User interaction functions for each phase
- Historical database for comparisons
- Asteroid name generator using Hindi words

---

## Why This Matters

Asteroid impacts are real threats:

- **66 million years ago** - Chicxulub impact killed the dinosaurs (10 km asteroid)
- **1908** - Tunguska event flattened 2,000 km² of Siberian forest
- **2013** - Chelyabinsk meteor injured 1,500 people in Russia
- **Today** - NASA/ISRO track 30,000+ near-Earth objects

**ISRO's Role:**
- NETRA system tracks space debris and NEOs
- Space Situational Awareness program monitors threats
- Growing planetary defense capabilities

This tool helps visualize the scale of these impacts and understand the physics behind planetary defense.

---

## Educational Use

**Good for:**
- High school physics students (energy, momentum, impact dynamics)
- Space enthusiasts learning about planetary defense
- Anyone curious about asteroid threats
- Understanding scale of cosmic impacts

**Learning Topics:**
- Kinetic energy calculations
- Logarithmic scales
- Scientific notation
- Impact physics
- Threat assessment

---

## About the Name

**PRAHAR (प्रहार)** means "strike" or "attack" in Hindi/Sanskrit. It's also the name of India's tactical ballistic missile system. The acronym stands for:

**P**lanetary **R**isk **A**ssessment for **H**azardous **A**steroid **R**eentry

The double meaning works perfectly - both striking (the missile) and being struck (the asteroid impact).

---

## Indian Observatory References

The program uses real ISRO facilities:

**NETRA** - Network for Space Objects Tracking
- ISRO's space debris tracking system
- Located in multiple sites across India

**Devasthal Observatory** - Uttarakhand
- Houses Asia's largest optical telescope (3.6m)
- Operated by Aryabhatta Research Institute

**Mount Abu Observatory** - Rajasthan
- Oldest operating observatory in India
- Infrared astronomy facility

**Indian Astronomical Observatory** - Hanle, Ladakh
- World's highest astronomical observatory (4,500m altitude)
- Operated by Indian Institute of Astrophysics

---

## Hindi Asteroid Names

Each simulation randomly generates names using these Sanskrit/Hindi words:

- **Ashani** (अशनि) - Lightning, Thunderbolt
- **Vajra** (वज्र) - Divine Weapon, Thunder
- **Agni** (अग्नि) - Fire
- **Rudra** (रुद्र) - Storm God, Destroyer aspect of Shiva
- **Kaal** (काल) - Time, Death
- **Vinash** (विनाश) - Destruction
- **Pralaya** (प्रलय) - Apocalypse, Cosmic Dissolution
- **Mahakal** (महाकाल) - Great Time, Supreme Destroyer

These names are combined with random 4-digit IDs (e.g., "Vajra-3847").

---

## Future Improvements

Ideas I'm considering:
- Impact angle variations (currently assumes 45°)
- Ocean vs land impact differences
- Atmospheric entry calculations for smaller objects
- Deflection mission calculator (time required, delta-v needed)
- Multiple impact scenarios
- Save simulation results to file

---

## Contact

If you have questions or suggestions, feel free to reach out:
- GitHub: https://github.com/enchanter-coder
- Email: juststudiesmail@gmail.com

---

**Made with 💖 for planetary defense awareness**

**प्रहार (Prahaar) - Strike Before Impact**
