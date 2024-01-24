# Dado um array de inteiros, encontre aquele que aparece um número ímpar de vezes.
# Sempre haverá apenas um número inteiro que aparece um número ímpar de vezes.
# Exemplos:
# [7] deve retornar 7, porque ocorre 1 vez (o que é ímpar).
# [0] deve retornar 0, porque ocorre 1 vez (o que é ímpar).
# [1,1,2] deve retornar 2, porque ocorre 1 vez (o que é ímpar).
# [0,1,0,1,0] deve retornar 0, pois ocorre 3 vezes (o que é ímpar).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] deve retornar 4, porque aparece 1 vez (o que é ímpar).

def solution(array):
    elementosArray = {}  # Cria um dicionário vazio para armazenar os elementos e suas contagens
    for n in array:
        if n in elementosArray:
            elementosArray[n] += 1  # Se o elemento já existe no dicionário, incrementa sua contagem
        else:
            elementosArray[n] = 1   # Se o elemento é novo, adiciona-o ao dicionário com contagem 1
    for n, count in elementosArray.items():
        if count % 2 != 0:  # Percorre os elementos e suas contagens no dicionário
            return n        # Se a contagem for ímpar, imprime o elemento correspondente
