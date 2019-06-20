import numpy as np
import matplotlib.pyplot as plt

def plot(x,y,stepen=1,n=0):
    x0 = [0] * n + list(x)
    y0 = [0] * n + list(y) 
    p0 = np.poly1d(np.polyfit(x0,y0,stepen))
    xp = np.linspace(x[0], x[-1], 10000)
    yp = p0(xp)
    plt.plot(x,y,'o',xp,yp)
    plt.show()
    return
    
a = lambda x : np.asarray(x)

u = [241, 226, 208, 191, 172, 156, 139, 122, 104, 87, 70, 52]
i0 = [2.55, 2.2, 1.85, 1.65, 1.45, 1.3, 1.1, 1, 0.9, 0.8, 0.8, 0.75]
p0 = [285, 245, 213, 192, 175, 153, 143, 129, 120, 113, 107, 104]
pfepf = a(p0) - 3*8.94* a(i0) * a(i0)
u1 = a(u) * 1.73
cosfi = a(p0) / (3 * a(u) * a(i0))



uk = [73, 64, 58, 48, 41, 32]
ik = [4.6, 4, 3.5, 3, 2.5, 2]
pk = [623, 481, 387, 278, 202, 126]

