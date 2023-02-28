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

# calculamos priors
def prior(c):
  return len(X[y==c])/len(X)

# tenemos cuatro posibles distribuciones a ajustar (verosimilitud)
def distX0(c):
  if c==0:
    return fit_distribution(X[y==0][:,0])
  elif c==1:
    return fit_distribution(X[y==1][:,0])

def distX1(c):
  if c==0:
    return fit_distribution(X[y==0][:,1])
  elif c==1:
    return fit_distribution(X[y==1][:,1])

# verosimilitud
def likelihood(X, c):
  return distX0(c).pdf(X[0])*distX1(c).pdf(X[1])

# posterior
def probability(c, X):
  return prior(c)*likelihood(X,c)

predictions = [np.argmax([probability(0, vector), probability(1, vector)]) for vector in X]

from sklearn.metrics import confusion_matrix
confusion_matrix(y, predictions)

def class_distribution(x, y):
  return np.argmax([probability(0, [x,y]), probability(1, [x,y])])

class_distribution(-6, 0)

plt.scatter(X[y==1][:,0], X[y==1][:,1], label = '1', color='red', marker = '*')
plt.scatter(X[y==0][:,0], X[y==0][:,1], label = '0', color = 'blue', marker='*')
plt.scatter(-6, 0, color = 'red', marker='s', s=53)
plt.scatter(-4, 0, color = 'blue', marker='s', s=53)
plt.legend()