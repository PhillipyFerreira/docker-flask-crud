'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database: 
    def connect(self):
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" ) # LOG: INFO

    def read(self, id): # Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except: 
            return ()  # LOG: DEBUG
        finally:
            con.close()

    def insert(self,data): # Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit() # LOG: INFO

            return True
        except:
            con.rollback() # LOG: DEBUG

            return False
        finally:
            con.close()

    def update(self, id, data): # Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit() # LOG: INFO

            return True
        except:
            con.rollback() # LOG: DEBUG

            return False
        finally:
            con.close()

    def delete(self, id): # Tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit() # LOG: INFO

            return True
        except:
            con.rollback() # LOG: DEBUG

            return False
        finally:
            con.close()
