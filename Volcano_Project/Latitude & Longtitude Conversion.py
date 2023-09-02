# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:34:12 2023

@author: Dave
"""
import difflib
import pandas as pd

volcano_df = pd.read_excel("The Volcanoes Of Earth.xlsx")

'''
for x in volcano_df['Latitude']:
    if x == "°S":
        continue
    print(x)
    
difflib.get_close_matches("°S", volcano_df["Latitude"], 10, cutoff= 1)
'''

'''
def fix_latitude(x):
    if x.endswith('°S'):
        x = -float(x.strip('°S'))
    else:
        x = x.strip('°N')
        return x     
    
volcano_df['FixedLatitude'] = volcano_df.Latitude.apply(fix_latitude)
'''

#So get rid of the degree sign and put into a new column
nodegree_df = volcano_df['Latitude'].str.replace("°"," ")

volcano_df['degreefix'] = nodegree_df


#I can use the delimiter to place the direction into a seprate column and use the ' ' as the splitting point
#To optimize I'll use the degree as the split point
volcano_df[['degreefix','direction']] = volcano_df['degreefix'].str.split(' ',expand=True)

volcano_df['direction'] = volcano_df['direction'].str.replace('S','-')
volcano_df['direction'] = volcano_df['direction'].str.replace('N','+')

volcano_df['Latitude Coordinates'] = volcano_df['direction'].astype(str) + volcano_df['degreefix']

volcano_df['Latitude Coordinates'] = volcano_df['Latitude Coordinates'].str.replace('+','')

#print(volcano_df['Latitude Coordinates'])


#next time try volcano_df['Latitude'].str.replace('°S$','-') and bring the '-' to the front and get rid of "°N"


#Nice and Clean; split, replace, and concat
volcano_df[['Longitude','east_west']] = volcano_df['Longitude'].str.split('°',expand=True)

volcano_df['east_west'] = volcano_df['east_west'].str.replace('E','')
volcano_df['east_west'] = volcano_df['east_west'].str.replace('W','-') 

volcano_df['Longitude Coordinates'] = volcano_df['east_west'].astype(str) + volcano_df['Longitude']
#print(volcano_df['Longitude Coordinates'])

volcano_df = volcano_df.drop(columns = ['degreefix','direction','east_west','Latitude','Longitude'])

volcano_df.to_csv('Volcanoes On Earth.csv')
