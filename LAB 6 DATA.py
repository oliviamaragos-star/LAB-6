# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 16:21:56 2025

@author: Olivia Maragos and Victoria Milioto 
"""

import pandas as pd
import seaborn as sns
print(sns.__version__)
data = pd.read_csv("wdi_wide.csv")

# ----------------------------------------------------------
#Part 3 – Understanding and preparing the data
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
# a) Count how many countries are in each region
print(data["Region"].value_counts())
# b) How many high income economies are there?
print(data["High Income Economy"].value_counts())
# Where are the high income economies (per region)?
table = pd.crosstab(data["Region"], data["High Income Economy"])
print(table)
# Create empty lists
countries_over_80 = []

# Loop through the dataset row by row
for i in range(len(data)):
    if data["Life expectancy, female"][i] > 80:
        countries_over_80.append(data["Country Name"][i])
print("Number of countries where women live more than 80 years:", len(countries_over_80))
print("Countries:", countries_over_80)

# ----------------------------------------------------------
#Part 4 - Visualizing statistical relationships
import matplotlib.pyplot as plt

# Scatter plot for females
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, female")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()
# Scatter plot for males
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, male")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()
# ----------------------------------------------------------
#Step 1: relplot() with color by Region
# Female life expectancy by region
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",             # color-coded by region
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, female by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()
# Male life expancy by region 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    kind="scatter",
    height=5,
    aspect=1.3)
plt.title("GNI per Capita vs Life expectancy, male by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()
#Step 2: relplot() with Lines and Standard Deviation
#For women
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
    kind="line",
    ci="sd",        # show standard deviation as shaded area
    height=5,
    aspect=1.3
)
plt.title("GNI per Capita vs Life expectancy, female by Region — Line + SD")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()
#For men 
sns.relplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    kind="line",
    ci="sd",
    height=5,
    aspect=1.3
)
plt.title("GNI per Capita vs Life expectancy, male by Region — Line + SD")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()
#lmplot() — Linear Regression per Region
#for women 
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, female",
    hue="Region",
    height=5,
    aspect=1.3,
    scatter_kws={"alpha":0.6}
)
plt.title("Linear Regression: GNI per Capita vs Life expectancy, femaleby Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Female, years)")
plt.grid(True)
plt.show()
#for men
sns.lmplot(
    data=data,
    x="GNI per capita",
    y="Life expectancy, male",
    hue="Region",
    height=5,
    aspect=1.3,
    scatter_kws={"alpha":0.6}
)
plt.title("Linear Regression: GNI per Capita vs Life expectancy, male by Region")
plt.xlabel("GNI per Capita (USD)")
plt.ylabel("Life Expectancy (Male, years)")
plt.grid(True)
plt.show()

#Part 5 ----------------------------------------------------
data_melted = pd.melt(
    data, 
    id_vars=["Country Name", "Region", "GNI per capita", "Health expenditure" ,
             "Physicisans" , "CO2 emissions (metric tons per capita)",
             "Internet use","Population"],
    value_vars=["life expectancy, female", "Life expectancy, male"],
    var_name="Gender", 
    value_name="Life Expectancy")
# Simplify gender labels 
data_melted["Gender"] = data_melted["Gender"].str.replace("Life expectancy,","")

#Question 1
#Is life expectancy related to health expenditure?
sns.relplot(
    data=data_melted,
    x="Health expenditure",
    y="Life Expectancy",
    col="Gender",
    kind="scatter",
    height=5,
    aspect=1
)
plt.suptitle("Life Expectancy vs Health Expenditure by Gender", y=1.05)
plt.show()

#Question 2 
# Is life expenctancy related to the number of physicians? 
sns.relplot(
    data=data_melted,
    x="Physicians",
    y="Life Expectancy",
    col="Gender",
    kind="scatter",
    height=5,
    aspect=1)

plt.suptitle("Life Expectancy vs Number of Physicians by Gender", y=1.05)
plt.show()

#Question 3
#Does Interpret use influence life expenctancy?
sns.relplot(
    data=data_melted,
    x="Interpret use",
    y="Life Expectancy",
    col="Gender",
    kind="scatter",
    height=5,
    aspect=1
)
plt.suptitle("Life Expectancy vs Internet USe by Gender", y=1.05)
plt.show()

#Question 4 
#Does CO2 emissions affect life expectancy?
sns.relplot(
    data=data_melted,
    x="CO2 emissions (metric tons per capita)",
    y="Life Expectancy",
    col="Gender",
    kind="scatter",
    height=5,
    aspect=1)

plt.suptitle("Life Expectancy vs CO2 Emissions by Gender", y=1.05)
plt.show()

#Question 5
#Is population size related to life expectancy?
sns.relplot(
    data=data_melted,
    x="Population",
    y="Life Expectancy",
    col="Gender",
    kind="scatter",
    height=5,
    aspect=1)

plt.suptitle("Life Expectancy vs Population by Gender", y=1.05)
plt.show()


#Part 6 -----------------------------------------
#a) Is there any association between internet use and emissionsper capita ?
sns.lmplot(
    data=data,
    x="Internet Use",
    y="CO2 emissions (metric tons per capita)",
    hue="Region",
    height=5,
    aspect=1.3,
    scatter_kws={"alpha":0.6})

plt.title("Association between Internet Use and CO2 Emissions per Capita")
plt.xlabel("Internet Use (% of population)")
plt.ylabel("CO2 Emissions (metric tons per capita)")
plt.grid(True)
plt.show()

#b) Which are the countries with higher emissions (> 0.03)?
high_emissions = data[data["Co2 emissions (metric tons per capita)"] > 0.03]
print (high_emissions[["Country Name", "Region","CO2 emissions (metric tons per capita)"]])
print (high_emissions [["Country Name", "Region","CO2 emission (metric tons per capita)"]])

#c) Is there much variation by region (high emissions vs Internet Use)?
sns.relplot (data=data,
             x="Internet use",
             y="CO2 emissions (metric tons per capita)",
             hue="Region",
             kind="scatter",
             height=5,
             aspect=1.3)

plt.title("Internet USe vs CO2 Emissions by Region")
plt.xlabel("Internet USe (% of population)")
plt.ylabel("CO2 Emissions (metric tons per capita)")
plt.grid(True)
plt.show()

sns.boxplot(
    data=data,
    x="Region",
    y="CO2 emissions (metric tons per capita)")
plt.title("Variation of CO2 Emissions by Region")
plt.xticks(rotation=45)
plt.show()




























