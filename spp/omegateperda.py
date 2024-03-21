import matplotlib.pyplot as plt
import numpy as np

NP = 10000
W_P = 2*np.pi*10000000000.
W_0 = 2*np.pi*4000000000.
F = 0.56
G_M = 1.
W_SPP = W_P/np.sqrt(2)
beta = np.linspace(0,1,NP)
# frequencia onde acontece o spp na polarização TE (ja dividido por W_P)
d = (2.-F)
e = (2.*G_M**2 + (F-4.)*W_0**2)
f = 2.*W_0**4
delta = (2.*G_M**2 + (F-4.)*W_0**2)**2 - 4*(2.-F)*2.*W_0**4

# aqui nao foi divido por W_P ainda devido ao calculo
def wspp_te_func(beta):
    return (np.sqrt((-(2.*(beta*W_SPP)**2 + (F-4.)*W_0**2)+np.sqrt(((beta*W_SPP)**2 + (F-4.)*W_0**2)**2 - 4*(2.-F)*2.*W_0**4))/(2.*(2.-F))))
# aqui foi divido por W_P


def w_tm(b):
    return W_SPP*np.sqrt(1.-b**2)

fig, ax = plt.subplots()
ax.plot(beta, wspp_te_func(beta)/W_P, color="royalblue", zorder=9)
# limites dos eixos
#ax.set(xlim=(0,0.008))
#ax.set(ylim=(0.42,0.48))

plt.xlabel(r'$\beta$')
plt.ylabel(r'$\dfrac{\omega_{TE}}{\omega_p}$', rotation=0, labelpad=15)
plt.show()
