

#####################################################################
# CONSTANTES

MAIUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛÇ'
MINUSCULAS = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìîóòõôúùûç'
LETRAS     = MAIUSCULAS + MINUSCULAS

#####################################################################

def main():

    nome = input("Digite o nome do arquivo: ")
    
    with open(nome, 'r', encoding='utf-8') as entrada:
        texto = entrada.read()

    palavra, quantidade = conta_palavras( texto )
    ordena_decrescente(palavra, quantidade)
    string = imprima_palavras(palavra, quantidade)
    
    with open("new_f.txt", "w") as new_f:
         new_f.write(string)
    new_f.close()


######################################################################

def imprima_palavras(pal, freq):
    
    i = 0; s = ""
    
    while i < 200:
        s += str(pal[i])
        s += "\n"
        i += 1
    return s

                
######################################################################

def conta_palavras(texto):
    
    palavras = [] #armazena as palavras
    frequencia = [] #armazena as frequências
    
    texto = lower(texto) #chamamos a função lower definida abaixo para tornar a função case insensitive
    listexto = texto_em_lista(texto) # = texto.split()  
    
    k = 0 #iterador
    n = len(listexto) #tamanho do texto
    
    
    while k < n:
        #a função índice retorna o índice de um item numa lista, caso contrário, retorna None
        if indice(listexto[k], palavras) is None: #se o caractere não foi encontrado...
            palavras.append(listexto[k]) #... precisamos acrescentar na lista de caracteres...
            frequencia.append(1) #... e sua ocorrência é 1
        else:
            #se não retornou None, é porque já está na lista de caracteres pois apareceu anteriormente:
            index = indice(listexto[k], palavras) #buscamos pelo indice e...
            frequencia[index] += 1 #... somamos um ao número registrado naquele indice na lista de ocorrencias
            
        k += 1 #próximo loop           
    
    return palavras, frequencia
    
######################################################################

def indice (item, seq):
    '''(objeto,list ou str) -> int ou None

    Recebe um objeto 'item' e uma estrutura sequencial 'seq' e
    retorna o índice da posição em que item ocorre em seq.
    Caso item não ocorra em seq a função retorna o valor None.'''
    
    k = 0 #iterador na lista
    n = len(seq) #tamanho da lista
        
    while k < n: 
        if item == seq[k]: #se o objeto for igual àquele que está na lista no índice 
           return k #retorna o índice            
        k += 1 #próximo loop
        #ao terminar, se não encontrar, retorna None


######################################################################

def ordena_decrescente(pal, freq):
    ''' (list, list)

    Recebe uma lista 'pal' de palavras e outra lista 'freq' de mesmo tamanho 
    com  o número de ocorrências das palavras de índices correspondentes.

    A função modifica as duas listas, acabando quando as palavras
    estiverem em ordem decrescente de número de ocorrências.      
    '''
    
    n = len(freq)
    i = 1
    
    while i < n:
        pivo = freq[i]
        pivo2 = pal[i]
        j = i-1
        while j >= 0 and freq[j] < pivo:
            freq[j+1] = freq[j]
            pal[j+1] = pal[j]
            j -= 1
        freq[j+1] = pivo
        pal[j+1] = pivo2
        i += 1
    

######################################################################

def lower(texto):
    '''(str)-> str
    
    Equivalente à função built-in string.lower(), recebe uma string e
    retorna sua versão em minúsculas. Se já for minúscula, retorna ela mesma.
    Exemplos:
    
    >>> lower(casa)
    casa
    >>> lower(Casa)
    casa
    >>> lower(CaSA)
    casa'''
    
    resp = ""
    n = len(MAIUSCULAS)
    m = len(texto)
    i = 0 #iterador nas listas
    it = 0 #iterador na string
    maiuscula = False
    
    while it < m:
        while i < n:
            if texto[it] == MAIUSCULAS[i]: #se estiver na lista de maiusculas
                resp += (MINUSCULAS[i]) #acrescenta na resposta o caractere minusculo
                maiuscula = True
            i += 1 #vai para a pŕoxima letra da lista até acabar a lista de letras
        if maiuscula == False: #se não encontrou, era minúscula ou não alfabético
            resp += (texto[it]) #adiciona ele mesma
        maiuscula = False; i = 0 #reinicia os parâmetros para o próximo loop
        it += 1 #próximo caractere
    return resp
        
######################################################################
        
def texto_em_lista(texto):
    '''(str) -> list
    A partir de um texto, cria uma lista com suas palavras, retirando espaços e pontuações, equivale a str.split()'''
        
    lista = []
    texto += "\s"
    n = len(texto)
    i = 0 #iterador
    palavra = ""
    
    while i < n:
        if texto[i] in LETRAS:
            palavra += texto[i]
            
        else:
            if palavra != "":
                lista.append(palavra)
                palavra = ""
        i += 1
    return lista
  
if __name__ == "__main__":         
    main()
