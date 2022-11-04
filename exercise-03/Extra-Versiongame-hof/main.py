from textAdventureClasses import *
import textAdventureGameLogic as gameLogic
import textAdventureIO as io

game = Game()

print('')
io.tprint(game.playerSpaceship.name, font='small')
io.speak(game.playerSpaceship.name, printError=True)
skipIntro = io.prompt('Skip intro?: ', ['Yes', 'No']) == 'Yes'
gameLogic.introScene(game, skipIntro)
