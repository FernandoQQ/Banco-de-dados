import sqlite3

conn = sqlite3.connect("empresa.db")
cursor = conn.cursor()
#cursor.execute("CREATE TABLE usuario(nome TEXT, senha NUMBER);")
cursor.execute('Insert into usuario(nome , senha) values ("Fernando",1234);')
conn.commit()
