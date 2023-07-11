# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 13:13:21 2021

@author: Zack
"""
import sys
class BikeStation : 
    def __init__(self, stationNum, stationName, timeStamp, totalDocks, availableBikes, status):
        self.stationNum = stationNum
        self.stationName = stationName
        self.timeStamp = timeStamp
        self.totalDocks = totalDocks
        self.availableBikes = availableBikes
        self.status = status
       
   
    @property
    def stationName(self):
        return self.__stationName
    @stationName.setter
    def stationName(self,x):
        if not isinstance(x,str):
           x = str(x)
        self.__stationName = x[0:30]
        
    
    def display_usedbikes(self,availableBikes,totalDocks):
        percentfull = int(self.availableBikes) / int(self.totalDocks)
        print(percentfull)
        
    def __str__(self):
        return '{} had {} bikes on {}'.format(self.stationName,self.availableBikes,self.timeStamp)

def main():   
    fname = input("Enter a file name: ")
    try:
        file = open(fname)
        read_data = file.readlines()
    except:
        print("There is no existing file name under", fname)
        sys.exit()

#changed code to be more efficient rather than hardcoding
#line 51-56 were adapted 

    mystations = ["31", "46", "176", "182", "620"]
    data = [] #for the data
    for line in read_data:
        if line.startswith('[{"id": ') or ('["id": '):
            line = line.strip().split(sep=',')
            stationNum = line[0].replace('"', '').replace(' ','').split(sep=":")
            stationName = line[1].replace('"', '').strip().split(sep=":")
            timeStamp = line[2].replace('"', '').split(sep=":")
            availableBikes = line[6].replace('"', '').replace(' ','').split(sep=":")
            totalDocks = line[3].replace('"', '').replace(' ','').split(sep=":")
            status = line[8].replace('"', '').replace(' ','').split(sep=":")
            for station in mystations:
                if station in stationNum[1] and len(station) == len(stationNum[1]):
                    data.extend((stationNum[1],timeStamp[1],stationName[1].strip(), totalDocks[1], availableBikes[1], status[1].strip))
                    
#creating objects    
    bikestation31 = BikeStation(data[0], data[1], data[2], data[3], data[4], data[5])
    bikestation46 = BikeStation(data[6], data[7], data[8], data[9], data[10], data[11])       
    bikestation176 = BikeStation(data[12], data[13], data[14], data[15], data[16], data[17])
    bikestation182 = BikeStation(data[18], data[19], data[20], data[21], data[22], data[23])
    bikestation620 = BikeStation(data[24] ,data[25], data[26], data[27], data[28], data[29])
 #list of stations with data   
    new_stations = [bikestation31, bikestation46, bikestation176, bikestation182, bikestation620]
 #endingtoatals
    Total_BikesAvail = int(data[4]) + int(data[10]) + int(data[16]) + int(data[22]) + int(data[28])
    Total_Docks = int(data[3]) + int(data[9]) + int(data[15]) + int(data[21]) + int(data[27])
   
    for station in new_stations:
        str(station)
        print(station)
    print("Stations: ", mystations, "Bikes Available ", Total_BikesAvail, "Docks Available ", Total_Docks)
if __name__ == "__main__":
    main()