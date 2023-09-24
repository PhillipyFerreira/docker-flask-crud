'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    # PODEM SER INSERIDAS METRICAS DO FOUR GOLDEN SIGNAL
    def connect(self):
        # INFO 
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    def read(self, id):
         # INFO 
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
             # WARNING 
            return ()
        finally:
            con.close()

    def insert(self,data):    
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            # INFO 
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            return True
        except:
            # WARNING 
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            # INFO 
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
        except:
            # WARNING 
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
         
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            # INFO 
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            # WARNING 
            con.rollback()

            return False
        finally:
            con.close()
