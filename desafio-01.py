# //Se listarmos todos os números naturais abaixo de 10 que são múltiplos de 3 ou 5, obtemos 3, 5, 6 e 9. A soma desses múltiplos é 23.
# Finalize a solução para que ela retorne a soma de todos os múltiplos de 3 ou 5 abaixo do número passado.
# Além disso, se o número for negativo, retorne 0.
# Observação: se o número for múltiplo de 3 e 5, conte-o apenas uma vez.

def solution(number):
  soma = 0
  for n in range(number):
      if n % 3 == 0 or n % 5 == 0:
          soma += n
      else:
          pass
  return(soma)
