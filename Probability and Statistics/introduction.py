import numpy as np
import pandas as pd
import random 
import matplotlib.pyplot as plt


random_sample = [random.randint(0,10) for _ in range(30)]

mean = np.mean(random_sample)
variance = np.var(random_sample)


print(f"Our random sample{random_sample}")
print(f"Mean is {mean}")
print(f"Variance is {variance}")