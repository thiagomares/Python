require 'sqlite3'

db = SQLite3::Database.open 'Teste.db'
puts db.execute 'Select * FROM clientes'

