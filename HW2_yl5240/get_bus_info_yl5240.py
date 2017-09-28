
# coding: utf-8

# In[ ]:

import urllib.request as urllib
import json
import pandas as pd
import sys
import csv

url1 = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='
url3 = '&VehicleMonitoringDetailLevel=calls&LineRef='
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
BUS_LINE_csv = sys.argv[3]
url = url1 + str(MTA_KEY) + url3 + str(BUS_LINE)

if str(BUS_LINE_csv).split('.')[0] != str(BUS_LINE):
    print("Please name the csv file according to the bus line data loaded.")
else:
    try:
        response = urllib.urlopen(url)
        data = response.read().decode('utf-8')
        bus_data = json.loads(data)
        number = len(bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
        # creat a dictionary with the keys, which are our targeted variables, and blank values
        NEXT_STOP = {'Latitude':[], 'Longitude':[], 'Stop Name':[], 'Stop Status':[]}
        for i in range(number):
            # i means each bus of the input bus line
            VehicleActivity = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
            MornitoredVehicleJourney = VehicleActivity[i]['MonitoredVehicleJourney']
            
            # get the location 
            location = MornitoredVehicleJourney['VehicleLocation']  
            Latitude = location['Latitude']
            Longitude = location['Longitude']
            
            # get the Stop Name and Stop Status via MonitoredCall
            if "MonitoredCall" not in MornitoredVehicleJourney:
                Stop_Name = 'N/A'
                Stop_Status = 'N/A'
            else:
                MonitoredCall = MornitoredVehicleJourney["MonitoredCall"]
                Stop_Name = MonitoredCall['StopPointName']
                Stop_Status = MonitoredCall['Extensions']['Distances']['PresentableDistance']
        
            # fill the dictionary with the next_stop_information bus by bus
            NEXT_STOP['Latitude'].append(Latitude)
            NEXT_STOP['Longitude'].append(Longitude)
            NEXT_STOP['Stop Name'].append(Stop_Name)
            NEXT_STOP['Stop Status'].append(Stop_Status)
        NEXT_STOP = pd.DataFrame(NEXT_STOP)
        #print(NEXT_STOP)

        NEXT_STOP.to_csv(str(BUS_LINE_csv), sep=',', index = False)
        
        with open(str(BUS_LINE_csv), newline = '') as csvfile:
            new = csv.reader(csvfile)
            for row in new:
                print(",".join(row))
    except:
        print('There is no Bus line : ' + str(BUS_LINE))

