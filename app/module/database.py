'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    def read(self, id): #Tracing, como visto em sala para controle, esta e as outras funções devem ter o tracing adicionado
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data): #Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit() #Pelo o que entendi o método .commit() dita que se uma transação for concluída com êxito, o banco de dados será alterado permanentemente portanto um Info -> LOG seria interessante

            return True
        except:
            con.rollback() #.rollback() é quando a transação ocorre sem êxito portanto um Info -> LOG seria interessante talvez até um WARNING pois se muitas operações não ocorrerem com êxito pode haver algo errado

            return False
        finally:
            con.close()

    def update(self, id, data): #Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit() #Info -> LOG Acompanhar o que está tendo exito

            return True
        except:
            con.rollback() #Info -> LOG seria interessante talvez até um WARNING pois se muitas operações não ocorrerem com êxito pode haver algo errado

            return False
        finally:
            con.close()

    def delete(self, id): #Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit() #Info -> LOG Acompanhar o que está tendo exito

            return True
        except:
            con.rollback() #Info -> LOG seria interessante talvez até um WARNING pois se muitas operações não ocorrerem com êxito pode haver algo errado

            return False
        finally:
            con.close()
