import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-np.pi, np.pi, 100) #generate time for x axis
fm = 10 #frequency of msg signal
fc = 30 #frequency of carrier signal
Am = 1 #Amplitude of msg signal
Ac = 2 #Amplitude of carrier signal

#message signal
def m(t, Am, fm):
    return Am*np.sin(2*(np.pi)*fm*t)

#carrier signal
def c(t, Ac, fc):
    return Ac*np.cos(2*(np.pi)*fc*t) 

#modulation function
def mod(t, Ac, Am, fc, fm):
    return (1 + m(t, Am, fm))*c(t, Ac, fc)

yc = c(t, Ac, fc)
ym = m(t, Am, fm)

plt.plot(t, ym, label = "Message signal")
plt.plot(t, yc, label = "Carrier signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-8,8])
plt.legend()
plt.show()

y = mod(t, Ac, Am, fc, fm)

plt.plot(t, y, label = "Modulated signal (AM)")
plt.plot(t, yc, ":" ,label = "Carrier signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-8,8])
plt.legend()
plt.show()