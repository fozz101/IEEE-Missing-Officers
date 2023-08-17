# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 14:22:09 2023

@author: fedig
"""

import time
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


#members = pd.read_excel("excelFileName.xlsx")
members = pd.read_excel("VolunteerListUpdatedStatus1.xlsx")

all_positions = ["Chair", "Counselor", "Secretary", "Treasurer", "Vice Chair", "Webmaster"]

grouped = members.groupby("OU Name")["Position"].agg(list).reset_index()

def find_missing_positions(positions):
    return [pos for pos in all_positions if pos not in positions]

grouped["Missing Positions"] = grouped["Position"].apply(find_missing_positions)


grouped.to_excel("Missing Volunteers.xlsx")