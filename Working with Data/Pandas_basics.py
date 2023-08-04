import pandas as pd

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