import psycopg2
from config import config


class discovery:
    Quest = {
        "name": "Quest"
        ,0: (1,"a QUEST! You must Kill 10 monsters")
        ,1: (1,"a QUEST! You must kill 1 monster in 1 hit")
    }
    Encounter = {
        "name": "Encounter"
        ,0: (1,"an ENCOUNTER!")
    }
    Weapon = {
        "name": "Weapon"
        ,0: (1,"a Wooden Sword")
        ,1: (1,"a Wooden Axe")
        ,2: (1,"a Shoestring Bow")
        ,3: (1,"a Practice Bow")
        ,4: (1,"a Wooden Club")
    }
    Armor = {
        "name": "Armor"
        ,0: (1,"a Padded Armor")
        ,1: (1,"a Leather Armor")
        ,2: (1,"a Studded Leather Armor")
        ,3: (1,"a Hide Armor")
        ,4: (1,"a Padded Helmet")
    }
    Misc = {
        "name": "Misc"
        ,0: (1,"a Cool Rock")
        ,1: (1,"a Normal Rock")
        ,2: (1,"an Actively Un-cool Rock")
    }
    Consumable = {
        "name": "Consumable"
        ,0: (1,"a Minor Healing Potion")
        ,1: (1,"a Gunpowder Bomb")
        ,2: (1,"a Molotov Cocktail")
    }
    Item = {
        "name": "Item"
        ,0: (1,Weapon)
        ,1: (1,Armor)
        ,2: (1,Consumable)
        ,3: (1,Misc)
    }

    discTable = {
        "name": "Discovery"
        ,0: (1,Quest)
        ,1: (1,'nothing....... better luck next time')
        ,2: (1,Encounter)
        ,3: (10,Item)
    }
    def generateTable(self,seed_input,probTable_input=discTable):
        
        
        # print(f"Called 'generateTable({seed_input},{probTable})'")
        #seed = abs(hash(seed_input))%(list(probTable.keys())[-1]+1)
        """
        for key,val in probTable.items():
            if seed <= key:
                if type(probTable[key]) == dict:
                    print(f"TESTING {probTable[key]}")
                    return generateTable(seed,probTable[key]) # result =
                else:
                    result = probTable[key]
                    
                print(val)
                return result
        """
        ## VV implemented with probability val dicts rather than prob range dicts
        #? How to implement this, keys need to be unique
        probTable = probTable_input
        totalProb = 0
        for key,val in probTable.items():
            if type(key) == int:
                totalProb += val[0]
        seed = (abs(hash(seed_input))%(totalProb))
        print(f'\ntotalProb: {totalProb}')
        print(f"SEED: {seed}, probtable: {probTable}")

        seedTicker = seed
        if totalProb >= 0:
            for key,val in probTable.items():
                # print(f"Key: {key}, Val: {val}")
                # print(f"seedTicker -= val[0] --> {seedTicker} - {val[0]}")
                if type(key) == int:
                    seedTicker -= val[0]
                            
                    if seedTicker < 0:
                        if type(probTable[key][1]) == dict: #needing to dig deeper
                            # print("Digging deeper")
                            return self.generateTable(seed_input,(probTable[key][1]))
                        # print("Found it")
                        #found it
                        self.printDiscovery(probTable[key][1],probTable['name'])
                        self.fetchDiscovery(key,probTable['name'])
                        return probTable[key][1],probTable['name']
                    else:
                        pass
                    
            return "result?"
            
        return (f"Empty prob table: {probTable}")
    def printDiscovery(self,discovery,table):
        if discovery == "nothing....... better luck next time":
            print("CONGRATULATIONS on finding nothing :)")
        else:
            print(f"CONGRATS! You've found {discovery}, I'll grab info from the {table} table")
    def fetchDiscovery(self,discoveryID,discoveryTable):
        conn = None
        try:

            params = config()
            conn = psycopg2.connect(**params)
            # create a cursor
            cur = conn.cursor()
            # cur.execute("SELECT pg_is_in_recovery();")
            # print(cur.fetchall())
            
            selectScript = f"""
            SELECT *
            FROM {discoveryTable}
            WHERE id = {discoveryID}
            """
            cur.execute(selectScript)
            conn.commit()
            selectDiscovery = cur.fetchall()
            cur.close()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection terminated.')
                

def main():
    # gen = discovery()
    # gen.generateTable('12341234')
    pass

if __name__ == '__main__':
    main()


# cur.close()
# conn.close()







# Quest = {
#     0: (1,"quest.0")
#     ,1: (1,"quest.2")
# }
# Encounter = {
#     0: (1,"ADD ENCOUNTERS TO Encounter")
# }
# Weapon = {
#     0: (1,"Wooden Sword")
#     ,1: (1,"Wooden Axe")
#     ,2: (1,"Shoestring Bow")
#     ,3: (1,"Practice Bow")
#     ,4: (1,"Wooden Club")
# }
# Armor = {
#     0: (1,"Padded Armor")
#     ,1: (1,"Leather Armor")
#     ,2: (1,"Studded Leather Armor")
#     ,3: (1,"Hide Armor")
#     ,4: (1,"Padded Helmet")
# }
# Misc = {
#     0: (1,"Cool Rock")
#     ,1: (1,"Normal Rock")
#     ,2: (1,"Actively Un-cool Rock")
# }
# Consumable = {
#     0: (1,"Minor Healing Potion")
#     ,1: (1,"Gunpowder Bomb")
#     ,2: (1,"Molotov Cocktail")
# }
# Item = {
#     0:  (10,Weapon)
#     ,1: (1,Armor)
#     ,2: (1,Consumable)
#     ,3: (1,Misc)
# }

# discTable = {
# 0: (1,Quest)
# ,1: (1,'nothing')
# ,2: (1,Encounter)
# ,3: (1,Item)
# }

# testing = generateTable("12341234",discTable)
# print(testing)
