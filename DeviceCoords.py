#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys

file = sys.argv[1]
sensors = pd.read_csv(file)

sensors[['latlong','longitude']] = sensors['latlong'].str.split(',',expand=True)   #splits column into 2 via delimiter

sensors = sensors.drop('projectid',1)

sensors.columns = ['id','deviceuid', 'latitude', 'longitude']

sensors['latitude'] = sensors['latitude'].str[1:]                              #splits entire column of strings
sensors['longitude'] = sensors['longitude'].str[:-1]

sensors = sensors.sort_values(by='id',ascending=True)                             #sorts sensors in ascending order

print(sensors)

sensors.to_csv(file, index=False)                                               #Overwrites csv enterted in command


