## 1. Introduction
do the homework all by myself
including 3 deliverables:

        show_bus_locations_yl5240.py
        
        get_bus_info_yl5240.py
        
        HW2_assignment3_yl5240.ipynb

## 2. Assignment 1 and 2
The deliverables of assignment1 and assignment are python files as .py and could
be run by the commands below respectively:

        python show_bus_locations_yl5240.py <MTA_KEY> <BUS_LINE>

        python get_bus_info_yl5240.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv

<MTA_KEY>: is a MTA Bus Time API Key. It could request got from http://bustime.mta.info/wiki/Developers/Index

<BUS_LINE>: should be a string of the actual MTA Bus Line. If not, the output will be "'There is no Bus line : ' str(BUS_LINE)"

<BUS_LINE>.csv: the name should be exactly same with <BUS_LINE> in the same command. If not, the output will be "Please name the csv file according to the bus line data loaded."

**In the assignment 2, I use the "MonitoredCall" instead of "OnwardCall", which I think make more sense. Because "MonitoredCall" is the next stop information of each bus on roads, and "OnwardCall" includes the next stops' information, from the next stop to the last stop, for each bus on roads. That's why there is "OnwardCall" under "OnwardCalls".**

## 3. assignment 3
This Jupyter notebook is writen on NYU CUSP compute via the below SSH tunnel command 

        ssh yl5240@gw.cusp.nyu.edu -L 8000:compute.cusp.nyu.edu:8000
        
and the [address](https://localhost:8000)

Instructions could be got from [here](https://datahub.cusp.nyu.edu/sites/default/files/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf)

Since the [CUSP data facility](https://datahub.cusp.nyu.edu/data-catalog) (DF) is currently unavailable, I fetch csv files in the data facility NYCopendata directory by running in notebook (on JupyterHub) the command:

        !ls $DFDATA/*/*csv
        
the environmental variable DFDATA points to 

        /gws/open/NYCOpenData/nycopendata/data/
        
9 csv  datasets could be fetched and I choose the 4th dataset, which includes two numerial columns.



