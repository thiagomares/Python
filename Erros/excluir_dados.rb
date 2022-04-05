require 'sqlite3'

db = SQLite3::Database.open 'Teste.db'
db.execute 'ALTER TABLE clientes RENAME COLUMN telefone TO senha'

