nome = 'Jean Lucas'
idade = 23
altura = 1.75
peso = 65.2
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos de idade')
print('{} tem {} anos de idade'.format(nome, idade))
print('{1} tem {0} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu no ano de {nascimento}.')
