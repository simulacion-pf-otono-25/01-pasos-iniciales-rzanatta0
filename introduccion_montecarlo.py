import numpy as np
import matplotlib.pyplot as plt


# Limites de integración
a = 0
b = 2

def funcion_a_integrar(x) : 
    return - x ** 2

N = 100000

x = np.random.uniform(a , b, N)
y = np.random.uniform(funcion_a_integrar(a), funcion_a_integrar(b) , N)

print(x, y)

