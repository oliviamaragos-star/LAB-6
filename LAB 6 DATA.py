# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 16:21:56 2025

@author: Olivia Maragos and Victoria Milioto 
"""

import pandas as pd
import seaborn as sns
print(sns.__version__)

data = pd.read_csv("wdi_wide.csv")
print("Missing values in Physicians:", data["Physicians"].isnull().sum())
print("Missing values in Population:", data["Population"].isnull().sum())







