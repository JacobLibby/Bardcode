from abc import ABC, abstractmethod

class ProbTable(ABC):
    # loot
    # loot odds
    # 
    @abstractmethod
    def generateTable(self):
        print("DiscoveryTable: generateTable()")
        pass
    @abstractmethod
    def generateDiscovery(self):
        print("DiscoveryTable: generateDiscovery()")
        pass


def get_from_prob_table(probTable, key):
    seed = key%(probTable()[-1]+1)
    for each in range(0,(len(probTable))):
        if seed <= probTable[each]:
            mapped_encoding = probTable.get(key%probTable()[each])
            # result = mapped_encoding(key) # should i call function or create object?
            if callable(mapped_encoding):
                result = get_from_prob_table(mapped_encoding,key) # should i call function or create object?
            else:
                result = mapped_encoding
            return result
    return False

probTable_discCat = {
    0:  probTable_quest
    ,39: nothing
    ,45: probTable_encounter
    ,66: probTable_item
}

probTable_quest = {
    10: probTable_quest_find
    ,50: probTable_quest_kill
}
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
    disc_cat_table = ({
        0:  quest
       ,39: nothing
       ,45: encounter
       ,66: item
    })
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

    pass


if __name__ == '__main__':
    test()