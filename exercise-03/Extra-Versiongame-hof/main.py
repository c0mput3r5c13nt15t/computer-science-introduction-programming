from textAdventureClasses import *
import textAdventureGameLogic as gameLogic
import textAdventureIO as io

game = Game()

print('')
io.tprint(game.playerSpaceship.name, font='small')
gameLogic.secondScene(game)
