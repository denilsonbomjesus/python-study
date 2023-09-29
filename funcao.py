# > FUNCOES 

# criando funcoes

# funcao inicial

def saudacao():
    print('seja bem vindo')
    print('é um prazer tê-lo fazendo parte desse curso')

saudacao()

# funcao com parametros

def saudacao(nome, curso):
    print(f'seja bem vindo, {nome}')
    print(f'é um prazer tê-lo fazendo parte do curso de {curso}')

saudacao('Salvatore', 'ADA Python')

# funcao com parametros default

def saudacao(nome, curso='Python'):
    print(f'seja bem vindo, {nome}')
    print(f'é um prazer tê-lo fazendo parte do curso de {curso}')

saudacao('Salvatore')
saudacao('Salvatore', 'ADA C')

# funcao com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(2, 3)

print('o resultado da soma é:', resultado)