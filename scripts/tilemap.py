from scripts.tileCreator import TileCreator
from scripts.rollButton import RollButton

class TileMap:
    def __init__(self, screen):
        # always places the boxes along the edges regardless of screen resolution
        self.screen = screen
        boxsizeWithMargin = int((self.screen.get_width() * 0.14) + 10)

        self.playerTile1 = TileCreator(10, 10, screen)
        self.playerTile2 = TileCreator(boxsizeWithMargin + 10, 10, screen)
        self.playerTile3 = TileCreator(2 * boxsizeWithMargin + 10, 10, screen)
        self.playerTile4 = TileCreator(3 * boxsizeWithMargin + 10, 10, screen)
        self.playerTile5 = TileCreator(4 * boxsizeWithMargin + 10, 10, screen)

        self.shopTile1 = TileCreator(10, int(self.screen.get_height() - boxsizeWithMargin), screen)
        self.shopTile2 = TileCreator(boxsizeWithMargin + 10, int(self.screen.get_height() - boxsizeWithMargin), screen)
        self.shopTile3 = TileCreator(2 * boxsizeWithMargin + 10, int(self.screen.get_height() - boxsizeWithMargin), screen)
        self.shopTile4 = TileCreator(3 * boxsizeWithMargin + 10, int(self.screen.get_height() - boxsizeWithMargin), screen)

        self.rollButton = RollButton(10, int(self.screen.get_height() - (1.75 * boxsizeWithMargin)), screen)

    def displayTiles(self, screen):
        self.playerTile1.blitTile()
        self.playerTile2.blitTile()
        self.playerTile3.blitTile()
        self.playerTile4.blitTile()
        self.playerTile5.blitTile()

        self.shopTile1.blitTile()
        self.shopTile2.blitTile()
        self.shopTile3.blitTile()
        self.shopTile4.blitTile()

        self.rollButton.blitTile()