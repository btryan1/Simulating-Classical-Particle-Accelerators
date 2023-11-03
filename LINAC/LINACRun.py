from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np
import matplotlib.pyplot as plt

time = 0  # initial time stamp
time2=0
deltat =0.5e-06  # time steps of 1ms
deltat_2=0.0002E-5
times = []
times_2=[]
Positions=[]
particle=Proton()
ZeroField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
square_sig,t=ZeroField.Linear_Square_Wave_Gen(50000)
PB=ChargedParticleBunch()
EM=ChargedParticleBunch(electric = np.array([10,0,0], dtype=float), magnetic = np.array([0,0,0], dtype=float))
ZeroEM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,0], dtype=float))
radius_of_orbit=2.9868732070658437
L=0.09
offset=0.9427024015157145
Bunch=PB.Generate_Bunch(1)

Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
lines=[0,0.2]
Averages=EM.Averages(Bunch)
Average_Positons.append(Averages[0])
Average_Velocities.append(Averages[1])
Average_Kinetic_Energies.append(Averages[2])
Bunch=EM.Bunch_Update(Bunch,deltat,2)
times.append(time)
time += deltat
check=Average_Positons[-1]
it=1
iter=1
ver=0
for i in range(6):
    while check[0]<=L:
            Averages=EM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=EM.Bunch_Update(Bunch,deltat,2)
            times.append(time)
            time += deltat
            check=Average_Positons[-1]
    while square_sig[it]==iter:
            it+=1
            Averages=ZeroEM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=ZeroEM.Bunch_Update(Bunch,deltat,2)
            times.append(time)
            time += deltat
    check2=(Average_Positons[-1])[0]
    lines.append(check2)
    lines.append(check2+L)
    check3=check2+1E-10
    Check=check3-check2
    iter*=-1
    while Check<=L:
            Averages=EM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=EM.Bunch_Update(Bunch,deltat,2)
            times.append(time)
            time += deltat
            time2+=deltat
            check3=(Average_Positons[-1])[0]
            Check=check3-check2
    print(lines)


pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositions.csv')
pd.DataFrame(Average_Kinetic_Energies).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergy.csv')


pd.DataFrame(times).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimes.csv')
