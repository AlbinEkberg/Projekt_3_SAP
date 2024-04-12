from scripts.tileCreator import TileCreator
from scripts.rollButton import RollButton
from scripts.creature import Creature

class TileMap:
    def __init__(self, screen):
        # always places the boxes along the edges regardless of screen resolution
        self.screen = screen
        self.boxsizeWithMargin = int((self.screen.get_width() * 0.14) + 10)

        self.playerTile1 = TileCreator(10, 10, screen)
        self.playerTile2 = TileCreator(self.boxsizeWithMargin + 10, 10, screen)
        self.playerTile3 = TileCreator(2 * self.boxsizeWithMargin + 10, 10, screen)
        self.playerTile4 = TileCreator(3 * self.boxsizeWithMargin + 10, 10, screen)
        self.playerTile5 = TileCreator(4 * self.boxsizeWithMargin + 10, 10, screen)

        self.shopTile1 = TileCreator(10, int(self.screen.get_height() - self.boxsizeWithMargin), screen)
        self.shopTile2 = TileCreator(self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen)
        self.shopTile3 = TileCreator(2 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen)
        self.shopTile4 = TileCreator(3 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen)

    def displayTiles(self):
        self.playerTile1.blitTile(self.playerTile1.content['img'])
        self.playerTile2.blitTile(self.playerTile2.content['img'])
        self.playerTile3.blitTile(self.playerTile3.content['img'])
        self.playerTile4.blitTile(self.playerTile4.content['img'])
        self.playerTile5.blitTile(self.playerTile5.content['img'])

        self.shopTile1.blitTile(self.shopTile1.content['img'])
        self.shopTile2.blitTile(self.shopTile2.content['img'])
        self.shopTile3.blitTile(self.shopTile3.content['img'])
        self.shopTile4.blitTile(self.shopTile4.content['img'])

    def updateShop(self):
        self.shopTile1.content = Creature.generateCreature()
        self.shopTile2.content = Creature.generateCreature()
        self.shopTile3.content = Creature.generateCreature()
        self.shopTile4.content = Creature.generateCreature()
        print(self.shopTile4.content['img'])