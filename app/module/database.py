'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    def connect(self):
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    # Inclusão de logging de INFO.
    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        # Inclusão de logging de INFO.
        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()

        # Inclusão de logging CRITICAL / FATAL.
        except:
            return ()

        # Inclusão de logging de INFO.
        finally:
            con.close()

    # Inclusão de logging de INFO.
    def insert(self,data):
        con = Database.connect(self)
        cursor = con.cursor()

        # Inclusão de logging de INFO.
        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            return True
            
        # Inclusão de logging CRITICAL / FATAL.
        except:
            con.rollback()

            return False
            
        # Inclusão de logging de INFO.
        finally:
            con.close()

    # Inclusão de logging de INFO.
    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        # Inclusão de logging de INFO.
        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
            
        # Inclusão de logging CRITICAL / FATAL.
        except:
            con.rollback()

            return False
        
        # Inclusão de logging de INFO.
        finally:
            con.close()

    # Inclusão de logging de INFO.
    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        # Inclusão de logging de INFO.
        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True

         # Inclusão de logging CRITICAL / FATAL.
        except:
            con.rollback()

            return False

        # Inclusão de logging de INFO.
        finally:
            con.close()
