import sqlite3 as sql
import mysql.connector


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sql.connect(arquivo)
        self.cursor = self.conn.cursor()
        
    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()
        
    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()
        
    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id, ))
        self.conn.commit()
        
    def listar(self, valor):
        self.cursor.execute('SELECT * FROM agenda WHERE nome LIKE ?', (f'%{valor}%', ))  # Com isso aqui, conseguimos buscar itens no meio do nome      
        for linha in self.cursor.fetchall():
            print(linha)
        
    def fechar(self):
        self.cursor.close()
        self.conn.close()
            

if __name__ =='__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Thiago', '31989190738')
    agenda.inserir('Thiago Mares', '31358258881')
    agenda.inserir('Ana Clara', '999999999')
    
agenda.listar('Ana Clara')
agenda.fechar()