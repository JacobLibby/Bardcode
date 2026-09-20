import psycopg2
from config import config
from abc import ABC, abstractmethod
import hashlib
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
        """
        if itemID in playerInventory
            increment count by 1 -- later by itemCount?
        else: -- if itemID not in playerInventory
            insert into playerInventory:
                itemID = itemID
                itemCat = table
                id = hash(table, "'" + str(itemID) + "''" + str(itemCat) + "'")
                count = 1
                equipped = False
        """
        tableCols, tableColsArr = self.getTableCols(table)
        piTableCols, piTableColsArr = self.getTableCols('playerinventory')

        if len(tableColsArr) < 3:
            print(f"+++++++len(tableColsArr) < 3")
            # can't normally create new ID w hash
            return False

        # selectScriptHashVals = f"""
        # SELECT {tableColsArr[1][0]},{tableColsArr[2][0]}
        # FROM {table}
        # WHERE id = '{itemID}'
        # """
        selectScriptInventory = f"""
        SELECT *
        FROM PlayerInventory
        WHERE itemID = '{itemID}'
                    """

        conn = None
        try:
            params = config()
            print('Connecting to PostgreSQL database')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()
            cur.execute(selectScriptInventory)
            conn.commit()
            selectScriptInventory_ret = cur.fetchall()

            inventoryScript = ''
            if selectScriptInventory_ret:
                # item is already in inventory --> increment count
                print(f"+++++++INCREMENT COUNT OF ITEM IN INVENTORY")
                inventoryScript = f"""
                UPDATE {'PlayerInventory'}
                SET count = count + 1
                WHERE itemID = '{itemID}'
                """

                pass
            else:
                # item is not in inventory --> add to inventory
                playerInventoryID = hashlib.sha256(bytes('PlayerInventory' + "'" + str(itemID) + "''" + str(table) + "'","utf-8")).hexdigest()
                print(f"++++++++ADD ITEM TO INVENTORY")
                inventoryScript = f"""
                INSERT INTO PlayerInventory 
                VALUES ('{str(playerInventoryID)}','{itemID}','{table}',1,False)
                """
                #({piTableCols})


            print(inventoryScript)
            cur.execute(inventoryScript)
            conn.commit()
            # inventoryScript_ret = cur.fetchall()
            
            cur.close()
            print("Cursor closed.")
            
            hashval =""
            hashID = hashlib.sha256(bytes(table + hashval,"utf-8")).hexdigest()

            # see if already in inventory (then would need to increase count)
            
                
            insertScript = """
            INSERT INTO PlayerInventory ({piTableCols})
            VALUES ({table})


            """

            """ OBJECTIVE: add info to csv and table
            1. add new row to csv
            2. add row to table ()
            """


            
            
        except(Exception, psycopg2.DatabaseError) as error:
            print(f"+++++++++++++++++++++++++++playerInventory.addToInventory --> {error}")
        finally:
            if conn is not None:
                conn.close()
                print('Database connection terminated.')
        return True #select_ret

    def removeFromInventory(self,table,itemID):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
