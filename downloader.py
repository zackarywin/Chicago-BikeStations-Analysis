# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:49:26 2021

@author: Zackch
"""

#31, 46, 176, 182, 620
import json
import urllib.request, urllib.parse, urllib.error
import pymongo


bikeURL = 'https://data.cityofchicago.org/resource/eq45-8inv.json?'
paramD = dict()
paramD['$limit'] = 1000

    
#mongo db

uri = 'mongodb+srv://m001-student:Polofish@sandbox.e2bj5.mongodb.net/db.bikedata?retryWrites=true&w=majority'
client = pymongo.MongoClient(uri)
dblist = client.list_database_names()

db = client["stationdb"]
bikedata = db.bikedata

Stations = ['31', '46', '176', '182', '620']

if 'stationdb' not in dblist:
    for i in Stations:
        paramD['id'] = i
        params = urllib.parse.urlencode(paramD)
        document = urllib.request.urlopen(bikeURL + params)
        text = document.read().decode()
        print('Downloaded', paramD['$limit'], 'for station ', i, ':', bikeURL+params)
        
        js = json.loads(text)
        new_bike = bikedata.insert_many(js)
else:
    print('Database already exists.')