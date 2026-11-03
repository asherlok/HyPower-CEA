# CEA CALCULATOR
A python sciprt which uses NASA's CEA to calculate C*, Isp, Chamber Temperature, Mass Flow Rate and Throat Area for any liquid bipropellant rocket engine.

Must provide the following:
- Fuel
- Oxidiser
- O/F Ratio
- Chamber Pressure
- Contraction Ratio
- Expansion Ratio
- Throat Diameter

The script also plots C* and Isp against O/F for every integer of O/F in the range of 0 to 20

# INSTALLATION
1. Clone git
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python -m venv .venv

2. ACTIVATE THE VIRTUAL ENVIRONMENT
.\.venv\Scripts\Activate.ps1

3. INSTALL DEPENDENCIES
pip install rocketcea matplotlib tabulate