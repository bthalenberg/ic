# -*- coding: utf-8 -*-

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
           if "</s>" in line[0]:
              line.append("</s>")
           if "\$" in line[0]:
              line[1] = line[0]
              
        if len(line) >= 2 and "<ext" not in line[0]:      
           corpus.append(line[1])   
          
    
    with open("new_f.txt", "w") as new_f:
         for item in corpus:
             new_f.write(item + " ")
    new_f.close()

      
lemma_extraction(sentences)        
       

 

