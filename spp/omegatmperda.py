import matplotlib.pyplot as plt
import numpy as np

NP = 10000
W_P = 2*np.pi*10000000000.
W_SPP = W_P/np.sqrt(2)
b = np.linspace(0,1,NP)

def w_tm(b):
    return W_SPP*np.sqrt(1.-b**2)

fig, ax = plt.subplots()
ax.plot(b, w_tm(b)/W_P, color="crimson", zorder=9)
plt.title(r'$\omega_{TM} = \omega_{SPP}\sqrt{1-\beta^2}$')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$\omega_{TM}/\omega_p$', rotation=0, labelpad=15)
plt.show()