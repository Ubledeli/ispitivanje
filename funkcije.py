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
