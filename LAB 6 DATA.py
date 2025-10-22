# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 16:21:56 2025

@author: Olivia Maragos and Victoria Milioto 
"""

import pandas as pd
import seaborn as sns
print(sns.__version__)
data = pd.read_csv("wdi_wide.csv")

#Answer the question: how many empty values for the column “Physicians” and “Population”?
print("Missing values in Physicians:", data["Physicians"].isnull().sum())
print("Missing values in Population:", data["Population"].isnull().sum())

#nunique counts how many different entries exist per column.
print(data.nunique())
#Get descriptive statistics for all numeric columns
print(data.describe())
# Add a new column for GNI per capita
data["GNI per capita"] = data["GNI"] / data["Population"]
data["GNI per capita"] = data["GNI per capita"].round(2)
# Count how many countries are in each region
print(data["Region"].value_counts())






