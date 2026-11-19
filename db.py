import psycopg2
from config import config
import os
import pandas as pd
import csv
import logging
logger = logging.getLogger(__name__)



def drop_if_new_schema():
    #INPUT: 
    #OUTPUT:

    # given filename, lookup table and see if header of file matches table header and datatypes
    pass


def drop_tables(tables_arr):
    try:
        params = config()
        print('Connecting to PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        for table in tables_arr:
            drop_script = "DROP TABLE IF EXISTS " + str(table) + ";"
            
            cur.execute(drop_script)
            print(f"TABLE {table} SUCCESSFULLY DROPPED")
            conn.commit()

        cur.close()

    except psycopg2.Error as e:
        print(f"Error dropping table: {e}")
        conn.rollback()
    finally:
        cur.close()
        if conn is not None:
            conn.close()
            print('Database connection terminated.')
    print("Done.")


def connect(file_dir):
    create_script_arr = []
    conn = None
    try:
        params = config()
        print('Connecting to PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version: ')
        for file in os.listdir(file_dir):
            if file[-4:] == '.csv':

                header = 0
                primary_keys = []
                foreign_keys = []
                create_script_arr = []
                create_script_exists = False
                insert_script_exists = False
                create_script = "CREATE TABLE IF NOT EXISTS " + str(file).replace("CreateTable_","").replace(".csv","")
                insert_script = "INSERT INTO " + str(file).replace("CreateTable_","").replace(".csv","")
                filename = file_dir + '\\' + file
                with open(filename) as csv_file:
                    reader = csv.reader(csv_file,delimiter='|',quotechar='"')
                    for row in reader:
                        create_script_exists = True
                        
                        row_arr = []
                        if header == 0:
                            header = 1
                            
                            for eachind in range(0,len(row)):
                                if (row[eachind].split(" ")[0]).startswith("__"):
                                    create_script_arr.append(f"{str(row[eachind].split("__")[1])} references {str(row[eachind].split(" ")[0].split("__")[1]).upper().split("ID")[0]}(id)")
                                    foreign_keys.append(f"{str(row[eachind].split(" ")[0].split("__")[1])} references {str(row[eachind].split(" ")[0].split("__")[1]).upper().split("ID")[0]}(id)")
                                elif (row[eachind].split(" ")[0]).startswith("_"):
                                    create_script_arr.append(f"{str(row[eachind].split("_")[1])} primary key")
                                    primary_keys.append(f"{str(row[eachind].split(" ")[0].split("_")[1])} primary key")
                                else: #column is not a primary key or a foreign key
                                    create_script_arr.append(row[eachind])
                                    pass
                                row[eachind] = row[eachind].strip("_")
                                
                            create_script += " (" + ','.join(create_script_arr)
                            for col in row:
                                row_arr.append(col.split(" ")[0])
                            insert_script += " (" + ','.join(row_arr) + ") VALUES " #### row has datatypes, how to remove?
                        else: # maybe delete?
                            insert_script_exists = True
                            for col in row: # maybe delete?
                                row_arr.append(col.replace("`",",")) # maybe delete?
                            if header == 1:
                                header = 2
                                insert_script += "(" + ','.join(row_arr) + ")"
                            else:
                                insert_script += ",(" + ','.join(row_arr) + ")"
                        
                    insert_script += (" ON CONFLICT  DO NOTHING;")
                
                if create_script_exists:
                    create_script += ");"
                    print(create_script)
                    cur.execute(create_script)
                    conn.commit()
                if insert_script_exists:
                    insert_script = insert_script.replace('`',"'")
                    cur.execute(insert_script)
                    conn.commit()


        cur.close()
        print("Cursor closed.")
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection terminated.')
    print("Done.")

    return False


def selectDiscovery(discoveryKey,discoveryTable):

    conn = None
    try:
        params = config()
        print('Connecting to PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version: ')

        cur.execute(f'SELECT * FROM {discoveryTable} WHERE id = {discoveryKey};')
        
        select_test = []
        select_test = cur.fetchall()
        print(select_test)
        cur.close()
        print("Cursor closed.")
    
    except(Exception, psycopg2.DatabaseError) as error:
        print("EXCEPTED")
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection terminated.')
    print("Done.")

    return False #STOP running code, testing CreateTable_CSVs



def main():
    #lilBobby
    print('lil'' bobby drop tables')
    drop_tables(['PlayerInventory'])
    # drop_tables(['encounternpc','monster','npc','playerinventory','scanned','Weapon','Armor','Consumable','discovery','encounter','item','misc','quest'])

    connect('CreateTable_CSVs')
    connect('CreateTable_CSVs\\has_dependencies1')
    connect('CreateTable_CSVs\\has_dependencies2')

if __name__ == "__main__":
    main()
