# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:49:50 2022

@author: Thomas
"""

import matplotlib.pyplot as plt
from pandas import read_csv
from scipy.ndimage import gaussian_filter1d
import numpy as np

#%% Section 1 NPN Data Read, Gaussian Smoothing and Plotting

NPN10uA = (read_csv("BC547_NPN_10uA.csv"))
NPN10uA['VCE (V)'] = gaussian_filter1d(NPN10uA['VCE (V)'], sigma =1.5)
NPN10uA['IC (mA)'] = gaussian_filter1d(NPN10uA['IC (mA)'], sigma =1.5)
plt.plot(NPN10uA['VCE (V)'], NPN10uA['IC (mA)'], label='10uA')

NPN20uA = (read_csv("BC547_NPN_20uA.csv"))
NPN20uA['VCE (V)'] = gaussian_filter1d(NPN20uA['VCE (V)'], sigma =1.5)
NPN20uA['IC (mA)'] = gaussian_filter1d(NPN20uA['IC (mA)'], sigma =1.5)
plt.plot(NPN20uA['VCE (V)'], NPN20uA['IC (mA)'], label='20uA')

NPN30uA = (read_csv("BC547_NPN_30uA.csv"))
NPN30uA['VCE (V)'] = gaussian_filter1d(NPN30uA['VCE (V)'], sigma =1.5)
NPN30uA['IC (mA)'] = gaussian_filter1d(NPN30uA['IC (mA)'], sigma =1.5)
plt.plot(NPN30uA['VCE (V)'], NPN30uA['IC (mA)'], label='30uA')

NPN40uA = (read_csv("BC547_NPN_40uA.csv"))
NPN40uA['VCE (V)'] = gaussian_filter1d(NPN40uA['VCE (V)'], sigma =1.5)
NPN40uA['IC (mA)'] = gaussian_filter1d(NPN40uA['IC (mA)'], sigma =1.5)
plt.plot(NPN40uA['VCE (V)'], NPN40uA['IC (mA)'], label='40uA')

NPN50uA = (read_csv("BC547_NPN_50uA.csv"))
NPN50uA['VCE (V)'] = gaussian_filter1d(NPN50uA['VCE (V)'], sigma =1.5)
NPN50uA['IC (mA)'] = gaussian_filter1d(NPN50uA['IC (mA)'], sigma =1.5)
plt.plot(NPN50uA['VCE (V)'], NPN50uA['IC (mA)'], label='50uA')

plt.title("IV Characteristic Curves of BC547 NPN Transistor", fontsize=17)
plt.xlabel("VCE (V)", fontsize=14)
plt.ylabel("IC (mA)", fontsize=14)
plt.legend(title="Supplied Base Current")
plt.grid()
plt.savefig('BC547NPN.eps', dpi=350)
plt.show()

#%% Section 1 PNP Data Read, Gaussian Smoothing and Plotting

PNP10uA = (read_csv("BC557_PNP_10uA.csv"))
PNP10uA['VCE (V)'] = gaussian_filter1d(PNP10uA['VCE (V)'], sigma =1)
PNP10uA['IC (mA)'] = gaussian_filter1d(PNP10uA['IC (mA)'], sigma =1)
plt.plot(PNP10uA['VCE (V)'], PNP10uA['IC (mA)'], label='10uA')

PNP20uA = (read_csv("BC557_PNP_20uA.csv"))
PNP20uA['VCE (V)'] = gaussian_filter1d(PNP20uA['VCE (V)'], sigma =1)
PNP20uA['IC (mA)'] = gaussian_filter1d(PNP20uA['IC (mA)'], sigma =1)
plt.plot(PNP20uA['VCE (V)'], PNP20uA['IC (mA)'], label='20uA')

PNP30uA = (read_csv("BC557_PNP_30uA.csv"))
PNP30uA['VCE (V)'] = gaussian_filter1d(PNP30uA['VCE (V)'], sigma =1)
PNP30uA['IC (mA)'] = gaussian_filter1d(PNP30uA['IC (mA)'], sigma =1)
plt.plot(PNP30uA['VCE (V)'], PNP30uA['IC (mA)'], label='30uA')

PNP40uA = (read_csv("BC557_PNP_40uA.csv"))
PNP40uA['VCE (V)'] = gaussian_filter1d(PNP40uA['VCE (V)'], sigma =1)
PNP40uA['IC (mA)'] = gaussian_filter1d(PNP40uA['IC (mA)'], sigma =1)
plt.plot(PNP40uA['VCE (V)'], PNP40uA['IC (mA)'], label='40uA')

PNP50uA = (read_csv("BC557_PNP_50uA.csv"))
PNP50uA['VCE (V)'] = gaussian_filter1d(PNP50uA['VCE (V)'], sigma =1)
PNP50uA['IC (mA)'] = gaussian_filter1d(PNP50uA['IC (mA)'], sigma =1)
plt.plot(PNP50uA['VCE (V)'], PNP50uA['IC (mA)'], label='50uA')

plt.title("IV Characteristic Curves of BC557 PNP Transistor", fontsize=17)
plt.xlabel("VCE (V)", fontsize=14)
plt.ylabel("IC (mA)", fontsize=14)
plt.legend(title="Supplied Base Current")
plt.grid()
plt.savefig('BC557PNP.eps', dpi=350)

#%% Section 2 Heat Graph

TwoResHeat = read_csv("2ResBiasHeat.csv")
TwoResHeat["IB (mA)"] = TwoResHeat["IB (mA)"]*1000
fig, ax1 = plt.subplots()
ax1.plot(TwoResHeat["Time"], TwoResHeat["IB (mA)"], 'g', label="IB (Micro A)")
plt.xlabel("Seconds", fontsize=14)
plt.ylabel("Micro Amps", fontsize=14)
ax2 = ax1.twinx()
ax2.plot(TwoResHeat["Time"], TwoResHeat["B ()"], 'orange', label="Gain")
ax2.plot([],[],'g',label="IB (MicroA)")
plt.ylabel("Gain", fontsize = 14)
plt.grid()
plt.legend(loc=6)
plt.title("2 Resistor Bias Transformer Circuit: Gain vs IB when heat applied", fontsize=17)
plt.savefig('2ResHeat.eps', dpi=350)

plt.show()

FourResHeat = read_csv("4ResBiasHeat.csv")
FourResHeat["IB (mA)"] = FourResHeat["IB (mA)"]*1000
FourResHeat['IB (mA)'] = gaussian_filter1d(FourResHeat['IB (mA)'], sigma =5)
FourResHeat['B ()'] = gaussian_filter1d(FourResHeat['B ()'], sigma =5)
fig, ax1 = plt.subplots()
ax1.plot(FourResHeat["Time (s)"], FourResHeat["IB (mA)"], 'g', label="IB (Micro A)")
plt.xlabel("Seconds", fontsize=14)
plt.ylabel("Micro Amps", fontsize=14)
ax2 = ax1.twinx()
ax2.plot(FourResHeat["Time (s)"], FourResHeat["B ()"], 'orange', label="Gain")
ax2.plot([],[],'g',label="IB (MicroA)")
plt.ylabel("Gain", fontsize = 14)
plt.grid()
plt.legend(loc=6)
plt.title("4 Resistor Bias Transformer Circuit: Gain vs IB when heat applied", fontsize=17)
plt.savefig('4ResHeat.eps', dpi=350)

plt.show()
#%% Part 3 With load line plotted

NPN10uA = (read_csv("BC547_NPN_10uA.csv"))
NPN10uA['VCE (V)'] = gaussian_filter1d(NPN10uA['VCE (V)'], sigma =1.5)
NPN10uA['IC (mA)'] = gaussian_filter1d(NPN10uA['IC (mA)'], sigma =1.5)
plt.plot(NPN10uA['VCE (V)'], NPN10uA['IC (mA)'], label='10uA')

NPN20uA = (read_csv("BC547_NPN_20uA.csv"))
NPN20uA['VCE (V)'] = gaussian_filter1d(NPN20uA['VCE (V)'], sigma =1.5)
NPN20uA['IC (mA)'] = gaussian_filter1d(NPN20uA['IC (mA)'], sigma =1.5)
plt.plot(NPN20uA['VCE (V)'], NPN20uA['IC (mA)'], label='20uA')

NPN30uA = (read_csv("BC547_NPN_30uA.csv"))
NPN30uA['VCE (V)'] = gaussian_filter1d(NPN30uA['VCE (V)'], sigma =1.5)
NPN30uA['IC (mA)'] = gaussian_filter1d(NPN30uA['IC (mA)'], sigma =1.5)
plt.plot(NPN30uA['VCE (V)'], NPN30uA['IC (mA)'], label='30uA')

NPN40uA = (read_csv("BC547_NPN_40uA.csv"))
NPN40uA['VCE (V)'] = gaussian_filter1d(NPN40uA['VCE (V)'], sigma =1.5)
NPN40uA['IC (mA)'] = gaussian_filter1d(NPN40uA['IC (mA)'], sigma =1.5)
plt.plot(NPN40uA['VCE (V)'], NPN40uA['IC (mA)'], label='40uA')

NPN50uA = (read_csv("BC547_NPN_50uA.csv"))
NPN50uA['VCE (V)'] = gaussian_filter1d(NPN50uA['VCE (V)'], sigma =1.5)
NPN50uA['IC (mA)'] = gaussian_filter1d(NPN50uA['IC (mA)'], sigma =1.5)
plt.plot(NPN50uA['VCE (V)'], NPN50uA['IC (mA)'], label='50uA')

llx = np.arange(0, 12, 0.001) # Load Line x values
lly =  ((-0.916*llx)+11) #Load Liney values
plt.plot(llx, lly,'red', label = ('Load Line')) 
#idx = np.argwhere(np.diff(np.sign(lly - NPN20uA['IC (mA)']))).flatten()
#plt.plot(llx[idx], lly[idx], 'ro', label =("{:.2}".format(llx[idx][0]) + "V, "+"0.00mA"))


plt.title("IV Characteristic Curves of BC547 NPN Transistor", fontsize=17)
plt.xlabel("VCE (V)", fontsize=14)
plt.ylabel("IC (mA)", fontsize=14)
plt.legend(title="Supplied Base Current")
plt.grid()
plt.savefig('BC547NPN_LoadLine.eps', dpi=350)
plt.show()