# sem lista

nota1 = 7
nota2 = 8
nota3 = 9

# com lista

notas = [7, 8, 9]

# criando listas

lista = [] # vazia
lista = list() # funcao especifica do python para criacao de lista
lista = [2.3, 'Salvatore', True, 10] # com mais de um tipo de dado
lista_de_listas = [10, [1, 2, 3]] # lista de listas

# indexacao

lista = [2.3, 'Salvatore', True, 10]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1]) # imprime o ultimo elemento; lista[-2] o penultumo elemento...

print('\nnova coisa \n')

# slices (fatiamento)

lista1 = [10, 20, 30, 40, 50]

print(lista1[0:3]) # do elemento 0 até o elemento menor que 3
print(lista1[3:5])
print(lista1[1:]) # do elemento 1 até o final
print(lista1[1:5:2]) # do elemento 1 ao menor que 5 pulando de 2 em 2

print('\nnova coisa \n')

# INTERAÇÕES COM FOR

# utilizando os proprios elementos da lista

for elemento in lista1:
    print(elemento)

print('\nnova coisa \n')

# utilizando os indices

print('comprimento da lista:', len(lista1))

for i in range(len(lista1)):
    print(i)
    print(lista1[i])
    print('\n')


# > METODOS DE LISTAS

lista2 = [1, 3, 12, 8, 2]

# append -> adicionar elemento no final

print('antes do append:', lista2)

lista2.append(3)

print('depois do append:', lista2)

# insert -> escolhe onde adicionar

lista2.insert(2, 10) # 2 -> indice e 10 -> elemento

print('depois do insert:', lista2)

# extend -> juntar duas listas

lista2.extend(lista1) # adiona a lista1 no final da lista2

print('depois do extend:', lista2)

# pop -> remover elemento especificado, senao especificar remove o ultimo

lista2.pop()

print('depois do pop sem indice:', lista2)

lista2.pop(0)

print('depois de remover o elemento do indice 0:', lista2)

# remove -> remove o elemento indicado, se houver o mesmo elemento repetido, ele remove o primeiro que encontra

lista2.remove(3)

print('depois de remove elemento 3:', lista2)

# count -> contar quantas vezes um elemento aparece na lista

print('quantidade de 2 na lista:', lista2.count(2))

# index -> passa o index do elemento especificado

print('qual o index do elemento 8:', lista2.index(8))

# sort -> ordena os elementos da lista em ordem crescente

lista2.sort()

print('depois do sort:', lista2)

lista2.sort(reverse=True) # ordena de forma decrescente

print('depois do sort decrescente:', lista2)

# > FUNCOES PARA LISTAS

# len -> quantos elementos tem na lista

print('quantidade de elementos da lista:', len(lista2))

# sum -> soma todos os elementos da lista

print('soma de todos os elementos da lista:', sum(lista2))

# max -> maior elemento da lista

print('maior elemento da lista:', max(lista2))

# min -> menor elemento da lista

print('menor elemento da lista:', min(lista2))