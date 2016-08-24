# -*- coding: utf-8 -*-
import re, os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split("\t")
            
 
 
sentences = MySentences('/home/bthalenberg/Desktop/semantic vectors/corpus/tsv')

def pos_extraction(f):
    corpus = []
    

  
    for line in f:
                         
        if re.search("<\/s>|<s>|\$", line[0]) is not None:
            corpus.append(line[0])
        
        if len(line) >= 2:
            if "[" in line[1]:
                lemma = line[1]
                for value in line:
                    if re.search("^PROP$|^PRP$|^N$|^V$|^ADV$|^DET$|^ADJ$|^NUM$|^KC$|^PERS$|^KS$|^SPEC$|^EC$|^IN$", value) is not None and "@" not in value:
                      lemma += "(" + value + ")"
                      corpus.append(lemma)
        
    with open("new_f.txt", "w") as new_f:
         for item in corpus:
             new_f.write(item + " ")
    new_f.close()

      
pos_extraction(sentences)        
       

 

