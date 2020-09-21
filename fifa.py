# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 20:54:24 2020

@author: suman
"""

import pandas as pd

# Importing the dataset which has player image url and joining with the players dataset
left = pd.read_excel("Fifa_left.xlsx")
right = pd.read_excel("Player final.xlsx")
right.columns
right = right.loc[:, ['short_name','ATT', 'MID', 'DEF', 'GK',"overall",'joined','nationality',"age"]]

final = pd.merge(left=left, right=right, left_on= ['Overall','Joined','Country',"Age"],right_on=["overall","joined","nationality","age"])
final.sort_values("GK",ascending=False,inplace=True)

final.columns

final.drop(['DEF_x',"Hits",'overall', 'joined', 'nationality', 'age'] ,axis=1, inplace=True)
final.drop(['short_name'] ,axis=1, inplace=True)
final.rename(columns={"DEF_y":"DEF"},inplace=True)
final.to_csv("Final_Fifa.csv")
final= pd.read_excel("Final_Fifa.xlsx")
dummy = pd.DataFrame(final['Club'].unique())

# Mapping the club names to the league and country
club = pd.read_excel("Club_Country.xlsx")
final = pd.merge(how="left", left=final, right=club,left_on="Club",right_on="Club")
final.rename(columns={"Country_y": "Club Country"},inplace=True)
final.rename(columns={"Country_x":"Country"},inplace=True)

final.drop(final.columns[0],axis=1 ,inplace=True)
final.to_excel("Final_Fifa.xlsx")
