#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Nov 10 2018
@author: pleunipennings

Making a plot of the number of women in the US Congress (House and Senate). 
That jump in 2019 feels good! Makes me optimistic for the future. 
Data from https://en.wikipedia.org/wiki/Women_in_the_United_States_House_of_Representatives#Number_of_women_in_the_United_States_House_of_Representatives_and_Senate_by_Congress

If anyone has similar data for the number of people of color in congress, I would like to plot that too!

"""

import matplotlib.pyplot as plt
import csv

      
def get_data():
    list_years = [] #create an empty list to store years
    list_num =[] #create an empty list to store the number of women
    linenum=0 #create a variable to count the lines, 
    #just so that I can skip the data from the first line
    file =  open("WomenCongress.csv")  #open the file with the data
        #file structure: 
        #Congress,Years,in Congress,Percentage
        #65th,1917–1919,1,0.20%
        #66th,1919–1921,0,0%
        #67th,1921–1923,4,0.70%
        #68th,1923–1925,1,0.20%        
    for line in file: #for each line
        data = line.split(",") #split the line at the commas (bc it is a csv file) 
        year = data[1][0:4] #take the first 4 characters from the second column as the year
        if linenum>0:  #do this, but not for the very first line
            list_years.append(int(year)) #append the year to the list of years
            list_num.append(int(data[2])) #append the number of women to the list for that
        linenum+=1 #update the counter for the number of lines
    file.close()
    return list_years,list_num # return the list for the years and the list for the number of women
    
list_years,list_num=get_data() #use the get_data function to get the list of years and the list of the number of women in congress

print(list_years[0]) #print statement to make sure it worked 

fig = plt.figure()
plt.plot(list_years, list_num, 'o') #plot year vs the number of women
plt.plot(list_years[-1], list_num[-1], 'ro')  #Highlight the last year (2019) in red
plt.suptitle('Number of Women in the US Congress', fontsize=16) #add a title
#plt.show() # show the plot

fig.savefig('plot.png')
