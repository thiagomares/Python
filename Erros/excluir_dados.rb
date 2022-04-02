require 'sqlite3'

db = SQLite3::Database.open 'Teste.db'
db.execute 'DELETE FROM clientes'

for valor in db.execute 'SELECT * FROM clientes'
    id, nome, telefone = valor
    puts id, nome, telefone
end

db.close