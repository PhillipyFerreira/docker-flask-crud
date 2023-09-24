'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    #adicionar métricas de latência e tracing
    def connect(self):
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))
            #Four Golden signal: Medir latência das consultas SELECT
            return cursor.fetchall()
        except:
            #logging ERRO para registrar erros de consulta
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            #logging INFO para registrar inserções bem-sucedidas

            return True
        except:
            con.rollback()
            #logging ERROR para registrar falhas na inserção
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()
            #logging oara registrar atualizações bem-sucedidas
            return True
        except:
            con.rollback()
            #logging ERROR para registrar falhas na inserção
            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()
            #logging INFO para registrar exclusões bem-sucedidas

            return True
        except:
            con.rollback()
            #logging ERROR para registrar falhas na exclusão
            return False
        finally:
            con.close()
