import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
# Load data from github url 
base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/" # loading from Internet

infected_dataset_url = base_url + "time_series_covid19_confirmed_global.csv"

infected = pd.read_csv(infected_dataset_url)
print(infected.head())

print(infected["Province/State"].value_counts())

print(infected[["Province/State", "Country/Region"]])

# Making sense of Data
# we can note the Province/State column has NAN on some rows 
china = infected[infected["Country/Region"]=="China"]
print(china)

print("Grouped by")
#  Pre-processing data 
# our dataframe will be indexed by country/region column after groupby is applied. 
infected = infected.groupby("Country/Region").sum()
print(infected)

# access Data for a specific country in the dataframe

infected.loc["Albania"][2:].plot()
plt.show()
