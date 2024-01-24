# Implemente a função unique_in_order que toma como argumento uma sequência e retorna uma lista de itens sem nenhum
# elemento com o mesmo valor próximos uns dos outros e preservando a ordem original dos elementos.
# Por exemplo:
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]

def unique_in_order(sequencia):
    resultado = []
    elementoAnterior = None

    for elemento in sequencia:
        if elemento != elementoAnterior:
            resultado.append(elemento)
            elementoAnterior = elemento

    return resultado

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))

