import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 501)
ampl = np.exp(-(x - 3.5)**2 / 0.8)
y = np.sin(x * 25) * ampl


#plot the waves using matplotlib
plt.figure(figsize=(10,5))
plt.plot(x, y, label='signal')
plt.plot(x, ampl, ':', label='amplitude')
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.show()