# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 14:22:09 2023

@author: fedig
"""
'''
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


#members = pd.read_excel("excelFileName.xlsx")
members = pd.read_excel("Volunteer List by OU .xlsx")

all_positions = ["Chair", "Counselor", "Secretary", "Treasurer", "Vice Chair", "Webmaster"]

grouped = members.groupby("OU Name")["Position"].agg(list).reset_index()

def find_missing_positions(positions):
    return [pos for pos in all_positions if pos not in positions]

grouped["Missing Positions"] = grouped["Position"].apply(find_missing_positions)


grouped.to_excel("SBs Missing Volunteers.xlsx")
'''
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Read the Excel file
members = pd.read_excel("Volunteer List by OU.xlsx")

all_positions = ["Chair", "Advisor", "Secretary", "Treasurer", "Vice Chair", "Webmaster"]

# Group by OU Name and aggregate email addresses into a comma-separated string
grouped = members.groupby("OU Name").agg({
    "Position": list,
    "Email Address  ": lambda x: ','.join(x) if not x.empty else ''
}).reset_index()

# Define a function to find missing positions
def find_missing_positions(positions):
    return [pos for pos in all_positions if pos not in positions]

# Apply the function to create a new column for missing positions
grouped["Missing Positions"] = grouped["Position"].apply(find_missing_positions)

# Save the result to an Excel file
grouped.to_excel("SBCs Missing Volunteers.xlsx", index=False)


