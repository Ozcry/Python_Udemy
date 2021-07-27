import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def conecta():
    conexao = pymysql.connect(  # criando conexão
        host='127.0.0.1',
        user='root',
        # password='' --> senha do servidor
        db='clientes',  # opcional
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor  # removendo esse parâmetro o banco de dados me retorna uma tupla
    )

    try:
        yield conexao
    finally:
        conexao.close()


# Comando UPDATE
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Jean', 3))
        conexao.commit()
'''


# Comando DELETE
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql, (6,))
        conexao.commit()
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        cursor.execute(sql, (1, 2, 4))
        conexao.commit()
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql, (5, 7))
        conexao.commit()
'''


# Comando INSERT
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        cursor.execute(sql, ('Jean', 'Lucas', 23, 65))
        conexao.commit()
'''

'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        dado = [
            ('Emile', 'Gracielle', 21, 50),
            ('Giovanna', 'Alves', 17, 43),
            ('Matheus', 'Mol', 24, 86),
            ('Daniel', 'Willians', 21, 53),
            ('Karine', 'Gracielle', 44, 70),
            ('Priscila', 'Nascimento', 41, 69),
            ('Diego', 'Nascimento', 37, 78)
        ]
        cursor.executemany(sql, dado)
        conexao.commit()
'''


# Comando SELECT
with conecta() as conexao:  # gerenciador de contexto da conexão
    with conexao.cursor() as cursor:  # gerenciador de contexto do cursor
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['nome'], linha['sobrenome'])

print('\033[33m-=\033[m' * 20)

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT nome, sobrenome FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['nome'], linha['sobrenome'])

print('\033[33m-=\033[m' * 20)

with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT nome as n, sobrenome as sn FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['n'], linha['sn'])
