
# coding: utf-8

# In[ ]:

import urllib.request as urllib
import json
import sys

url1 = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='
url3 = '&VehicleMonitoringDetailLevel=calls&LineRef='
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
url = url1 + str(MTA_KEY) + url3 + str(BUS_LINE)


try:
    response = urllib.urlopen(url)
    data = response.read().decode('utf-8')
    bus_data = json.loads(data)
    number = len(bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    print('Bus line : ' + str(BUS_LINE))
    print('Number of Active Buses : ' + str(number))
    for i in range(number):
        location = bus_data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']
        print('Bus ' + str(i) + ' is at latitude ' + str(location['Latitude']) +  ' and longitude ' + str(location['Longitude']))   
except:
    print('There is no Bus line : ' + str(BUS_LINE))

