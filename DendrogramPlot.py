from os import times
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
from matplotlib.animation import FuncAnimation, PillowWriter

df = pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantPositions.csv')
df2=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantKineticEnergy.csv')
df3=pd.read_csv(r'C:\Users\benti\Documents\PHYS 389\100ProtonConstantTimes.csv')
n = 1000
number_of_frames = 1000
data = pd.DataFrame(df).to_numpy()
data2 = pd.DataFrame(df2).to_numpy()
data3 = pd.DataFrame(df3).to_numpy()

Positions=data[:,1:]
Bunch_Kinetic_Energies=data2[:,1]
Times=data3[:,1]


X_1=Positions[:,0]
Y_1=Positions[:,1]
Z_1=Positions[:,2]


def update_hist(num, data):
    print(num)
    plt.cla()
    plt.hist(data[num])

    fig = plt.figure()
    hist = plt.hist(data[7])

    animation = animation.FuncAnimation(fig, update_hist, number_of_frames, fargs=(data, ) )
        
def Extract(X_1,Y_1,Z_1):
    X=[]
    Y=[]
    Z=[]
    for i in range(0,45916,1):
        X.append(X_1[i])
        Y.append(Y_1[i])
        Z.append(Z_1[i])
    return X,Y,Z


time_percent=3.049968E-4    

X_line=[]
Y_line=[]
Z_line=[]


def update(i):
    ax.cla()

    x = X[i]
    y = Y[i]
    z = Z[i]
    X_line.append(x)
    Y_line.append(y)
    Z_line.append(z)


    ax.scatter(x, y, z, s = 10, marker = 'o')
    ax.plot(X_line, Y_line, Z_line)



    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-0.1, 0.1)

    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(projection='3d')

    anim = FuncAnimation(fig = fig, func = update, frames = frames, interval = 1, repeat = False)
    f = r'C:\Users\benti\Documents\PHYS 389\100Proton.gif'
    writergif = animation.PillowWriter(fps=30) 
    anim.save(f, writer=writergif)
    plt.show()
    plt.plot(X_1,Y_1)
    plt.axvline(x=0, c='green', lw=1, linestyle='dashed')
    plt.axvline(x=0.2, c='green', lw=1, linestyle='dashed')
    plt.axvline(x=0.43458026252932286, c='red', lw=1, linestyle='dashed')
    plt.axvline(x=0.6345802625293229, c='red', lw=1, linestyle='dashed')
    plt.axvline(x= 0.9652196887551634, c='blue', lw=1, linestyle='dashed')
    plt.axvline(x=1.1652196887551634, c='blue', lw=1, linestyle='dashed')
    plt.axvline(x=1.5211678559479282, c='yellow', lw=1, linestyle='dashed')
    plt.axvline(x=1.7211678559479282, c='yellow', lw=1, linestyle='dashed')
    plt.axvline(x=2.2404727143906094, c='purple', lw=1, linestyle='dashed')
    plt.axvline(x=2.4404727143906095, c='purple', lw=1, linestyle='dashed')
    plt.axvline(x=2.8988768141757024, c='grey', lw=1, linestyle='dashed')
    plt.axvline(x=3.0988768141757026, c='grey', lw=1, linestyle='dashed')
    plt.axvline(x=3.6219380386791786, c='black', lw=1, linestyle='dashed')
    plt.axvline(x=3.821938038679179, c='black', lw=1, linestyle='dashed')
    plt.show()
    Times=np.delete(Times,[0,-1,-2])
Maxy=max(Y_1)
Maxx=max(X_1)
Times=np.insert(Times,0,0)
Times=np.delete(Times,[0])
plt.plot(Times,Bunch_Kinetic_Energies/1.6E-19)
plt.show()
Miny=min(Y_1)
Min=min(Y_1)
print(Times[-1])
