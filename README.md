# CEA CALCULATOR
A python sciprt which uses NASA's CEA to calculate C*, Isp, Chamber Temperature, Mass Flow Rate and Throat Area for any liquid bipropellant rocket engine.

## Inputs
Set these at the top of the script:
- Fuel
- Oxidiser
- O/F Ratio
- Chamber Pressure
- Contraction Ratio
- Expansion Ratio
- Throat Diameter

The script also plots C* and Isp against O/F for every integer of O/F in the range of 0 to 20

## Installation
1. Clone git
```bash
git clone https://github.com/asherlok/hypower-cea.git
cd hypower-cea
```
2. Create and activate virtual environment
```bash
python -m venv .venv
```

3. Install dependencies
```bash
pip install rocketcea matplotlib tabulate
```

## Usage
Edit the engine details at the top of the script, then run:
```bash
python hypower_cea_calc.py
```

## Limitations
- Results are ideal equilibrium values from CEA, so real engines will perform worse
- Propellant names must be ones RocketCEA recognises
- Film cooling and additives are not modelled