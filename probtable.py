from abc import ABC, abstractmethod
import hashlib


class ProbTable(ABC):
    # loot
    # loot odds
    # 
    @abstractmethod
    def generateTable(self,seed):
        print("ProbTable: generateTable()")
        pass
    @abstractmethod
    def generateDiscovery(self,seed):
        print("ProbTable: generateDiscovery()")
        pass

class DiscoveryProbTable(ProbTable):
    # options
    # odds

    probTable = {
    0:  'quest'
    ,39: 'nothing'
    ,45: 'encounter'
    ,66: 'item'
    }

    def generateTable(self,seed_input):
        seed = abs(hash(seed_input))%(list(self.probTable.keys())[-1]+1)
        if seed == 0:
            print("QuestProbTable(self,seed)")
        elif seed <= 39:
            print("nothing?!?!?")
        elif seed <= 45:
            print("EncounterProbTable(self,seed)")
        elif seed <= 66:
            print("ItemProbTable(self,seed)")
            ipt = ItemProbTable(seed)
            
            print(ipt)
        else:
            print("MOD FUNCTION in DiscoveryProbTable.generateTable() NOT IMPLEMENTED PROPERLY")
        print(f"SEED INPUT: {seed_input}, SEED: {seed}")


        print("DiscoveryProbTable: generateTable()")
        pass
    def generateDiscovery(self,seed):
        print("DiscoveryProbTable: generateDiscovery()")
        pass

class ItemProbTable(DiscoveryProbTable):
    probTable = {
        0:  '1'
        ,39: '2'
        ,45: '3'
        ,66: '4'
    }
    def __init__(self,seed):
        super().__init__()
        seed = abs(hash(seed))%(list(self.probTable.keys())[-1]+1)
        for key,val in self.probTable.items():
            if seed <= key:
                print(val)

    def generateTable(self,seed):
        seed = abs(hash(seed))%(list(self.probTable.keys())[-1]+1)
        for key,val in self.probTable.items():
            if seed <= key:
                print(val)



        print("DiscoveryProbTable: generateTable()")
        pass
    def generateDiscovery(self,seed):
        print("DiscoveryProbTable: generateDiscovery()")
        pass




def get_from_prob_table(probTable, key):
    seed = key%(list(probTable.keys())[-1]+1)
    for each in range(0,(len(probTable))):
        if seed <= list(probTable.keys())[each]:
            mapped_encoding = probTable.get(key%list(probTable.keys())[each])
            # result = mapped_encoding(key) # should i call function or create object?
            if callable(mapped_encoding):
                print("CALLABLE")
                result = get_from_prob_table(mapped_encoding,abs(hash(key))) # should i call function or create object?
            else:
                print("ELSE")
                result = mapped_encoding
            return result
    return False



probTable_discCat_str = {
    0:  'probTable_quest'
    ,39: 'nothing'
    ,45: 'probTable_encounter'
    ,66: 'probTable_item'
}
"""
probTable_discCat = {
    0:  probTable_quest
    ,39: 'nothing'
    ,45: probTable_encounter
    ,66: probTable_item
}




probTable_quest = {
    10: probTable_quest_find
    ,50: probTable_quest_kill
}"""
probTable_encounter = {
    10: "easy"
    ,50: "test"
}
probTable_item = {
    10: "easy"
    ,50: "test"
}


def nothing():
    print("NOTHING")

class DiscoveryCategoryTable(ProbTable): # Singleton Pattern
    instance = None
    # disc_cat_table = ({
    #     0:  quest
    #    ,39: nothing
    #    ,45: encounter
    #    ,66: item
    # })
    def __init__(self):
        super().__init__()

    def get_disccat(self,barcode):
        seed = barcode%(self.disc_cat_table.keys()[-1]+1)
        for each in range(0,(len(self.disc_cat_table))):
            if seed < self.disc_cat_table[each]:
                mapped_encoding = self.disc_cat_table.get(barcode%self.disc_cat_table.keys()[each])
                result = mapped_encoding(barcode) # should i call function or create object?
                return result
        return False
        


    def __new__(cls,barcode):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    

class DiscoveryTable_Quest(ProbTable):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def generateTable(self):
        pass
    def generateDiscovery(self):
        pass
class DiscoveryTable_Encounter(ProbTable):
    def generateTable(self):
        pass
    def generateDiscovery(self):
        pass
    
class DiscoveryTable_Item(ProbTable):
    def generateTable(self):
        pass
    def generateDiscovery(self):
        pass

class Discovery():
    # test
    def foo(self):
        pass



def test():
    #print(get_from_prob_table(probTable_discCat_str,3781855356463334020))
    dpt = DiscoveryProbTable()
    dpt.generateTable('12341234')
    pass


if __name__ == '__main__':
    test()