import numpy as np

import matplotlib.pyplot as plt
#ice cream sale
x = [50, 65,70,85,100]
y = [3,18,54, 75,98]

plt.scatter(x, y)
plt.show()
plt.savefig("mygraph.png")

#argument(args) and parameters(params)
def salamtoAll(name):
    print("Aoa, everyone from ",name)
    return name
    
    
def myfunction():
    pass


from scipy import stats

slope, intercept, r, p, std_err = stats.linregress(x, y)

def predictY(x):
  return slope * x + intercept



mymodel = list(map(predictY, x))

plt.scatter(x, mymodel)

plt.show()

predition=predictY(30)
