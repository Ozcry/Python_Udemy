usuario = str(input('Nome do usuário: '))
senha = int(input('Senha do usuário: '))
usuario_bd = 'Jean Lucas'
senha_bd = 123456
if not usuario != usuario_bd and not senha != senha_bd:
    print('Acesso permitido')
else:
    print('Senha ou usuário incorreto')
