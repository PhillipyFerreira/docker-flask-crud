'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    def read(self, id):
        #Logging - INFO - Database - read - Inicia conexão com bando de dados.
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                #Logging - INFO - Database - read - Conexão com o bando de dados sem passagem de parâmetro id, filtrando todos os registros.
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                #Logging - INFO - Database - read - Conexão com o bando de dados com passagem de parâmetro id, filtrando apenas o id escolhido.
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            #Logging - INFO - Database - read - Posiciona no registro encontrado.
            return cursor.fetchall()
        except:
            #Logging - CRITICAL/FATAL - Database - read - Erro na conexão com o bando de dados.
            return ()
        finally:
            #Logging - INFO - Database - read - Fecha a conexão com o bando de dados.
            con.close()

    def insert(self,data):
        #Logging - INFO - Database - insert - Inicia conexão com bando de dados.
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            #Logging - INFO - Database - insert - Executa INSERT com os valores informados.
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()
            #Logging - INFO - Database - insert - Commit realizado.
            return True
        except:
            #Logging - CRITICAL/FATAL - Database - insert - Erro na conexão com o bando de dados.
            con.rollback()

            return False
        finally:
            #Logging - INFO - Database - insert - Fecha a conexão com o bando de dados.
            con.close()

    def update(self, id, data):
         #Logging - INFO - Database - update - Inicia conexão com bando de dados.
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            #Logging - INFO - Database - update - Executa UPDATE com os valores informados.
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()
             #Logging - INFO - Database - update - Commit realizado.

            return True
        except:
            #Logging - CRITICAL/FATAL - Database - update - Erro na conexão com o bando de dados.
            con.rollback()
            return False
        finally:
            #Logging - INFO - Database - update - Fecha a conexão com o bando de dados.
            con.close()

    def delete(self, id):
        #Logging - INFO - Database - delelte - Inicia conexão com bando de dados.
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            #Logging - INFO - Database - delete - Executa DELETE utilizando o id como filtro.
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()
             #Logging - INFO - Database - delete - Commit realizado.
            return True
        except:
            #Logging - CRITICAL/FATAL - Database - delete - Erro na conexão com o bando de dados.
            con.rollback()

            return False
        finally:
            #Logging - INFO - Database - delete - Fecha a conexão com o bando de dados.
            con.close()
