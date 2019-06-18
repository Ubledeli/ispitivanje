import numpy as np
import matplotlib.pyplot as plt


jpk = [0, 1.5, 2.8, 4, 5.2]
ik = [0, 2, 4, 6, 8]

o = [0]*100000
ik0 = o + ik
jpk0 = o + jpk
p0 = np.poly1d(np.polyfit(ik0,jpk0,1))
x = np.linspace(ik[0], ik[-1], 5000)
y = p0(x)
#plt.plot(ik,jpk,'o', x,y)
#plt.show()

jp1 = [1,2,3,4,4.9,6,7,8,9]
jp2 = [1,2,3,4,5.1,6,7,8,9]
jp3 = [1,2,3,4,5.1,6,7,8,9]

ig1 = [5.4,3.8,2.4,1.22,0,1.22,2.4,3.6,4.75]
ig2 = [5.6,4.1,1.6,1.35,0.63,1.35,2.5,3.75,4.7]
ig3 = [5.9,4.25,2.8,1.53,1.1,1.53,2.5,3.7,4.75]

mord1 = np.poly1d(np.polyfit(jp1,ig1,2))
x1 = np.linspace(jp1[0],jp1[-1],10000)
y1 = mord1(x1)
#plt.plot(jp1,ig1,'o', x1,y1)

jp10 = [4.9]*100000 + jp1
ig10 = o + ig1

jp20 = [5.1]*100000 + jp2
ig20 = [0.63]*100000 + ig2

jp30 = [5.1]*100000 + jp3
ig30 = [1.1]*100000 + ig3

mord1 = np.poly1d(np.polyfit(jp10,ig10,3))
mord2 = np.poly1d(np.polyfit(jp20,ig20,3))
mord3 = np.poly1d(np.polyfit(jp30,ig30,3))

x1 = np.linspace(jp1[0],jp1[-1],10000)
x2 = np.linspace(jp2[0],jp2[-1],10000)
x3 = np.linspace(jp3[0],jp3[-1],10000)

y1 = mord1(x1)
y2 = mord2(x2)
y3 = mord3(x3)

#plt.plot(jp1,ig1,'o', x1,y1,jp2,ig2,'o', x2,y2,jp3,ig3,'o', x3,y3)

jph = [-6, -4.5, -3.4, -2.15, -1.9, -1.25, -0.9, -0.45, -0.2, 0, 0.5, 1.1, 1.5, 2.1, 2.7, 4.1, 6]
eph = [-440, -390, -320, -220, -165, -112, -63, 0, 30, 58, 116, 170, 220, 270, 320, 385, 440]

jph0 = [-6]*10000 + jph + [6]*10000
eph0 = [-440]*10000 + eph + [440]*10000
histg = np.poly1d(np.polyfit(jph0,eph0,3))
xhist = np.linspace(jph[0],jph[-1],10000)
yhist = histg(xhist)

jpha = np.asarray(jph)
epha = np.asarray(eph)

#plt.plot(jph,eph,'o',-jpha,-epha,'o', xhist,yhist, -xhist,-yhist)
#plt.show()

rev = np.flip(-yhist)
sred = 0.5*(rev + yhist)


h = np.poly1d(np.polyfit(xhist[4950:5050], sred[4950:5050],1))
tang = h(xhist)

#plt.plot(jph,eph,'o',-jpha,-epha,'o', xhist,yhist, -xhist,-yhist, xhist, sred, xhist, tang)
nominalna_pobuda = xhist[np.where(sred>=400)[0][0]]
