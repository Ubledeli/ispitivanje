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

u0 = [245, 220, 200, 170, 138, 120]
i0 = [4.5, 4.5, 4.5, 4.8, 5.2, 6]
n = [1500] * len(i0)
r = [466.73, 466.73, 466.73, 462.44, 456.90, 446.42]
r75 = [554.35,554.35,554.35,549.24,542.66,530.22] # milioma
ip = [1.4, 1.15, 1, 0.8, 0.58, 0.58]
#ri0 = [2.07, 2.07, 2.07, 2.16, 2.29, 2.58]
r75io = a(r75) * a(i0) / 1000
rio2 = r75io * a(i0)
ea = a(u0) - r75io
pfepf = ea * a(i0)


iam = [10*x for x in range(1,9)]
um = [220] * len(iam)
rm = [0.50, 0.43, 0.41, 0.40, 0.40, 0.39, 0.39, 0.39]
eam = [215, 211, 208, 204, 200, 197, 193, 189]
pfepfm = [960, 940, 930, 920, 900, 890, 880, 860]
ipm = [1.25, 1.12, 1.08, 1.06, 1.05, 0.9, 0.9, 0.87]
im = a(iam) + a(ipm)
p1m = im * a(um)
pdm = a(iam) * a(iam) / 34
pgm = a(pfepfm) + a(rm) /1000 * a(iam) * a(iam) + a(um) * a(ipm) + pdm
nim = (p1m - pgm) / p1m

iag = iam
rg = rm
pgg = pgm
pg = p1m
nig = pg / (pg + pgg)
eag = [225, 229, 232, 236, 240, 243, 247, 251]
ipg = [1.26, 1.26, 1.27, 1.32, 1.35, 1.38, 1.45, 1.5]

