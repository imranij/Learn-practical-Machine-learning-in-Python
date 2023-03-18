import numpy as np
import pandas as pd
array1=[2,3,5,10]
meanX=np.mean(array1)

wind=ds['wind']
mean_Wind=np.mean(wind)
print("mean value of wind is=",mean_Wind)


median_Wind=np.median(wind)
print("median value of wind is=",median_Wind)

from scipy import stats


mode_Wind=stats.mode(wind)
print("median value of wind is=",median_Wind)


std_Wind=np.std(wind)
print("standard deviation value of wind is=",std_Wind)


var_Wind=np.var(wind)
print("variance value of wind is=",var_Wind)

score=[5,22,33,44,82,33,2,88,66,23]
score_percentile=np.percentile(score,90)

import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 1090, 1000)
x_df=pd.DataFrame(x)

plt.hist(x, 5)
plt.show()
