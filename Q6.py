'''
Created on Jul 27, 2018

@author: Scott Jackson
'''

import json

#Open JSON file
with open('ca.json') as data_file:    
    data = json.load(data_file)

from tkinter import *
from tkinter.ttk import *

#Create window
window = Tk()
window.title("City Information")
window.geometry('450x200')

#Create drop-down box to select City
Label(window, text="City").grid(column=0, row=0, padx=(0,50), pady=10)
cityVar = StringVar()
city = Combobox(window, width=50, textvariable=cityVar)
city['values']= tuple()
for i in range(0, len(data)):
    city['values']+= tuple([data[i]["name"]])
city.current(0)
city.grid(column=1, row=0)

#Create entry to populate County
Label(window, text="County").grid(column=0, row=1, padx=(10,50), pady=10)
countyVar = StringVar()
county = Entry(window, width=53, textvariable=countyVar)
county.grid(column=1, row=1)
countyVar.set(data[city.current()]["full_county_name"])

#Create entry to populate Latitude
Label(window, text="Latitude").grid(column=0, row=2, padx=(10,50), pady=10)
latitudeVar = StringVar()
latitude = Entry(window, width=53, textvariable=latitudeVar)
latitude.grid(column=1, row=2)
latitudeVar.set(data[city.current()]["primary_latitude"])

#Create entry to populate Longitude
Label(window, text="Longitude").grid(column=0, row=3, padx=(10,50), pady=10)
longitudeVar = StringVar()
longitude = Entry(window, width=53, textvariable=longitudeVar)
longitude.grid(column=1, row=3)
longitudeVar.set(data[city.current()]["primary_longitude"])

#Populate county, latitude and longitude from JSON data when city changed
def change_dropdown(*args):
    countyVar.set(data[city.current()]["full_county_name"])
    latitudeVar.set(data[city.current()]["primary_latitude"])
    longitudeVar.set(data[city.current()]["primary_longitude"])

cityVar.trace('w', change_dropdown)
 
window.mainloop()
