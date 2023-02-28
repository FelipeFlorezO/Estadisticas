import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

# usando scipy
dist = norm(0, 1)
x = np.arange(-4,4,0.1)
y = [dist.pdf(value) for value in x]
plt.plot(x, y)