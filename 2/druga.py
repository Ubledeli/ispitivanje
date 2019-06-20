import numpy as np
import matplotlib.pyplot as plt

def plot(x,y,stepen=1,n=0):
    x0 = x + [0] * n
    y0 = y + [0] * n
    p0 = np.poly1d(np.polyfit(x0,y0,stepen))
    xp = np.linspace(x[0], x[-1], 10000)
    yp = p0(xp)
    plt.plot(x,y,'o',xp,yp)
    plt.show()
    return

n = [980, 980, 980, 980, 950, 980, 970, 950, 900]
u = [220] * len(n)
i = [4, 5, 9, 12, 15, 19, 21.5, 24, 32]
p1 = [880, 1100, 1980, 2640, 3300, 4180, 4730, 5280, 7040]
m = [0.1, 0.32, 1.15, 1.7, 2.1, 2.8, 3.3, 3.7, 4.9]
m0 = [28, 28, 28, 28, 25, 28, 27, 25, 24] # podeliti sa 10000
ma = np.asarray(m)
m0a = np.asarray(m0)
na = np.asarray(n)
p = 1.027 * na * (ma + m0a / 10000)
ni = p / np.asarray(p1)
m = 9.56 * p / na

plot(list(n), list(m), stepen = 1)
plot(i, list(m), stepen = 2)
plot(i, list(p), stepen = 2)
plot(i, list(ni), stepen = 3, n = 10000)
plot(i, list(na))

