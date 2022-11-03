from textAdventureClasses import *
import textAdventureGameLogic as gameLogic
import textAdventureIO as io

game = Game()

print('')
io.tprint(game.playerSpaceship.name, font='small')
while True:
    gameLogic.secondScene(game)
    print()
    if io.prompt('Do you want to play again?', ['Yes', 'No']) == 'No':
        break
    game.reset()
