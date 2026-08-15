import psycopg2
from config import config

def connect():
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

        create_scripts = (''' CREATE TABLE IF NOT EXISTS Inventory2 (
                                id int PRIMARY KEY,
                                itemID int,
                                title varchar(255),
                                description varchar(255),
                                count int) ''',
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
        )
        # cur.execute(create_script)

        for create_script in create_scripts:
            cur.execute(create_script)



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