#Pandas version check

#import pandas
#pandas.__version__


import numpy as np
import pandas as pd

#series
#panda series contains both sequence of indices and sequence of values
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

#values
data.values

#index
data.index
#however use it like 
data[1]