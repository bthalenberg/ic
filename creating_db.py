# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:58:23 2017

@author: bthalenberg
"""

def main():
    import os
    
    target, ant, syn = cria_listas()
    
    for filename in os.listdir("/home/bthalenberg/ic/novos novos"):
        pega_dados(filename, target, ant, syn)

def cria_listas():
    
    import csv
    
    target = []
    ant = []
    syn = []
    
    with open("/home/bthalenberg/ic/adj.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            target.append(row[0]+"(ADJ)")
            ant.append(row[1]+"(ADJ)")
            syn.append(row[2]+"(ADJ)") 
    
    #deleting header        
    del target[0], ant[0], syn[0]
            
    return target, ant, syn
    
def pega_dados(vecfile, target, ant, syn):
    
    import csv
    from gensim.models import KeyedVectors

    cosine_ant = []
    cosine_syn = []
    subcos_ant = []
    subcos_syn = []
    
    mod = KeyedVectors.load_word2vec_format("/home/bthalenberg/ic/novos novos/"+vecfile, binary=False)
    
    i = 0
    while i != len(target):
        
        #getting cosine similary between target and antonym
        try:
            cos = mod.similarity(target[i], ant[i])
        except KeyError:
            cos = None
        cosine_ant.append(cos)
        
        #getting cosine similary between target and synonym
        try:
            cos_s = mod.similarity(target[i], syn[i])
        except KeyError:
             cos_s = None
        cosine_syn.append(cos_s)


        #subtracting the antonym cosine similarity from the synonym similarity for syn input
        try:
            subcos_syn.append(cos_s - cos)
        except TypeError:
            subcos_syn.append(None)
        
        #negating subtracted values for ant input
        try:
            subcos_ant.append(-(cos_s - cos))
        except TypeError:
            subcos_ant.append(None)
        
        i += 1
        
    dirname = vecfile[:-4]
    
    with open(dirname+"/db_ant.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        i = 0
        while i != len(target):
            writer.writerow([target[i], ant[i], cosine_ant[i]])
            i += 1
            
    with open(dirname+"/db_syn.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        i = 0
        while i != len(target):
            writer.writerow([target[i], syn[i], cosine_syn[i]])
            i += 1
                        
    with open(dirname+"/db_sub_ant.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        i = 0
        while i != len(target):
            writer.writerow([target[i], ant[i], subcos_ant[i]])
            i += 1
            
    with open(dirname+"/db_sub_syn.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        i = 0
        while i != len(target):
            writer.writerow([target[i], syn[i], subcos_syn[i]])
            i += 1
                
        
    
if __name__ == '__main__':
    main()
