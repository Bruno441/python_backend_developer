import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'example.sqlite')
cursor = con.cursor()

# Criação de tabelas
# cursor.execute('CREATE TABLE IF NOT EXISTS example_table (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')

# Criação de registros
data = (1,'Bruno', "teste@email.com")
cursor.execute('INSERT INTO example_table (id, name, email) VALUES (?, ?, ?)', data)
con.commit()

# Atualização de registros
update_data = ('Bruno Silva', 'teste@email.com')
cursor.execute('UPDATE example_table SET name = ? WHERE email = ?', update_data)
con.commit()

# Exclusão de registros
delete_data = ('teste@email.com',)
cursor.execute('DELETE FROM example_table WHERE email = ?', delete_data)
con.commit()

# Inserção de múltiplos registros usando executemany
multiple_data = [
    (2, 'Ana', 'ana@email.com'),
    (3, 'Carlos', 'carlos@email.com'),
    (4, 'Maria', 'maria@email.com')
]
cursor.executemany('INSERT INTO example_table (id, name, email) VALUES (?, ?, ?)', multiple_data)
con.commit()

# Selecionando um registro com fetchone
cursor.execute('SELECT * FROM example_table WHERE id = ?', (2,))
row = cursor.fetchone()
print('fetchone:', row)

# Selecionando todos os registros com fetchall
cursor.execute('SELECT * FROM example_table')
rows = cursor.fetchall()
print('fetchall:', rows)

# Exemplo utilizando row factory para retornar resultados como dicionários
con.row_factory = sqlite3.Row
cursor = con.cursor()
cursor.execute('SELECT * FROM example_table')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))

    try:
        cursor.execute('INSERT INTO example_table (id, name, email) VALUES (?, ?, ?)', (5, 'João', 'joao@email.com'))
        con.commit()
    except sqlite3.Error as e:
        print('Erro ao inserir registro:', e)
        con.rollback()