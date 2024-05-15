class Ability:
    def __init__(self):
        pass
        
    def affectAll(self, tileArray):
        for tile in tileArray:
            tile

    def frontToBack(self, tileArray, hpChange, atkChange, affectedCreatures):
        i = 0
        given = 0
        while i < 5 and given < affectedCreatures:
            if tileArray[i].content != None:
                tileArray[i].content["hp"] += hpChange
                tileArray[i].content["atk"] += atkChange
                given += 1
            i += 1

    def startOrEnd(self, tileArray, gameStage):
        if gameStage == 3 or gameStage > 6:
            self.goldToSteal = 0
            for tile in tileArray:
                if tile.content != None:

                    if gameStage == 3:  # start of battle
                        match tile.content["type"]:
                            case "ogre":
                                atkIncrease = 0
                                for emptyCheck in tileArray:
                                    if emptyCheck.content == None:
                                        atkIncrease += 1
                                atkIncrease * tile.content["lvl"] * 2
                                print(atkIncrease)
                                tile.content["atk"] += atkIncrease

                    elif gameStage > 6:   # end of battle
                        match tile.content["type"]:
                            case "goblin":
                                self.goldToSteal += tile.content["lvl"]
                            case "bigfoot":
                                tile.content["hp"] += tile.content["lvl"]
                            case "yeti":
                                tile.content["atk"] += tile.content["lvl"]

    def sell(self, tileArray, creature):
        if creature != None:
            self.freeRolls = 0
            match creature["type"]:
                case "gnome":
                    self.freeRolls = 1 * creature["lvl"]
                case "pig":
                    self.frontToBack(tileArray, 1, 0, creature["lvl"])
                case "unicorn":
                    self.frontToBack(tileArray, 0, 1, creature["lvl"])

    def buy(self, tileArray, creature):
        pass

    def death(self, tileArray, creature):
        match creature["type"]:
            case "gingerbread":
                self.frontToBack(tileArray, creature["lvl"], creature["lvl"], 2)
                creature["hp"] -= creature["lvl"]
                creature["atk"] -= creature["lvl"]
            case "bomb":
                pass

    def kill(self, tileArray, creature):
        match creature["type"]:
            case "trex":
                pass