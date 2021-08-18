nome = 'Jean Lucas'
idade = 23
altura = 1.75
e_maior = idade > 18
peso = 65
print('Nome:', nome, type(nome))
print('Idade:', idade, type(idade))
print('Altura:', altura, type(altura))
print('É maior:', e_maior, type(e_maior))
_teste = 5
print(_teste)
print(idade * altura)
imc = peso / altura ** 2
print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
