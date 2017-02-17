# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:47:03 2017

@author: bthalenberg
"""

from sklearn.decomposition import TruncatedSVD
import numpy as np
from gensim.models import Word2Vec

def svd(nome):
    '''nome deve ser escrito com a extensão ".txt" '''
    
    import itertools, csv
    
    with open("200-adjetivos.csv", "r", encoding="utf-8") as adjetivos:
        reader = csv.reader(adjetivos)
        adj1 = list(reader)
        adj = list(itertools.chain.from_iterable(adj1))
        adj = [x+"(ADJ)" for x in adj]
        adj = set(adj)
        adj.remove("(ADJ)")
     
    
    f = open("vetores cortados/" + nome, 'r')
    novo = open("novos vetores/" + nome,'w')

    arq = f.readlines()
    vecs = [] #lista de vetores
    words = [] #lista de palavras
    for line in arq:
        line = line.split(" ")
        if line[0] in adj:
            words.append(line[0])
            vec = line[1:]
            vecs.append([float(num) for num in vec])   
        
    array = np.array(vecs)
    svd = TruncatedSVD()
    svd.fit(array)
    a = svd.transform(array)
    
    for word,line in zip(words,a):
    	str1 = " ".join(str(x) for x in line)
    	newline = word+" "+str1+"\n"
    	novo.write(newline)
    novo.close
                    


