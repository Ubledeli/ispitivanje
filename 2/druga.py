import numpy as np
import matplotlib.pyplot as plt


n = [980, 980, 980, 980, 950, 980, 970, 950, 900]
u = [220] * len(n)
i = [4, 5, 9, 12, 15, 19, 21.5, 24, 32]
p1 = [880, 1100, 1980, 2640, 3300, 4180, 4730, 5280, 7040]
m = [0.1, 0.32, 1.15, 1.7, 2.1, 2.8, 3.3, 3.7, 4.9]
m0 = [28, 28, 28, 28, 25, 28, 27, 25, 24] # podeliti sa 10000
p = 1.027(m+m0)*n
ni = p/p1
m = 9.56*p/n