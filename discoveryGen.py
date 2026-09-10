import psycopg2
from config import config
from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)

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
        ,0: (2,Weapon)
        ,1: (1,Armor)
        ,2: (5,Consumable)
        ,3: (2,Misc)
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
        # print(f'\ntotalProb: {totalProb}')
        # print(f"SEED: {seed}, probtable: {probTable}")

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
                        
                        # self.printDiscovery(probTable[key][1],probTable['name'])
                        self.fetchDiscovery(key,probTable['name'])
                        return key,probTable['name']
                    else:
                        pass
                    
            return "result?"
            
        return (f"Empty prob table: {probTable}")
    def printDiscovery(self,discovery,table):
        print(f"FUNC printDiscovery() -- discovery: {discovery}, table: {table}")
        if discovery == "nothing....... better luck next time":
            print("CONGRATULATIONS on finding nothing :)")
        else:
            print(f"CONGRATS! You've found {discovery}! I'll grab info from the {table} table")
        return (f"CONGRATS! You've found {discovery}, I'll grab info from the {table} table")
    def fetchDiscovery(self,discoveryID,discoveryTable):
        logger.info(f'fetchDiscovery({discoveryID},{discoveryTable})')
        # print(f"FUNC fetchDiscovery() -- discoveryID: {discoveryID}, discoveryTable: {discoveryTable}")
        conn = None
        selectDiscovery = None
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
            # print(f"fetch: {selectDiscovery}")
            return selectDiscovery
        



class DiscoveryInstance(ABC):
    pass

class DiscoveryWeapon(DiscoveryInstance):
    id = -1
    title = ""
    description = ""
    category = ""
    damageType = ""
    value = None
    damage = ""
    toHit = None

    def __init__(self,infoList):
        # logger.info(f'DiscoveryWeapon({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.category = infoList[3]
        self.damageType = infoList[4]
        self.value = infoList[5]
        self.damage = infoList[6]
        self.toHit = infoList[7]
    

class DiscoveryArmor(DiscoveryInstance):
    id = -1
    title = ""
    description = ""
    category = ""
    bodySlot = ""
    value = -1
    acVal = -1
    dexBonusMax = -1
    strReq = -1
    stealthDisadvantage = False
    statBonus = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryArmor({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.category = infoList[3]
        self.bodySlot = infoList[4]
        self.value = infoList[5]
        self.acVal = infoList[6]
        self.dexBonusMax = infoList[7]
        self.strReq = infoList[8]
        self.stealthDisadvantage = infoList[9]
        self.statBonus = infoList[10]

class DiscoveryConsumable(DiscoveryInstance):
    id = -1
    title = ""
    description = ""
    category = ""
    value = -1
    damage = ""
    heal = ""
    status = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryConsumable({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.category = infoList[3]
        self.value = infoList[4]
        self.damage = infoList[5]
        self.heal = infoList[6]
        self.status = infoList[7]

class DiscoveryEncounter(DiscoveryInstance):
    id = -1
    name = ""
    description = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryEncounter({DiscoveryInstance})')
        self.id = infoList[0]
        self.name = infoList[1]
        self.description = infoList[2]
    pass


class DiscoveryMisc(DiscoveryInstance):
    id = -1
    title = ""
    description = ""
    value = -1

    def __init__(self,infoList):
        # logger.info(f'DiscoveryMisc({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.value = infoList[3]


class DiscoveryQuest(DiscoveryInstance):
    id = -1
    title = ""
    description = ""
    goal = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryQuest({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.goal = infoList[3]

class PlayerInventory:
    def addToInventory(self,table,itemID):
        pass
    def removeFromInventory(self,table,itemID):
        pass

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
