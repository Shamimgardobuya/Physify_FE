#import data files into numpy arrays 
#to create an array of month names from months.txt which is available for download at 
#get data from source usually in form of url

#no one will step on humanity as long as I believe- Alhamdulillah
#then convert format into array

import os
import numpy as np
import earthpy as myearth
import matplotlib.pyplot as plt

month_names_source = 'https://ndownloader.figshare.com/files/12565616'
# myearth.data.get_data(url=month_names_source)
os.chdir(os.path.join(myearth.io.HOME, 'earth-analytics')) #set directories to earth-analytics

file_name = os.path.join('data','earthpy-downloads','avg-monthly-precip.txt')

#import  monthly names to numpy array
# month_names = np.loadtxt(file_name)
# print(month_names)
#receiving ValueError: could not convert string to float: 'Jan' when getting numpy array of string content array
#working with csv files to get data
precip_2002_2013_url = 'https://ndownloader.figshare.com/files/12707792'
myearth.data.get_data(url=precip_2002_2013_url)
myearth.data.get_data(url=month_names_source)

os.chdir(os.path.join(myearth.io.HOME, 'earth-analytics')) 
file_name_two = os.path.join('data','earthpy-downloads','monthly-precip-2002-2013.csv')
file_name_2 = os.path.join('data','earthpy-downloads','months.txt')


month_precip = np.loadtxt(file_name_two,delimiter=',')
month_avg = np.loadtxt(file_name)
# month_names = np.loadtxt(file_name_2)

# month_names = np.loadtxt(file_name_2)

'''Create a new numpy array for the average monthly precipitation 
in 2013 by selecting all data values in the last row in 
precip_2002_2013 (i.e. data for the year 2013).'''
#acess asubarray of 2013
year_thirteen = month_precip[0:,-1:]#😄 
# print(np.average(year_thirteen))
'''Convert the values in the numpy array 
from inches to millimeters (1 inch = 25.4 millimeters).'''

#get all values of the 2d array to milimetres,
#loop through all the values of the array
#identify current unit - inches
#have a conversion range - 1 inch = 25.4 
#looping through the precipitation data
#convert each value to the precipitated data
#return new array

def converting_measurments(month_precip):
    new_measurment = month_precip
    for i in new_measurment:
        
        # for i in new_measurment: will loop twice
        #     i * 25.4
        return i*25.4
print(converting_measurments(month_precip))
#plot with Matpolib
#Use the converted numpy array
#  for 2013 and the numpy array 
# of month names to create plot of Average
#  Monthly Precipitation in 2013 for Boulder, CO.
fig,ax = plt.subplots(figsize = (9,6))
# ax.bar(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
#           "Aug", "Sept", "Oct", "Nov", "Dec"]
# ,
#        month_avg,
#        color='blue'
#        )
ax.plot(["Jan", "Feb", "Mar", "Apr", "May", "June", "July",  #x - axis
          "Aug", "Sept", "Oct", "Nov", "Dec"],
       month_avg,       #y - axis
       color='blue',
    #    edgecolors='lightblue',
    #    cmap='cyan',
       alpha=0.4,  #transparency of the color
       )
ax.set(
    title = 'Monthly Average Precipitation \n in Kenya',
    xlabel = 'months',
    ylabel = 'average per month\n(inches)'
)

plt.show()

# TypeError: 'ArtistList' object is not callable

