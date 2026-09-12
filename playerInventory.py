import psycopg2
from config import config
from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)

class PlayerInventory:
    instance = None
    uniqueItemCount = -1
    inventory = {}

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def fetchInventoryDetail(self):
        select_script = "SELECT * FROM playerInventory"
        sql = """
        SELECT pi.id, i.tablename, pi.count, pi.equipped FROM playerInventory pi
        LEFT JOIN item i ON pi.itemID i.id

        SELECT
        pi.id
        , CASE 
            WHEN pi.itemID = 0 THEN w.title
            WHEN pi.itemID = 1 THEN a.title
            WHEN pi.itemID = 2 THEN c.title
            WHEN pi.itemID = 3 THEN m.title
            else NULL
        END AS title
        , i.tablename
        , pi.count
        , pi.equipped
        FROM playerInventory pi
        LEFT JOIN item i ON pi.itemID = i.id
        LEFT JOIN weapon w ON w.id = pi.itemDetailID
        LEFT JOIN armor a ON a.id = pi.itemDetailID
        LEFT JOIN consumable c ON c.id = pi.itemDetailID
        LEFT JOIN misc m ON .id = pi.itemDetailID
        """
        item_table = "SELECT * FROM {} WHERE id = {}"
        pI = {}
        self.inventory = {}
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

    def fetchInventory(self):
        select_script = """
        SELECT
        pi.id
        , CASE 
            WHEN pi.itemID = 0 THEN w.title
            WHEN pi.itemID = 1 THEN a.title
            WHEN pi.itemID = 2 THEN c.title
            WHEN pi.itemID = 3 THEN m.title
            else NULL
        END AS title
        , i.tablename
        , pi.count
        , pi.equipped
        FROM playerInventory pi
        LEFT JOIN item i ON pi.itemID = i.id
        LEFT JOIN weapon w ON w.id = pi.itemDetailID
        LEFT JOIN armor a ON a.id = pi.itemDetailID
        LEFT JOIN consumable c ON c.id = pi.itemDetailID
        LEFT JOIN misc m ON m.id = pi.itemDetailID
        """
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
