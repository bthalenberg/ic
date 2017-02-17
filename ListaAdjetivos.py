# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 21:31:42 2016

@author: bthalenberg
"""

import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
 
sentences = MySentences('/home/bthalenberg/Desktop/semantic vectors/corpus/tsv')

def busca_adjetivos(f):
    adjetivos = []
    for line in f:
              
        if line != []:
           if "ADJ" in line:
              adjetivos.append(line[1])
    
    with open("new_f.txt", "w") as new_f:
         for item in adjetivos:
             new_f.write(item + "\n")
    new_f.close()

      
busca_adjetivos(sentences)        
       

 

