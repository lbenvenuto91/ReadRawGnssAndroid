#Read GNSS raw data obtained from ANDROID deviced
#Lorenzo Benvenuto


import csv
#import numpy as np
import matplotlib.pyplot as plt
#from numpy import *
import sys
import math

#constants

c = 299792458 #[m/s] speed of light in vacuum

def ReadSatID (raw_file):
    '''
    This function returns the sat id read from the raw file

    '''
    
    with open(raw_file, "r") as data_file:
        data_file_lines = data_file.readlines()

        
    #skip header
    no_header_file = data_file_lines[9:]

    data = list()
    for line in no_header_file:
        clean_line = line.strip()
        record = clean_line.split(',')
        data.append(record)

    #### Constellation Type ####
    # GPS = 1
    # GLONASS = 3
    # QZSS = 4
    # BEIDOU = 5
    # GALILEO = 6
    # SBAS = 2
    # UNKNOWN = 9

    GPS=[]
    SBAS=[]
    GLONASS=[]
    BEIDOU=[]
    GALILEO=[]
    QZSS=[]
    UNKNOWN=[]
    #print(data[0][0])
    #print(len(data))

    for i in range(len(data)):
        if data[i][0] == "Fix":
            continue
        elif data[i][25]=='1':
            if data[i][11] not in GPS:
                GPS.append(data[i][11])
            else:
                continue
        elif data[i][25]=='2':
            if data[i][11] not in SBAS:
                SBAS.append(data[i][11])
            else:
                continue
        elif data[i][25]=='3':
            if data[i][11] not in GLONASS:
                GLONASS.append(data[i][11])
            else:
                continue
        elif data[i][25]=='4':
            if data[i][11] not in QZSS:
                QZSS.append(data[i][11])
            else:
                continue
        elif data[i][25]=='5':
            if data[i][11] not in BEIDOU:
                BEIDOU.append(data[i][11])
            else:
                continue
        elif data[i][25]=='6':
            if data[i][11] not in GALILEO:
                GALILEO.append(data[i][11])
            else:
                continue
        elif data[i][25]=='9':
            if data[i][11] not in UNKNOWN:
                UNKNOWN.append(data[i][11])
            else:
                continue    

    print("GPS",GPS)
    print("SBAS",SBAS)
    print("GLONASS",GLONASS)
    print("QZSS",QZSS)
    print("BEIDOU",BEIDOU)
    print("GALILEO",GALILEO)

    return(GALILEO, SBAS, GLONASS, QZSS, BEIDOU, GALILEO, UNKNOWN)

def GetSatID(Svid, Constellation):
    '''
    This function returns the sat id starting from the Svid and the Constellation

    '''
    #### Constellation Type ####
    # GPS = 1
    # GLONASS = 3
    # QZSS = 4
    # BEIDOU = 5
    # GALILEO = 6
    # SBAS = 2
    # UNKNOWN = 9

    pass


def main ():

    RawDataFile = "/home/lorenzo/Documenti/test_vilanova_ESA_summerschool/24_luglio/gadip3_mi9/RawMeasurementsLogger_RawLog_2019_07_24_12_46_02.txt"
    RawDataFileNew = "/home/lorenzo/Documenti/test_vilanova_ESA_summerschool/24_luglio/gadip3_mi9/RawMeasurementsLogger_RawLog_2019_07_24_12_46_02_Elaborato.txt"
    #ReadSatID(RawDataFile)




    with open(RawDataFile, "r") as data_file:
        data_file_lines = data_file.readlines()
   # print(type(data_file_lines))
    #print(data_file_lines[18])
    
    no_header_file = data_file_lines[9:]
    header = data_file_lines[:9]
    
    text_header = []
    for i in range(len(header)):
        l=header[i].strip()
        line = l.split(',')
        text_header.append(line)   
    print (text_header[5])
    


    text_body = []
       
    for j in range(len(no_header_file)):
        l=no_header_file[j].strip()
        line = l.split(',')
        text_body.append(line)

    
    for line in text_body:
        if line[0]=='Raw':
            ConstellationType = line[25]
            Svid = line [11]
            T_rx = int(line [14]) #ReceivedSvTimeNanos
            T_n = int(line[2]) #TimeNanos
            T_on = float(line [12]) #TimeOffsetNanos
            FBN = int(line [5]) #FullBiasNanos
            BN = float(line [6]) #BiasNanos
            print(FBN)

            if ConstellationType == '1' and Svid == '11':
                
                weekNumberNs = 604800*10**9*math.floor(FBN*(-1)/604800*10**9)
                print(weekNumberNs)
                T_tx = (T_n + T_on) - (FBN + BN) - weekNumberNs
                #pseudorange computation

                pseudorange = c * (T_rx - T_tx)/(10**9)
                print(pseudorange)
                
                print(line)
                sys.exit()

            else:
                continue
        else:
            continue
    
    sys.exit()    
    for line in text_body:
        if line[0]=='Raw':
            ConstellationType = line[25]
            Svid = line [11]
            if ConstellationType == '1':
                line.append('%s%s' %('G',Svid))
            elif ConstellationType == '2':
                line.append('%s%s' %('SBAS',Svid))
            elif ConstellationType == '3':
                line.append('%s%s' %('R',Svid))
            elif ConstellationType == '4':
                line.append('%s%s' %('Q',Svid))
            elif ConstellationType == '5':
                line.append('%s%s' %('C',Svid))
            elif ConstellationType == '6':
                line.append('%s%s' %('E',Svid))
            else:
                line.append('error/unknown')
        else:
            continue
    
    print(str(text_body[0]))

   
    ConstellationType = text_body[7][25]
    print(ConstellationType)
    Svid = text_body[7][11]
    print(Svid)


   
    #preparing the text for the new file
    
    text_header[5].append("SatID")

    text_header5=",".join(str(x) for x in text_header[5])
    print(text_header5)
        
    #observation of sat G11

    obsG11 = []

    for i in text_body:
        print (i)
    sys.exit()   
    '''
        if i[0] == 'Fix':
            continue
        else:
            if i[25] == '1' and i[11] =='11':
                i.append(obsG11)
            else:
                continue
    print (obsG11)

'''
    #writing the new file
    with open(RawDataFileNew, "w") as out_file:
        for line in text_header:
            strin_line=",".join(str(x) for x in line)
            out_file.write(strin_line+'\n')
    
    #with open(RawDataFileNew, "w") as out_file:
        for line in text_body:
            strin_line=",".join(str(x) for x in line)
            out_file.write(strin_line+'\n')
    






if __name__== "__main__":
    main()



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