'''
Created on Sep 10, 2017

@author: Pavan Aleti
'''

import pymysql

class Database:
    def connect(self):
        #inserir tracing
        return pymysql.connect("phonebook-mysql","dev","dev","crud_flask" )

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()
        #inserir logging info
        try:
            if id == None:
                cursor.execute("SELECT * FROM phone_book order by name asc")
            else:
                cursor.execute("SELECT * FROM phone_book where id = %s order by name asc", (id,))

            return cursor.fetchall()
        except:
            #inserir logging error
            return ()
        finally:
            con.close()

    def insert(self,data):
        #inserir tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO phone_book(name,phone,address) VALUES(%s, %s, %s)", (data['name'],data['phone'],data['address'],))
            con.commit()

            return True
        except:
            con.rollback()
            #inserir logging.error
            return False
        finally:
            con.close()

    def update(self, id, data):
        #inserir tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s", (data['name'],data['phone'],data['address'],id,))
            con.commit()

            return True
        except:
            #inserir logging error
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        #inserir tracing
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            #inserir logging error
            con.rollback()

            return False
        finally:
            con.close()
