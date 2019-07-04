import csv
#import numpy as np
import matplotlib.pyplot as plt
#from numpy import *
import sys



sentence=[]

with open("4_luglio_GAL_E5a/RawMeasurementsLogger_RawLog_2019_07_04_06_38_22.txt", "r") as data_file:
    data_file_lines = data_file.readlines()

#skip header
no_header_file = data_file_lines[9:]

data = list()
for line in no_header_file:
    clean_line = line.strip()
    record = clean_line.split(',')
    data.append(record)

Svid = []
print(data[0][0])
print(len(data))
for i in range(len(data)):
    if data[i][0] == "Fix":
        continue
    else:
        if data[i][11] not in Svid:
            Svid.append(data[i][11])
        else:
            continue
print(Svid)
#### Constellation Type ####
# GPS = 1
# GLONASS = 3
# QZSS = 4
# BEIDOU = 5
# GALILEO = 6
# SBAS = 2
# UNKNOWN = 9

ConstellationType=[]
for i in range(len(data)):
    if data[i][0] == "Fix":
        continue
    else:
        if data[i][25] not in ConstellationType:
            ConstellationType.append(data[i][25])
        else:
            continue

#
ReceivedConst=[]
for i in ConstellationType:
    if i == '1':
        ReceivedConst.append('GPS')
    elif i == '2':
        ReceivedConst.append('SBAS')
    elif i == '3':
        ReceivedConst.append('GLONASS')
    elif i == '4':
        ReceivedConst.append('QZSS')
    elif i == '5':
        ReceivedConst.append('BEIDOU')
    elif i == '6':
        ReceivedConst.append('GALILEO')
    else:
        ReceivedConst.append('UNKNOWN')


print(ConstellationType)
print(ReceivedConst)

sys.exit()
'''
print((data[4][11]))
#SVID (cioè sat id è il record 11)

#list(set([data[i][11] for i in range(len(data))]))
'''
#Cn0 record16
prova = ['8', '11', '7']

for i in Svid:
    print(i)
    CN0_Svid=[]
    for j in range(len(data)):
        if data[j][0] == "Fix":
            continue
        else:
            if data[j][11] == i:
                CN0_Svid.append(float(data[j][16]))
            else: 
        
                continue
    plt.plot(range(len(CN0_Svid)), CN0_Svid, label="Svid {0}".format(i))
plt.title("C/N0 [dB-Hz]")
plt.xlabel("time [s]")
plt.grid(linestyle='--')
plt.legend(loc='upper right')
    

plt.show()



sys.exit()
CN0_Svid =[]

for i in range(len(data)):
    if data[i][0] == "Fix":
        continue
    else:
        if data[i][11] == '29':
            CN0_Svid.append(float(data[i][16]))
        else:
            continue




CN0_Svid1 =[]

for i in range(len(data)):
    if data[i][0] == "Fix":
        continue
    else:
        if data[i][11] == '6':
            CN0_Svid1.append(float(data[i][16]))
        else:
            continue








plt.plot(range(len(CN0_Svid)), CN0_Svid, label="Svid 29")
plt.plot(range(len(CN0_Svid1)), CN0_Svid1, label="Svid 6")
plt.title("C/N0 [dB-Hz]")
plt.xlabel("time [s]")
plt.legend(loc='upper left')

plt.show()