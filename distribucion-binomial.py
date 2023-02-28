from math import factorial

# definición de la distribución binomial 
def my_binomial(k, n, p):
  return factorial(n)/(factorial(k)*(factorial(n-k)))*pow(p,k)*pow(1-p, n-k)

def c_binomial(k, n, p):
  total = 0
  for i in range(k+1):
    total += my_binomial(i,n,p)
  return total
print(c_binomial(5,10,0.3)) 