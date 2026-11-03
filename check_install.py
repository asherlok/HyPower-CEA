# IMPORTING LIBRARIES
from rocketcea.cea_obj_w_units import CEA_Obj
import math
import matplotlib.pyplot as plt
from tabulate import tabulate

# INPUT ENGINE DATA (Engine 2 as reference)
fuel="Isopropanol"
oxidiser="N2O"
of_ratio=3
chamber_pressure=20                   # In bar
contraction_ratio=6
expansion_ratio=3.36
throat_diameter=48.54                 # In mm

# DISPLAY INPUTS
print("- ENGINE INPUTS -")
print(f"FUEL = {fuel}")
print(f"OXIDISER = {oxidiser}")
print(f"O/F RATIO = {of_ratio}")
print(f"CHAMBER PRESSURE = {chamber_pressure} bar")
print(f"CONTRACTION RATIO = {contraction_ratio}")
print(f"EXPANSION RATIO = {expansion_ratio}")
print(f"THROAT DIAMETER = {throat_diameter} mm")

# DEFINE UNITS FOR CEA
cea = CEA_Obj(fuelName=fuel,oxName=oxidiser,cstar_units="m/s",isp_units="sec",pressure_units="Bar",temperature_units="K",fac_CR=None)

# CALCULATING C*, ISP, CHAMBER TEMPERATURE, MASS FLOW RATE, THROAT AREA
cstar=cea.get_Cstar(Pc=chamber_pressure, MR=of_ratio)                             # Calculates C* in m/s
isp=cea.get_Isp(Pc=chamber_pressure, MR=of_ratio, eps=expansion_ratio)            # Calculates specific impulse in sec
chamber_temp=cea.get_Tcomb(Pc=chamber_pressure, MR=of_ratio)                      # Calculates chamber temperature in K
mass_flow_rate=chamber_pressure*100000*math.pi*(throat_diameter/2000)**2/cstar    # Calculates mass flow rate in kg/s
throat_area=math.pi*(throat_diameter/2000)**2                                     # Calculates throat area in m^2 

print(tabulate([["C*",cstar,"m/s"],["ISP",isp,"sec"],["Chamber Temperature",chamber_temp,"K"],["Mass Flow Rate",mass_flow_rate,"kg/s"],["Throat Area",throat_area,"m^2"]],headers=["CEA OUTPUT","VALUE","UNITS"],tablefmt="grid",colalign=("left","right","left")))

# PLOTTING GRAPHS
of_values=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cstar_values=[cea.get_Cstar(Pc=chamber_pressure, MR=of) for of in of_values]
isp_values=[cea.get_Isp(Pc=chamber_pressure, MR=of, eps=expansion_ratio) for of in of_values]

plt.plot(of_values,cstar_values,marker='o',color='b')
plt.xlim(0,20)
plt.ylim(0,2500)
plt.xticks(range(0, 21))
plt.xlabel("O/F")
plt.ylabel("C* (m/s)")
plt.title("C* vs O/F")
plt.grid(True)
plt.show()

plt.plot(of_values,isp_values,marker='o',color='r')
plt.xlim(0,20)
plt.ylim(0,500)
plt.xticks(range(0, 21))
plt.xlabel("O/F")
plt.ylabel("ISP (sec)")
plt.title("ISP vs O/F")
plt.grid(True)
plt.show()