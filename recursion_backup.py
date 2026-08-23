

class discovery:
    quest_map = {
        0:  (1,"a QUEST! You must Kill 10 monsters")
        ,1: (1,"a QUEST! You must kill 1 monster in 1 hit")
    }
    encounter_map = {
        0:  (1,"an ENCOUNTER!")
    }
    weapon_map = {
        0:  (1,"a Wooden Sword")
        ,1: (1,"a Wooden Axe")
        ,2: (1,"a Shoestring Bow")
        ,3: (1,"a Practice Bow")
        ,4: (1,"a Wooden Club")
    }
    armor_map = {
        0:  (1,"a Padded Armor")
        ,1: (1,"a Leather Armor")
        ,2: (1,"a Studded Leather Armor")
        ,3: (1,"a Hide Armor")
        ,4: (1,"a Padded Helmet")
    }
    misc_item_map = {
        0:  (1,"a Cool Rock")
        ,1: (1,"a Normal Rock")
        ,2: (1,"an Actively Un-cool Rock")
    }
    consumable_map = {
        0:  (1,"a Minor Healing Potion")
        ,1: (1,"a Gunpowder Bomb")
        ,2: (1,"a Molotov Cocktail")
    }
    item_map = {
        0:  (10,weapon_map)
        ,1: (1,armor_map)
        ,2: (1,consumable_map)
        ,3: (1,misc_item_map)
    }

    discTable = {
        0:  (1,quest_map)
        ,1: (1,'nothing....... better luck next time')
        ,2: (1,encounter_map)
        ,3: (1,item_map)
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
            totalProb += val[0]
        seed = (abs(hash(seed_input))%(totalProb))
        # print(f'\ntotalProb: {totalProb}')
        # print(f"SEED: {seed}, probtable: {probTable}")

        seedTicker = seed
        if totalProb >= 0:
            for key,val in probTable.items():
                # print(f"seedTicker -= val[0] --> {seedTicker} - {val[0]}")
                seedTicker -= val[0]
                
                if seedTicker < 0:
                    if type(probTable[key][1]) == dict: #needing to dig deeper
                        # print("Digging deeper")
                        return self.generateTable(seed_input,(probTable[key][1]))
                    # print("Found it")
                    #found it
                    self.printDiscovery(probTable[key][1])
                    return probTable[key][1]
                else:
                    pass
                    
            return "result?"
            
        return (f"Empty prob table: {probTable}")
    def printDiscovery(self,discovery):
        print(f"CONGRATS! You've found {discovery}")
    def fetchDiscovery(self,discoveryID,discoveryTable):
        pass


gen = discovery()
gen.generateTable('12341234')








# quest_map = {
#     0: (1,"quest.0")
#     ,1: (1,"quest.2")
# }
# encounter_map = {
#     0: (1,"ADD ENCOUNTERS TO encounter_map")
# }
# weapon_map = {
#     0: (1,"Wooden Sword")
#     ,1: (1,"Wooden Axe")
#     ,2: (1,"Shoestring Bow")
#     ,3: (1,"Practice Bow")
#     ,4: (1,"Wooden Club")
# }
# armor_map = {
#     0: (1,"Padded Armor")
#     ,1: (1,"Leather Armor")
#     ,2: (1,"Studded Leather Armor")
#     ,3: (1,"Hide Armor")
#     ,4: (1,"Padded Helmet")
# }
# misc_item_map = {
#     0: (1,"Cool Rock")
#     ,1: (1,"Normal Rock")
#     ,2: (1,"Actively Un-cool Rock")
# }
# consumable_map = {
#     0: (1,"Minor Healing Potion")
#     ,1: (1,"Gunpowder Bomb")
#     ,2: (1,"Molotov Cocktail")
# }
# item_map = {
#     0:  (10,weapon_map)
#     ,1: (1,armor_map)
#     ,2: (1,consumable_map)
#     ,3: (1,misc_item_map)
# }

# discTable = {
# 0: (1,quest_map)
# ,1: (1,'nothing')
# ,2: (1,encounter_map)
# ,3: (1,item_map)
# }

# testing = generateTable("12341234",discTable)
# print(testing)
