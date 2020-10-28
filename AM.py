import numpy as np
import matplotlib.pyplot as plt

class AmplitudeModulation():
	def __init__(self, t):
		self.t = t

	#message signal
	def msg(self, fm = 10, Am = 1):
		return Am*np.sin(2*(np.pi)*fm*self.t)

	#carrier signal
	def carrier(self, fc = 30, Ac = 2):
	    return Ac*np.cos(2*(np.pi)*fc*self.t) 

	#modulation function
	def modulated(self, fm = 10, fc = 30, Am = 1, Ac = 2):
	    return (1 + m(t, Am, fm))*c(t, Ac, fc)


class Plot():
	def __init__(self, t):
		self.t = t

	def plotMsgSignal(self, ym):
		plt.plot(self.t, ym, label = "Message Signal")
		plt.legend()
		plt.show()

	def plotCarrierSignal(self, yc):
		plt.plot(self.t, yc, label = "Carrier Signal")
		plt.legend()
		plt.show()

	def plotModulatedSignal(self, y):
		plt.plot(self.t, yc, label = "Modulated Signal")
		plt.legend()
		plt.show()



t = np.linspace(-np.pi, np.pi, 100)

Am = AmplitudeModulation(t)
p = Plot(t)

ym = Am.msg()

p.plotMsgSignal(ym)
