import pandas as pd
import numpy as np

data = {'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
print(df.rolling(window=3,center=True,min_periods=1).mean())