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

pw = [250, 0, 100, 300, 500, 700, 850]
u = [240] * 7
i = [10] * 4 + [10.5] * 3
N = [2] * 7
t = [48, 32, 31, 26, 22, 17, 15]
s = [0.0008, 0.001, 0.001, 0.001, 0.002, 0.002, 0.003]
pg = [317, 317, 317, 318, 328, 329, 330]
p1 = [567, 317, 417, 618, 828, 1029, 1180]
ni = [0.44, 0, 0.24, 0.5, 0.6, 0.68, 0.72]
n = [1501, 1502, 1502, 1502, 1503, 1504, 1504]
cosfi = [0.06, 0, 0.02, 0.07, 0.11, 0.16, 0.19]
m = [3.55, 1.96, 2.6, 3.87, 5.2, 6.48, 7.43]



