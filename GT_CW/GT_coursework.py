import numpy as np
import matplotlib.pyplot as plt

def C(x):
    y = x.copy()
    return 10*np.log(y)

def D(x):
    y = np.zeros(len(x))
    c = min(x)
    for i in range(len(x)):
        y[i] = (c/x[i])**2
    y = y*100/sum(y)
    return y

p = np.zeros((40,6))
for i in range(40):
    p[i] = np.array([2,0,0,0,0,0]) + 30*np.array([0,1,1.5,2,2.5,3])

prod = D(np.array([10000000,2/np.sqrt(3),np.sqrt(3/2),np.sqrt(2),np.sqrt(3),2])) + np.array([2,-0.4,-0.4,-0.4,-0.4,-0.4])

w = np.zeros(6) + np.array([0,1000,1000,1000,1000,1000])

def bertrandcomp(rounds, pricemat, productionvec, wealthvec):
    """Calculate the round's costs from the production volume given in the initial production volume vector
    Calculate this round's demands for next round from this round's prices
    Calculate this round's production by averaging last round's production and this round's demand
    Calculate the payoffs using this round's prices, production and costs
    Add these payoffs to the cumulative wealth
    Repeat for the given number of rounds
    Finally return the finalised wealth vector"""
    wealthmat = np.zeros((rounds+1,len(productionvec)))
    wealthmat[0] += wealthvec
    for i in range(rounds):
        costvec = C(productionvec)
        demandvec = D(pricemat[i])
        nuproductionvec = (3*productionvec + demandvec)/4
        g = costvec.copy()*(-1)
        b = pricemat[i].copy()
        for j in range(len(b)):
            b[j] = b[j]*min(nuproductionvec[j], productionvec[j])
        g += b
        wealthvec += g
        productionvec = nuproductionvec
        wealthmat[i+1] += wealthvec
        print(g)
    
    plt.figure()
    plt.plot(wealthmat[:,:6])
    plt.xlabel('Iterations of competition')
    plt.ylabel('Cumulative wealth of firms')
    plt.title("Undercutting competitor results")
    return wealthvec

bertrandcomp(40, p, prod, w)
