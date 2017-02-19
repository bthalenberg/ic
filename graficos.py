# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 20:11:50 2017

@author: bthalenberg
"""

import matplotlib.pyplot as plt


def grafico(nome):

    f = open(nome+".txt", 'r')
    x = f.readlines()
    for line in x:
        ind = line.index("(")
        word = line[:ind]
        x = float(line.split(' ')[1])
        y = float(line.split(' ')[2])  
        plt.text(x-1,y,(word),fontsize=8)
    
    
    plt.ylabel('SVD/LSA - 150 to 2 dimensions')
    plt.axis([-0.2, 1.5, -2, 2])
    plt.show()
