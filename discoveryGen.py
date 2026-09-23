import psycopg2
from config import config
from abc import ABC, abstractmethod
import logging
logger = logging.getLogger(__name__)
import playerInventory

class discovery:
    quest = {
        "name": "quest"
        ,'6ddedb89f6a1a2741b70ada74ba100d345310de3f50fb387590cbbe3c0d12aae': (1,"KILL KILL KILL")
        ,'473fc7cff56505f60f49479154f7bd172bd7dfe05d0ca4d915b0c8e51c1dc798': (1,"You''re RICH! .....for an amoeba")
        ,'2e1cbda90b2636f4fdfd16261ab8ccb1233f174cd72f32144bce53aeb331381e': (1,"We had a good run")
    }
    encounter = {
        "name": "encounter"
        ,'3cc645231b061098c09adbdfeb98980697421d10070d074df5301af7c6887153': (1, 'Humble Shopkeep')
        ,'a17eec10480e6eedae33cd675e5fdf40b7c1bdacd9eddebff8574fb1784e924c': (1, 'Potion Seller')
    }
    weapon = {
        "name": "weapon"
        ,'f39bc858dd349745fa035664d0c63cea28d00937caaf8ab93ffb32b75973d974': (1, "a Wooden Sword")
        ,'0dad16b82c9c0e85d5e3bcbbef61ed013d30c9667b14a0981896faf66cfd7f18': (1, "a Wooden Axe")
        ,'a62a4aed9d38c9268ef877baf39addc378106c4b9208291e66614d7a4dfbd8da': (1, "a Shoestring Bow")
        ,'7eb4e2866c9dfd71ef78ff533049ad511c649924d16e9d16f98da5a0c0f07cdb': (1, "a Practice Bow")
        ,'f29fc08aa4313fb70bfc52d461b8e2e6eed1782cb9d8b84c764455a5da616bd9': (1, "a Wooden Club")
        ,'13995abb6fa6d0ace8215bd235c3ae2117171d139ae55c26c772ca09a5fa9031': (1, "Iron Sword")
        ,'f5ff83b2eb20678a35dd0457333bb0f30b1ffac4c7b0eb87b58d702b4248bfd9': (1, "Iron Axe")
        ,'e19b5d2c604425aace9ac16a35165c2d02b6db591f1c452381e71d0407eef430': (1, "Spiked Club")
        ,'94737ed7a8bcdfea5710f5ee2c7014d7e58c888caab6aae216aacd60bcdb4222': (1, "Stick")

    }
    armor = {
        "name": "armor"
        ,'8ebd2fb9c3e8de71906500275f2b1a74a953e40a14e4a9a3e6ec8cf00e4d309f': (1,"a Padded Armor")
        ,'c0630e1c5a22d72dd9d1fab565a4df720fa95223613f74f0e23b5448d42bd212': (1,"a Leather Armor")
        ,'8c895bc8e01e925c4f5a6a039d749e1e7741649c133ddf3d015ebf8c6dcc3694': (1,"a Studded Leather Armor")
        ,'eaf9268749eeb31f211bff0c242b01c8298e7ee18f6b23bc465df75ff3097cef': (1,"a Hide Armor")
        ,'e2c908a912f233412a13a8d0840fcc43f90c0dfe4fb5e464982d0fbfb2190337': (1,"a Padded Helmet")
    }
    consumable = {
        "name": "consumable"
        ,'05072d07d2964cb2daf2ca5d88bc6e32780b444745af946ac99ead505fe37aa5': (1,"a Minor Healing Potion")
        ,'3b603038d196da75d15aaf73a1b105e63e5dc75a8b4272088f1b71246012efaf': (1,"a Gunpowder Bomb")
        ,'d292e8e04a260ebadc309c0617da61894350c39ae28cb945c23f77dc446b16a3': (1,"a Molotov Cocktail")
    }
    misc = {
        "name": "misc"
        ,'b5328d80569c6948118af71010f75be79bc799c087d74f6ea6d1f253c1ff6390': (1,"a Cool Rock")
        ,'49e5fa467f862c14356a7fa1bd38b32b61bb919729dc574e100b7e5420ce7e52': (1,"a Normal Rock")
        ,'0f2865ed0cc1daa68b03955df8e921660364dbacef3b74c249f6838cb77bc6dd': (1,"an Actively Un-cool Rock")
    }
    item = {
        "name": "item"
        ,'d56ef73153d98add091bfb2d51f0a0947e86af70a74c5ebea46c273f039fc5b3': (2,weapon)
        ,'0b3c88385e7ab701236d9e7e1bb8974a4cdd315bcd5cee13d2957cc28c8d74d3': (1,armor)
        ,'bccdab060fd35ba292271c9d10ef5aecdebce64defb1cbbdac3c5b566539fd42': (5,consumable)
        ,'484f5b5a0173e7d27d10ffd160e8a5423ad2583d035af7d9287716efa285dff3': (2,misc)
    }

    discTable = {
        "name": "discovery"
        ,0: (1,'nothing....... better luck next time')
        ,1000: (1,quest)
        ,3000: (1,encounter)
        ,6000: (10,item)
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
            if type(val) == tuple:
                # print(f"key: {key}, val: {val}")
                totalProb += val[0]
        # print(str(probTable.items()) + '\n')
        seed = (abs(hash(seed_input))%(totalProb))

        seedTicker = seed
        if totalProb >= 0:
            for key,val in probTable.items():
               if type(val) == tuple:
                    seedTicker -= val[0]
                            
                    if seedTicker < 0:
                        if type(probTable[key][1]) == dict: #needing to dig deeper
                            # print("Digging deeper")
                            return self.generateTable(seed_input,(probTable[key][1]))
                        # print("Found it")
                        #found it
                        
                        self.fetchDiscovery(key,probTable['name'])
                        if probTable['name'] in ('weapon','armor','consumable','misc'):
                            # print(f"++++++++++++discoveryGent.discovery.generateTable()")
                            pI = playerInventory.PlayerInventory()
                            pI.addToInventory(key,probTable['name'])
                        # print(f"print(key, probTable['name']) --> {key, probTable['name']}")
                        return key,probTable['name']
                    
                    
            return "result?", "result?2"
            
        return (f"Empty prob table: {probTable}")
    def printDiscovery(self,discovery,table):
        # print(f"FUNC printDiscovery() -- discovery: {discovery}, table: {table}")
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
            WHERE id = '{discoveryID}'
            """
            # print(f"=======fetchDiscovery..selectScript: {selectScript}")
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
    id = ""
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
    id = ""
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
    id = ""
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
    id = ""
    name = ""
    description = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryEncounter({DiscoveryInstance})')
        self.id = infoList[0]
        self.name = infoList[1]
        self.description = infoList[2]
    pass


class DiscoveryMisc(DiscoveryInstance):
    id = ""
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
    id = ""
    title = ""
    description = ""
    goal = ""

    def __init__(self,infoList):
        # logger.info(f'DiscoveryQuest({DiscoveryInstance})')
        self.id = infoList[0]
        self.title = infoList[1]
        self.description = infoList[2]
        self.goal = infoList[3]


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
