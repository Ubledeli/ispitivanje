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
f = lambda x : np.flip(x)

u13 = [230, 180, 150]
u23 = [240, 190, 180]
u1 = [235, 180, 150]
u = [136, 104, 87]
i1 = [1, 0.88, 0.32]
i2 = [1.5, 0.57, 0.48]
i0 = [1.25, 0.73, 0.4]
a1 = [48, -20, 10]
a2 = [-36, 21, -10]
p0 = [60, 5, 0]
kw = 5
pfe = p0

u13ks = [12, 9, 5]
u23ks = [13, 8.5, 6]
u1k = [12.5, 8.75, 5.5]
uk = [7.22, 5.05, 2.6]
ik  =[6.8, 4.7, 3]
pk = [40, 20, 8]
i1ks = [6.8, 5, 2.6]
i2ks = [6.8, 4.4, 3.4]
a1ks = [9, 4, 4]
a2ks = [-5, -9, -2]

kw_prve_kolone = 10
kw_druge_i_trece = 4
