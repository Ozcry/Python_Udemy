import sqlite3

conexao = sqlite3.connect('basededados.db')       # conectando com o banco de dados
curso = conexao.cursor()


curso.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'                      # Criando tabela
               'nome TEXT,'
               'peso REAL'
               ')')


curso.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('emile', 21))      # Inserindo registros
curso.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
              {'nome': 'giovanna', 'peso': 17})
curso.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
              {'id': None, 'nome': 'matheus', 'peso': 0})
conexao.commit()


curso.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
              {'nome': 'joana', 'id': 3})                           # atualizando registros
conexao.commit()


curso.execute('DELETE FROM clientes WHERE id=:id',                       # deleta um registro da tabela
              {'id': 3})
conexao.commit()


curso.execute('SELECT * FROM clientes')        # buscando valores da tabela
curso.execute('SELECT nome, peso FROM clientes WHERE peso > 20')    # buscando valores de forma mais especifica
curso.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
              {'peso': 20})

for linha in curso.fetchall():
    nome, peso = linha
    print(nome, peso)


curso.close()
conexao.close()                         # Fechando tudo
