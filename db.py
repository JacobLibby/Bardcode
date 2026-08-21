import psycopg2
from config import config
import os
import pandas as pd
import csv

def connect():
    create_script_index = 0
    create_script_arr = []
    conn = None
    try:
        params = config()
        print('Connecting to PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version: ')
        for file in os.listdir('CreateTable_CSVs'):

            header = 0
            key = ""
            primary_keys = []
            foreign_keys = []
            create_script_exists = False
            insert_script_exists = False
            create_script = "CREATE TABLE IF NOT EXISTS " + str(file).replace("CreateTable_","").replace(".csv","")
            insert_script = "INSERT INTO " + str(file).replace("CreateTable_","").replace(".csv","")
            filename = "CreateTable_CSVs\\" + file
            with open(filename) as csv_file:
                reader = csv.reader(csv_file,delimiter=',',quotechar='"')
                for row in reader:
                    create_script_exists = True
                    row_arr = []
                    if header == 0:
                        header = 1

                        for eachind in range(0,len(row)):
                            if (row[eachind].split(" ")[0]).startswith("__"):
                                foreign_keys.append(row[eachind].split(" ")[0].split("__")[1])
                            elif (row[eachind].split(" ")[0]).startswith("_"):
                                primary_keys.append(row[eachind].split(" ")[0].split("_")[1])
                            else: #column is not a primary key or a foreign key
                                pass
                            row[eachind] = row[eachind].strip("_")
                            
                        create_script += " (" + ','.join(row)
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
                if primary_keys:
                
                    create_script += (f", PRIMARY KEY ({','.join(primary_keys)}));")
                elif foreign_keys:
                    create_script += (f", UNIQUE({','.join(foreign_keys)}));")
                else:
                    create_script += ");"
                    print("NO KEYS IN THIS TABLE AT ALL")
                print(create_script)
                cur.execute(create_script)
                conn.commit()
            if insert_script_exists:
                insert_script = insert_script.replace('`',"'")
                print(insert_script)
                cur.execute(insert_script)
                conn.commit()

        cur.execute('SELECT * FROM Weapon WHERE id > 1;')
        select_test = []
        # db_version = cur.fetchall()
        select_test = cur.fetchall()
        print(select_test)
        # cur.execute('SELECT 12;')
        apple = []
        # apple = cur.fetchall()
        # print(apple)
        cur.close()
        print("Cursor closed.")
    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection terminated.')
    print("Done.")



    return False #STOP running code, testing CreateTable_CSVs
    conn = None
    try:
        params = config()
        print('Connecting to PostgreSQL database')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        print('PostgreSQL database version: ')
        # cur.execute('SELECT version()')
        # db_version = cur.fetchone()
        # print(db_version)

        # create_script = '''SELECT 31'''

        create_scripts = (      '''CREATE TABLE IF NOT EXISTS Inventory2 (
                                    id int PRIMARY KEY,
                                    itemID int,
                                    title varchar(255),
                                    description varchar(255),
                                    count int
                                ) ''',
                                '''CREATE TABLE IF NOT EXISTS NPCs (
                                    id int PRIMARY KEY)''',
                                '''CREATE TABLE IF NOT EXISTS Encounter (
                                    id int PRIMARY KEY,
                                    npcID int,
                                    npcIDs varchar(1000),
                                    name varchar(255),
                                    description varchar (510),
                                    CONSTRAINT npcID_FK
                                    FOREIGN KEY (npcID)
                                    REFERENCES NPCs(id)
                                )'''
                        
 
        ) # should I not be storing floats? !!!
        # cur.execute(create_script)

        for create_script in create_scripts:
            cur.execute(create_script)


        for filename in os.listdir('CreateTable_CSVs'):
            print(f"Filename: {filename}")
        
            
        # cur_create = conn.cursor()
        # cur_create.execute("CREATE TABLE test1(" \
        # "id int, " \
        # "col2 int, " \
        # "PRIMARY KEY (id));")
        # cur_create_fetch = cur_create.fetchall()
        # print(cur_create_fetch)

        # cur_select = conn.cursor()
        # cur_select.execute("SELECT * FROM test1")
        # cur_select_fetch = cur_select.fetchall()
        # print(cur_select_fetch)
        conn.commit()
        # cur_create = conn.cursor()
        # cur_create.execute("CREATE TABLE test1(" \
        # "id int, " \
        # "col2 int, " \
        # "PRIMARY KEY (id));")
        # cur_create_fetch = cur_create.fetchall()
        # print(cur_create_fetch)
        cur.close()
        

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection terminated.')

if __name__ == "__main__":
    connect()