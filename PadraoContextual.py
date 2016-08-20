# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 16:56:31 2016

@author: bthalenberg
"""

def busca_padroes():
    
    import re
    
    f = open("/home/bthalenberg/Desktop/semantic vectors/corpus/corpus-lemma.txt", "r", encoding="utf-8")
   
    resultados = []
    
    for line in f:
        antonimos = re.findall("([A-Za-záàãâéèêẽóòõôíìiúùç]+) e não ([A-Za-záàãâéèêẽóòõôíìiúùç]+)", line)
        antonimos2 = re.findall("([A-Za-záàãâéèêẽóòõôíìiúùç]+), e não ([A-Za-záàãâéèêẽóòõôíìiúùç]+)", line)
        possiveis_antonimos = re.findall("entre ([A-Za-záàãâéèêẽóòõôíìiúùç]+) e ([A-Za-záàãâéèêẽóòõôíìiúùç]+)", line)
        
        if antonimos != []:
            resultados.append(antonimos)
        if antonimos2 != []:
            resultados.append(antonimos2)
        if possiveis_antonimos != []:
            resultados.append(possiveis_antonimos)
            
    f.close()
        
 
    with open("padroes-contextuais.txt", "w", encoding="utf-8") as file:
        for lista in resultados:
            file.write("\n".join("%s e %s\n" %x for x in lista))
            
    file.close()
   

busca_padroes()

