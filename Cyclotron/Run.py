from tkinter import Y
from Particle import Proton
from GeneralEMField2 import EMField
import pandas as pd
from GenerateParticleBunch import ChargedParticleBunch
import numpy as np

time = 0  # initial time stamp
time2=0
deltat =1e-07  # time steps of 1ms
deltat_2=0.0002E-5
times = [0]
times_2=[]
Positions=[]
particle=Proton()
BField=EMField(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
Cyclo_Frequency=BField.Cyclotron_Frequency(particle)+32
square_sig=BField.Square_Wave_Gen(Cyclo_Frequency)
PB=ChargedParticleBunch()
CM=ChargedParticleBunch(electric = np.array([0,0,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
radius_of_orbit=2.9868732070658437
L=0.04
offset=1.476
Bunch=PB.Generate_Bunch(100)
Time_period=CM.Orbit_Period(Bunch)
Average_Positons=[]
Average_Velocities=[]
Average_Kinetic_Energies=[]
i=0
it=0
while time<=10*Time_period:
    if i==0:
        times.append(time)
        Averages=CM.Averages(Bunch)
        Average_Positons.append(Averages[0])
        Average_Velocities.append(Averages[1])
        Average_Kinetic_Energies.append(Averages[2])
        Bunch=CM.Bunch_Update(Bunch,deltat,2)
        time += deltat
        times.append(time)
        i+=1
    else:
        Y_avg=Average_Positons[-1]
        y=Y_avg[1]
        check=np.abs(y-offset)
        if check<=L:
            print(y,check)
            SQ_Val=square_sig[int(0.1*it)]
            EMC=ChargedParticleBunch(electric = np.array([0,SQ_Val*20,0], dtype=float), magnetic = np.array([0,0,-1E-5], dtype=float))
            Averages=EMC.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=EMC.Bunch_Update(Bunch,deltat,2)
            time += deltat
            times.append(time)
            print(SQ_Val,it)
        else:

            Averages=CM.Averages(Bunch)
            Average_Positons.append(Averages[0])
            Average_Velocities.append(Averages[1])
            Average_Kinetic_Energies.append(Averages[2])
            Bunch=CM.Bunch_Update(Bunch,deltat,2)
            time+=deltat
            times.append(time)
            it+=1




pd.DataFrame(Average_Positons).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonPositions.csv')
pd.DataFrame(Average_Kinetic_Energies).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonKineticEnergy.csv')
pd.DataFrame(times).to_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonTimes.csv')
print('All information has been saved')
