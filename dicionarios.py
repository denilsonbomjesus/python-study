# > DICIONARIOS

# criando dicionarios

dicionario = {} # dicionario vazio
dicionario = dict() # funcao que cria dicionarios

dicionario = {'nome': 'Salvatore', 'idade': 19, 'altura': 1.74}

print(dicionario)
print(dicionario['idade'])

# adicionando elementos a um dicionario

dicionario['programador'] = True

print(dicionario)

# sobrescrever

dicionario['altura'] = 2

print(dicionario)

# iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

# testando a existencia de uma chave

print('peso' in dicionario)
print('nome' in dicionario)