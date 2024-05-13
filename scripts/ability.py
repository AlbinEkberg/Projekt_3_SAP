class Ability:
    def __init__(self, screen):
        self.screen = screen
        
    def affectAll(self, tileArray):
        for tile in tileArray:
            tile

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
                                atkIncrease * tile.content["lvl"]
                                print(atkIncrease)
                                tile.content["atk"] += atkIncrease

                    elif gameStage > 6:   # end of battle
                        match tile.content["type"]:
                            case "goblin":
                                self.goldToSteal += tile.content["lvl"]
                            case "unicorn":
                                tile.content["hp"] += tile.content["lvl"]

    def sell(self, tileArray, creature):
        if creature != None:
            self.freeRolls = 0
            match creature["type"]:
                case "gnome":
                    self.freeRolls = 1 * creature["lvl"]

    def buy(self, tileArray, creature):
        pass

    def death(self, tileArray, creature):
        match creature["type"]:
            case "gingerbread":
                pass

    def kill(self, tileArray, creature):
        match creature["type"]:
            case "trex":
                pass