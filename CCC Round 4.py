# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 17:30:44 2022

@author: Thomas
"""
import matplotlib.pyplot as plt
from pandas import read_csv

data = (read_csv("CCC Round 4 First_Last_Omitted.csv"))

plt.plot(data['Lap'], data['Pete'], 'o',  label='Pete')
plt.plot(data['Lap'], data['Tom'], 'o', label='Tom')
plt.plot(data['Lap'], data['Mark'], 'o', label='Mark')
plt.plot(data['Lap'], data['Dylan'], 'o', label='Dylan')
plt.ylabel('Lap Time (s)')
plt.xlabel('Lap Number')
plt.ylim(64,73)
plt.grid()
plt.legend()
plt.title('eXpreSSSo Martini Round 4 Lap Times \n (First and last of each stint ommitted)')
plt.savefig('CCC Round 4.png', dpi=400)
plt.show()
