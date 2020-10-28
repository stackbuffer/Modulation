import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-6, 6, 200) #generate time for x axis
fm = 10 #frequency of msg signal
fc = 50 #frequency of carrier signal
Am = 1 #Amplitude of msg signal
Ac = 1 #Amplitude of carrier signal
kf = 0.32 #frequency deviation constant

#message signal
def m(t, Am, fm):
    return Am*np.sin(2*(np.pi)*fm*t + np.pi/6) #np.pi/6 is phase

#carrier signal
def c(t, Ac, fc):
    return Ac*np.cos(2*(np.pi)*fc*t) 

#frequency modulation function
def mod(t, Ac, Am, fc, fm, kf):
    return Ac*np.cos(2*np.pi*fc*t + kf*(-Am*(np.cos(2*(np.pi)*fc*t))/2*(np.pi)*fc))


yc = c(t, Ac, fc)
ym = m(t, Am, fm)

plt.plot(t, ym, label = "Message signal")
plt.plot(t, yc, label = "Carrier signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-5,5])
plt.legend()
plt.show()

y = mod(t, Ac, Am, fc, fm, kf)

plt.plot(t, y, label = "Modulated signal (FM)")
plt.plot(t, yc, ":" ,label = "Carrier signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.ylim([-5,5])
plt.legend()
plt.show()