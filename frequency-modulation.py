import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10*np.pi, 100)

y = 0.2*np.sin(x)

c = np.array([-0.2 if i%2==0 else 0.2 for i in range(100)])

d = c*y

plt.plot(x, y, label = "carrier signal")
plt.plot(x, c, label = "msg signal")
plt.plot(x, d, ":", label = "modulated signal", color = 'green')
plt.legend()
plt.show()

