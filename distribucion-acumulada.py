import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

# calculando la distribución acumulada
dist = norm(0, 1)
x = np.arange(-4,4,0.1)
y = [dist.cdf(value) for value in x]
plt.plot(x, y)