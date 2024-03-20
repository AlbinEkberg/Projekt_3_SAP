from scripts.tileCreator import TileCreator

class TileMap:
    def __init__(self, screen):
        self.playerTile1 = TileCreator(100, 10, screen)
        self.playerTile2 = TileCreator(100, 30, screen)
        self.playerTile3 = TileCreator(100, 50, screen)
        self.playerTile4 = TileCreator(100, 70, screen)
        self.playerTile5 = TileCreator(100, 90, screen)

        self.shopTile1 = TileCreator(100, 110, screen)
        self.shopTile2 = TileCreator(100, 130, screen)
        self.shopTile3 = TileCreator(100, 150, screen)
        self.shopTile4 = TileCreator(100, 170, screen)
        self.shopTile5 = TileCreator(100, 190, screen)

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
        self.shopTile5.blitTile()
        print("hej samuel")