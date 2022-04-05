require 'sqlite3'

db = SQLite3::Database.open 'Teste.db'
db.execute 'DELETE FROM clientes'

