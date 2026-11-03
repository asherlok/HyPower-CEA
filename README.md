# CEA CALCULATOR
A python sciprt which uses NASA's CEA to calculate C*, Isp, Chamber Temperature, Mass Flow Rate and Throat Area for any liquid bipropellant rocket engine.

Feed the following into the calculator:
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
git clone https://github.com/asherlok/hypower-cea.git
cd hypower-cea
python -m venv .venv

2. ACTIVATE THE VIRTUAL ENVIRONMENT
.\.venv\Scripts\Activate.ps1

3. INSTALL DEPENDENCIES
pip install rocketcea matplotlib tabulate


# USAGE
Edit the engine details at the top of the script and then run