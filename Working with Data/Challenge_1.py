import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 
# Load data from github url 
base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/" # loading from Internet

infected_dataset_url = base_url + "time_series_covid19_confirmed_global.csv"
recovered_dataset_url = base_url + "time_series_covid19_recovered_global.csv"
deaths_dataset_url = base_url + "time_series_covid19_deaths_global.csv"

infected = pd.read_csv(infected_dataset_url)
print(infected.head())
recovered = pd.read_csv(recovered_dataset_url)
deaths = pd.read_csv(deaths_dataset_url)

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
recovered = recovered.groupby("Country/Region").sum()
deaths = deaths.groupby("Country/Region").sum()

print(infected)

# access Data for a specific country in the dataframe

infected.loc["Albania"][2:].plot()
plt.show()

# dropping columns from a dataframe 
# this can remove rows permanently using the inplace parameter
print("----------------After dropping rows-----------------")

infected.drop(columns=["Province/State","Lat", "Long"], inplace=True) 
print(infected, "infected")
print(infected.loc["Albania"])
recovered.drop(columns=["Province/State","Lat", "Long"], inplace=True)
print(recovered, "recorvered")
deaths.drop(columns=["Province/State","Lat", "Long"], inplace=True)

print(deaths, "deaths")
# Investigating data 

def mkframe(country):
    df = pd.DataFrame({"infected": infected.loc[country],
                       "recovered": recovered.loc[country],
                       "deaths": deaths.loc[country]
                    
                      })
    print("-------my df BEFORE COVERTING------")
    print(df)

    
    df.index = pd.to_datetime(df.index)
    return df


df = mkframe("Zimbabwe")
df
df.plot()
plt.show()

#  computing the number of new infected cases each day 
# diff() calculates the differences between consecutive values 

df["ninfected"] = df["infected"].diff()
print(df)
df["ninfected"].plot()

plt.show()

#  we can look closer at one month of the results 

df[(df.index.year==2022)&(df.index.month==8)]["ninfected"].plot()
plt.show()