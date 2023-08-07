import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series
# Series is like a list or 1D-array, but with index. All operations are index-aligned.

# automatic numeric index labels
a = pd.Series(range(5,10))
print(a)

# custom index labels 
b = pd.Series(["I", "like", "python", "libraries"], index=["a","b","c","d"])
c = pd.Series(["I", "love","Django", "Most"], index=range(4,8))
print("------B-----")
print(b)
print("------C-----")
print(c)


# timeseries
#  In time series, index has a special structure - typically a range of dates or datetimes
# Example to create time serie data 

start_date = "Jan 1, 2023"
end_date = "May 27, 2023"
# getting the range of dates
index = pd.date_range(start_date, end_date)

print(index)

# Creating sample data of a series 
print("Threads Sample Data Created")
threads_sold = pd.Series(np.random.randint(25,50, size=len(index)), index=index)
print(threads_sold)

threads_sold.plot(figsize=(10,3))
plt.xlabel("Year 2023")
plt.ylabel("Threads Sold")
plt.show()

# suppose 10 threads are picked every week by a known customer 
# by default the date_range function we set the weekly frequency on sundays  
additional_threads = pd.Series(10, index=pd.date_range(start_date, end_date,freq="W"))
print(additional_threads)

# Addition of series 
# we specify a fill_value when ever we are addig series  for cases where we have 
# missing values for some index points i.e our additional_threads in this case
total_threads =  threads_sold.add(additional_threads, fill_value=0)

total_threads.plot()
plt.show()