# -*- coding: utf-8 -*-
import copy, re

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
 
sentences = MySentences('/home/bthalenberg/Desktop/semantic vectors/testes/corpus')

def lemma_extraction(f):
    corpus = []
    for line in f:
              
        if line != []:
           if re.search("</s>", line[0]) is not None:
              line.append("</s>")
           if re.search("\$", line[0]) is not None:
              line[1] = copy.copy(line[0])
              
        if len(line) >= 2 and re.search("<ext", line[0]) is None:      
           corpus.append(line[1])   
          
    
    with open("new_f.txt", "w") as new_f:
         for item in corpus:
             new_f.write(item + " ")
    new_f.close()

      
lemma_extraction(sentences)        
       

 

