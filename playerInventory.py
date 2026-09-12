import psycopg2
from config import config
from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)

class PlayerInventory:
    instance = None
    uniqueItemCount = -1

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def fetchInventory(self):
        select_script = "SELECT * FROM playerInventory"
        select_ret = ""
        conn = None
        try:
            params = config()
            print('Connecting to PostgreSQL database')
            conn = psycopg2.connect(**params)
    
            # create a cursor
            cur = conn.cursor()
            print('PostgreSQL database version: ')
            cur.execute(select_script)
            conn.commit()
            select_ret = cur.fetchall()
            cur.close()
            print("Cursor closed.")
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection terminated.')
        # print(f"fetched inventory. len={len(select_ret)}")
        return select_ret

    def addToInventory(self,table,itemID):
        pass

    def removeFromInventory(self,table,itemID):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
