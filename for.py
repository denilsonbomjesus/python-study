
# faixa de 0 ao numero indicado

for variavel in range(5):
    print(variavel)

print('\nnova coisa \n')

# faixa do primiro ao segundo numero

for variavel in range (1, 5):
    print(variavel)

print('\nnova coisa \n')

# faixa do primeiro ao segundo numero, pulando de n em n a quantidade do terceiro numero

for variavel in range(2, 13, 2):
    print(variavel)

# codigo elaborado

print('\nnova coisa \n')

soma = 0

for i in range(1,4):
    nota = float(input(f'digite a nota {i}: '))

    soma = soma + nota

media = soma / 3
print('a media dos numeros é:', media)

    