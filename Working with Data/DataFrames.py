import pandas as pd
# A DataFrame is essentially a collection of series with the same index


a = pd.Series(range(1,7))
b = pd.Series(["I", "WORK", "WITH", "DJANGO", "AND", "RAECT"], index=range(0,6))

df = pd.DataFrame(a)
print(df)

df = pd.DataFrame(b)
print(df)

# We can combine several series together into a DataFrame
combined_df = pd.DataFrame([a,b])
print(combined_df)


print("--------------columns-----------------")
# having the series as columns and specifying column names
# we use a dictionary for this 
df = pd.DataFrame({"A": a, "B":b})

print(df)

# we can as well traspose a dataframe to flip rows to column and vise versa.
print("--------------traspose-----------------")

df = combined_df.T
print(df)


print("--------------Rename Columns-----------------")

df = df.rename(columns={0:"Numbers", 1:"Word"})
print(df)

# Operations performed on Dataframes 

print("--------------column selection -----------------")
# we can select individual columns from a dataframe 

print(df["Numbers"]) # this will return a series 

# selecting a subset
print(df[["Word", "Numbers"]])

print("-----------------filtering------------------------")

print(df[df["Numbers"]>3])

# filtering more than one column 
print(df[(df["Numbers"]>3) & (df["Word"].str.contains("N"))])

print("-----------------new computable columns------------------------")
# Creating new computable columns 
# here we add new column DivNumber to our dataframe after calculating divergence
df["DivNumbers"] = df["Numbers"]-df["Numbers"].mean()

print(df)

# what is done above only works for operations compatible with Series 

# for complex expressions like string operations, numpy functions, custom functions 
#  we use the apply function perform those operation 

df["Lower"] = df["Word"].apply(lambda x: x.lower())
print(df)


