# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:50:24 2018

@author: Matt
"""

def dist_summary(dist, names = 'dist_name'):
    import pandas as pd
    import matplotlib.pyplot as plt
    ser = pd.Series(dist)
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.gca()
    ser.hist(ax = ax, bins = 120)
    ax.set_title('Frequency distribution of ' + names)
    ax.set_ylabel('Frequency')
    plt.show()
    return(ser.describe())
    
def gen_tips(num,numcustomers=1):  
    import pandas
    import numpy
    out=[tipjar(numcustomers) for _ in range(num)]
    return(out)
    
    
def tipjar(numcustomers):
    import numpy.random as nr
    unif = nr.uniform(size = numcustomers)
    out = 0 
    for x in unif:
        out +=  0 if x < 0.5 else (0.25 if x < 0.7 else (1.0 if x < 0.9 else 2.0))
    return out;


tps = gen_tips(100000,600)
dist_summary(tps, 'tips')