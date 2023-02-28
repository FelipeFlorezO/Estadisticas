from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

X, y = make_blobs(n_samples=10000, centers=2, n_features=2, random_state=1)

# esta función ajusta una gausiana 
# a un conjunto 'data' 
def fit_distribution(data): 
  mu = data.mean()
  sigma = data.std() 
  dist = norm(mu, sigma)
  return dist

plt.scatter(X[y==1][:,0], X[y==1][:,1], label = '1', color='red')
plt.scatter(X[y==0][:,0], X[y==0][:,1], label = '0', color = 'blue')
plt.legend()