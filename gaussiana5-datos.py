import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy.random import binomial

def generate_binomial_trials(trials=1000, coin_toss=100):
  '''
  el resultado de esta funcion es generar un conjuntos 
  de experimentos binomiales (trials) y de cada uno obtener 
  las cantidades de exitos en cada secuencia (e.j. lanzar monedas).

  * trial: es una secuencia de <coin_toss> lanzamientos de moneda

  * coin_toss: es el numero de monedas lanzadas en cada trial
  '''
  arr = []
  for _ in range(trials):
    arr.append(binomial(coin_toss, 0.5))
  values, dist = np.unique(arr, return_counts=True)

  return values, dist, np.array(arr)

values, dist, arr = generate_binomial_trials(100000)
plt.bar(values, dist)z

mu = arr.mean()
sigma = arr.std()
normal = norm(mu, sigma)

X = np.arange(30,70,0.1)
Y = [normal.pdf(x) for x in X]

plt.plot(X, Y)
plt.bar(values, dist/len(arr))