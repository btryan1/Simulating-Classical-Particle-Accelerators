from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np

time = 0  # initial time stamp

deltat =1e-06
  # time steps of 1ms
deltat_2=0.0002E-5
times = []
times_2=[]
Positions=[]
particle=Proton()
BField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
Cyclo_Frequency=BField.Cyclotron_Frequency(particle)
square_sig=BField.Square_Wave_Gen(Cyclo_Frequency)
PB=ChargedParticleBunch()
CM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
radius_of_orbit=1.4893437568218113
L=0.07446718784109056
Bunch=PB.Generate_Bunch(100)
Time_period=CM.Orbit_Period(Bunch)
Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
while time<=Time_period:
        Averages=CM.Averages(Bunch)
        Average_Positons.append(Averages[0])
        Average_Velocities.append(Averages[1])
        Average_Kinetic_Energies.append(Averages[2])
        Bunch=CM.Bunch_Update(Bunch,deltat,2)
        time += deltat

  

pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositionsConstant.csv')
print('100ProtonPositionsConstant.csv has been saved')
