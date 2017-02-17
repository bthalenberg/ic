# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 12:33:26 2016

@author: bthalenberg
"""
import logging, os
             
def sentencas_uteis():
    import csv, itertools
    
    with open("200-adjetivos.csv", "r", encoding="utf-8") as adjetivos:
        reader = csv.reader(adjetivos)
        adj1 = list(reader)
        adj = set(list(itertools.chain.from_iterable(adj1)))
        adj.remove("")
       
    lista_sentencas = []

    with open("/home/bthalenberg/ic/teste/corpus-pos.txt", 'r', encoding='utf-8') as f:
        for line in f:
            vista = False
            for item in adj:
                if item in line and not vista:
                    vista = True
                    lista_sentencas.append(line)
                
    with open("corpus-util.txt", "w", encoding="utf-8") as c:
        for sentenca in lista_sentencas:
            c.write(sentenca)


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 

def novos_vetores(diretorio, nome):
    
    sentences = MySentences(diretorio)
    
    from gensim.models import Word2Vec
    
    model = Word2Vec(sentences, min_count = 15, size = 150, window = 4, sg = 1, negative=5)
    model.save_word2vec_format(nome+".txt", binary=False)
    
def usando():
    modelo = Word2Vec.load('/home/bthalenberg/ic/vetores-seletos')

def cortando(iterador, pos, novo_nome):
	'''pos é uma string no formato (___), novo_nome é uma string com o nome do novo arquivo a ser gerado'''
	
 

	corpus_novo = []
	for line in iterador: #lembrando que o iterador fornece linha.split() do arquivo
		if "(ADJ)" in '\t'.join(line):
			for pal in line:
				if pos in pal: corpus_novo.append(pal)
				elif "(ADJ)" in pal: corpus_novo.append(pal)
			corpus_novo.append("\n")

	with open(novo_nome, "w") as f:
		for item in corpus_novo:
			f.write(item + " ")

def cortando3(iterador, pos1, pos2, novo_nome):
	'''pos é uma string no formato (___), novo_nome é uma string com o nome do novo arquivo a ser gerado'''
	
	corpus_novo = []
	for line in iterador: #lembrando que o iterador fornece linha.split() do arquivo
		if "(ADJ)" in '\t'.join(line):
			for pal in line:
				if pos1 in pal or pos2 in pal: corpus_novo.append(pal)
				elif "(ADJ)" in pal: corpus_novo.append(pal)
			corpus_novo.append("\n")

	with open(novo_nome, "w") as f:
		for item in corpus_novo:
			f.write(item + " ")
	
