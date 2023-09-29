# CONDICIONAIS 

# teste de idade

idade = int(input('digite sua idade: '))

if idade >= 18:
    print('voce é maior de idade.')
else:
    print('voce é menor de idade')

# teste de nota

media = float(input('informe a media do aluno: '))

if media >= 7:
    print('aprovado.')
elif media >= 5:
    print('recuperacao.')
else:
    print('reprovado')

# teste de nota e presenca

nota = 7
presenca = 100

if nota >= 7 and presenca >= 70:
    print('aprovado')
elif nota >=7 and presencao >= 70:
    print('recuperacao')
else:
    print('reprovado')