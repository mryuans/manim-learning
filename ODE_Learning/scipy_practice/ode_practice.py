import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(state, t):
    x, y, z = state
    dydt = y + x
    dxdt = z + y
    dzdt = z + x
    return [dydt, dxdt, dzdt]

y0 = (1, 0, 1)
t = np.arange(0, 10, 2)
y = odeint(model, y0, t)

print(*zip(t, y), sep="\n")

