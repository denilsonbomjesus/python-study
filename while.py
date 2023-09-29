# WHILE

numero_sorteado = 15

numero_escolhido = int(input('escolha um numero: '))

while numero_escolhido != numero_sorteado:

    print('voce errou, tente novamente...')
    numero_escolhido = int(input('escolha um numero: '))

print('voce acertou')

# exemplo 02: estrutura com contador

contador = 0

while contador < 5:
    
    print(contador)
    contador = contador + 1