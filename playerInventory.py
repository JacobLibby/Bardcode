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

    # def fetchInventoryDetail(self):
        # select_script = """
        # SELECT
        # pi.id
        # , CASE 
        #     WHEN pi.itemCat = 'Weapon' THEN w.title
        #     WHEN pi.itemCat = 'Armor' THEN a.title
        #     WHEN pi.itemCat = 'Consumable' THEN c.title
        #     WHEN pi.itemCat = 'Misc' THEN m.title
        #     else NULL
        # END AS title
        # , i.tablename
        # , pi.count
        # , pi.equipped
        # FROM playerInventory pi
        # LEFT JOIN item i ON i.id = pi.itemID
        # LEFT JOIN weapon w ON w.id = pi.itemID
        # LEFT JOIN armor a ON a.id = pi.itemID
        # LEFT JOIN consumable c ON c.id = pi.itemID
        # LEFT JOIN misc m ON m.id = pi.itemID
        # """
        # select_ret = ""
        # conn = None
        # try:
        #     params = config()
        #     print('Connecting to PostgreSQL database')
        #     conn = psycopg2.connect(**params)
    
        #     # create a cursor
        #     cur = conn.cursor()
        #     print('PostgreSQL database version: ')
        #     cur.execute(select_script)
        #     conn.commit()
        #     select_ret = cur.fetchall()
        #     cur.close()
        #     print("Cursor closed.")
        # except(Exception, psycopg2.DatabaseError) as error:
        #     print(error)
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection terminated.')
        # # print(f"fetched inventory. len={len(select_ret)}")
        # return select_ret

    def fetchInventory(self):
        select_script = """
        SELECT
        pi.id
        , CASE 
            WHEN pi.itemCat = 'weapon' THEN w.title
            WHEN pi.itemCat = 'armor' THEN a.title
            WHEN pi.itemCat = 'consumable' THEN c.title
            WHEN pi.itemCat = 'misc' THEN m.title
            else NULL
        END AS title
        , i.tablename
        , pi.count
        , pi.equipped
        FROM playerInventory pi
        LEFT JOIN item i ON i.tableName = pi.itemCat
        LEFT JOIN weapon w ON w.id = pi.itemID
        LEFT JOIN armor a ON a.id = pi.itemID
        LEFT JOIN consumable c ON c.id = pi.itemID
        LEFT JOIN misc m ON m.id = pi.itemID
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

    def getTableCols(self,table):
        selectScript = f"""
        SELECT column_name
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table}'

        """
        print(f"*******table: {table}")
        print(f"*******select_script: {selectScript}")
        select_ret = []
        ret = ''
        conn = None
        try:
            params = config()
            print('Connecting to PostgreSQL database')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()
            cur.execute(selectScript)

            # conn.commit()
            select_ret = cur.fetchall()
            cur.close()
            print("Cursor closed.")
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"playerInventory.addToInventory --> {error}")
        finally:
            if conn is not None:
                conn.close()
                print('Database connection terminated.')
        print(f"***select_ret: {select_ret}")
        for each in select_ret:
            ret += str(each[0]) + ','
        ret = ret[:-1]
        print(ret)
        return ret, select_ret
    

    def addToInventory(self,itemID,table):
        tableCols, tableColsArr = self.getTableCols(table)
        if len(tableColsArr) < 3:
            # can't normally create new ID w hash
            pass
            
        # insertScript = """
        # INSERT INTO {table}


        # """
        # conn = None
        # try:
        #     params = config()
        #     print('Connecting to PostgreSQL database')
        #     conn = psycopg2.connect(**params)

        #     # create a cursor
        #     cur = conn.cursor()
        #     cur.execute(insertScript)

        #     conn.commit()
        #     select_ret = cur.fetchall()
        #     cur.close()
        #     print("Cursor closed.")
        # except(Exception, psycopg2.DatabaseError) as error:
        #     print(f"playerInventory.addToInventory --> {error}")
        # finally:
        #     if conn is not None:
        #         conn.close()
        #         print('Database connection terminated.')
        # return select_ret

    def removeFromInventory(self,table,itemID):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
