# -*- coding: utf-8 -*-

import pymongo
import datetime
import sqlite3

uri = 'mongodb+srv://m001-student:Polofish@sandbox.e2bj5.mongodb.net/db.bikedata?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
db = client["stationdb"]
bikedata = db.bikedata


conn = sqlite3.connect('index.sqlite')
conn.text_factory = str
cur = conn.cursor()
cur.executescript('''DROP TABLE IF EXISTS bike_stations''')

cur.executescript('''CREATE TABLE IF NOT EXISTS bike_stations (id INTEGER, 
    station_name Text, timestamp INTEGER, total_docks INTEGER, 
    available_bikes INTEGER, status TEXT, percent_full INTEGER)''')

count = 0

for bike in bikedata.find():
    try:
        stationNum = bike['id']
        stationName = str(bike['station_name'])
        totalDocks = int(bike['total_docks'])
        availableBikes = int(bike['available_bikes'])
        status = str(bike['status'])
        percent_full = int(bike['percent_full'])
      
        isodate = bike["timestamp"]
        dt = datetime.datetime.fromisoformat(isodate)
        timestamp = datetime.datetime.timestamp(dt)
    
        cur.execute('''INSERT INTO bike_stations (id, station_name, timestamp, total_docks, available_bikes, status, percent_full) 
                     VALUES (?,?,?,?,?,?,?)''', (stationNum, stationName, timestamp, totalDocks, availableBikes, status, percent_full))
                    
        if count%100==0 : 
            print(count, 'station no: ', bike['id'])
        count += 1
    except ValueError:
        print("Error Detected!")
        break
        
print(count, "produced")
conn.commit()