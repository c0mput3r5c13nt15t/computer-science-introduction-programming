from time import sleep
import textAdventureIO as io
from textAdventureClasses import *
from getpass import getpass
from random import choice, randint


# Intro scene


def introScene(game: Game) -> None:
    io.printWithTypingAnimation('It\'s the year 2143. The war between the Allied Systems and the Empire of the Suns has been raging for two years now. The Empire has been slowly but surely gaining ground, and the Allied Systems Fleet has taken heavy losses. The Allied Systems have been forced to take defensive position, defending the remaining colonies against enemy attacks at all costs.')
    sleep(2)
    print()
    io.printWithTypingAnimation(
        f'For a few weeks now, you have been the captain of the light cruiser "{game.playerSpaceship.name}".', newLine=False)
    io.printWithTypingAnimation(
        'You were only a cadet when you were promoted to the rank of captain. You have never fought in a real battle, heck, you have never even been on a real spaceship before. Of course, the simulations are good, but they\'re nothing compared to commanding a real ship.')
    sleep(2)
    print()
    io.printWithTypingAnimation(
        'You are on a routine patrol in the "Elcaro" system. There haven\'t been any hostilities in the area so far, but you are nervous nonetheless.', newLine=False)
    io.printWithTypingAnimation(
        'You are currently in the bridge of your ship. The bridge is a small room with a few consoles and a chair in the middle. The chair is yours. You sit down and log into the ship\'s computer.')
    print()
    print('---- Ship computer ----')
    game.username = input('Username: ')
    game.password = getpass()
    print('-----------------------')
    print()
    io.printWithTypingAnimation('You check the status of the ship.')
    print()
    io.printProgessBar('Checking status', speed=0.5)
    print()
    print(game.playerSpaceship)
    print()
    io.printWithTypingAnimation('The ship is in perfect condition.')
    print()
    nextScene = False
    while not nextScene:
        match io.prompt('What do you want to do now?', ['Look around', 'Admire the ship', 'Sip coffee', 'Wait']):
            case 'Look around':
                lookAround()
                nextScene = choice([True, False, False])
            case 'Admire the ship':
                admireShip(game)
            case 'Sip coffee':
                sipCoffee()
                nextScene = choice([True, False])
            case 'Wait':
                nextScene = True
    secondScene(game)


def lookAround() -> None:
    item = choice(['plant', 'coffee cup', 'picture of your family'])
    io.printWithTypingAnimation(
        'You look around the sparsly furnished room ...', newLine=False)

    if item == 'plant':
        io.printWithTypingAnimation(
            'You see a potted plant in the corner.', newLine=False)
        io.printWithTypingAnimation(
            'It\'s a beautiful plant, but it\'s not your favourite.', newLine=False)
        io.printWithTypingAnimation(
            'You look at it for a few seconds and then turn away.')
    elif item == 'coffee cup':
        io.printWithTypingAnimation(
            'You see the coffee cup on the table.', newLine=False)
        io.printWithTypingAnimation('You think about taking a sip.')
    elif item == 'picture of your family':
        io.printWithTypingAnimation(
            'You see a picture of your family on the wall.')
        print(
            """
      ,--.
     //^\\\\\\  ,;;;,                        .
    ((-_-))) (-_- ;                       /_\\
     )))(((   >..'.    .:.     .--.      |SSt|
    ((_._ )  /.   .|  :-_-;   /-_-))
    _))A ((_//| S ||  ,`-'.   ))-((
    `(    )`' |___|),;, C \\_/,`I ))
      \\  /    | | |`' |___(/-'|___()  ,-.
       )(     | | |   | | |   | | |  (-_-)    _____
      /__\\    |_|_|   |_|_|   |_|_|  (\\I/\\.__|A|R|T|
      `''     `-'-'   `-'-'   `-'-'  `'-`'   `o' `o'
""")
        io.printWithTypingAnimation(
            'It makes you feel sad when you think about how much you miss them and that you might never see them again.')
    print()


def sipCoffee() -> None:
    io.printWithTypingAnimation(
        'You reach for the coffee cup on the table next to you.', newLine=False)
    io.printWithTypingAnimation(
        'You slowly lift the cup to your mouth and take a long sip. *slurp*')
    print()


def admireShip(game: Game) -> None:
    """Prints the ship."""
    print(game.playerSpaceship)
    print()
    io.printWithTypingAnimation(
        'It\'s a beautiful ship. You feel proud to be her captain. But will you be able to protect her?')
    print()


# Second scene


def secondScene(game: Game) -> None:
    enemyCount = choice([1, 1, 1, 1, 2, 2, 3])
    for i in range(enemyCount):
        game.newEnemySpaceship()
    io.printWithTypingAnimation(
        f'*Sirens blare* "Enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} detected!"', newLine=False)
    io.printWithTypingAnimation(
        f'You startle in your chair. What is going on? You look at the radar.', newLine=False)
    if enemyCount == 1:
        io.printWithTypingAnimation('There is one enemy ship approaching.')
    else:
        io.printWithTypingAnimation(
            f'There are {enemyCount} enemy ships approaching.')
    print()
    io.printDialogue('First Officer', 'What do we do, captain?', 'asks')
    print()
    match io.prompt('You have to decide quickly.', [f'Scan enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}', 'Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
        case 'Scan enemy ship':
            scanShips(game)
            match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
                case 'Attack':
                    attack(game)
                case 'Send a distress signal':
                    game = sendDistressSignal(game)
                    match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Scan enemy ships':
            scanShips(game)
            match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Send a distress signal', 'Retreat', 'Surrender']):
                case 'Attack':
                    attack(game)
                case 'Send a distress signal':
                    game = sendDistressSignal(game)
                    match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Attack':
            attack(game)
        case 'Send a distress signal':
            game = sendDistressSignal(game)
            match io.prompt('Unimpressed with this desperate attempt, the enemy ships close in. What now?', ['Scan enemy ships', 'Attack', 'Retreat', 'Surrender']):
                case 'Scan enemy ship':
                    scanShips(game)
                    match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Scan enemy ships':
                    scanShips(game)
                    match io.prompt('Now that you know your enemy, you can make an informed decision on what to do.', ['Attack', 'Retreat', 'Surrender']):
                        case 'Attack':
                            attack(game)
                        case 'Retreat':
                            retreat(game)
                        case 'Surrender':
                            surrender(game)
                case 'Attack':
                    attack(game)
                case 'Retreat':
                    retreat(game)
                case 'Surrender':
                    surrender(game)
        case 'Retreat':
            retreat(game)
        case 'Surrender':
            surrender(game)


def scanShips(game: Game) -> None:
    io.printWithTypingAnimation(
        f'You instruct the Science Officer to scan the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLine=False)
    print()
    for enemySpaceships in game.enemySpaceships:
        print()
        print(enemySpaceships)
    print()


def sendDistressSignal(game: Game) -> Game:
    io.printWithTypingAnimation(
        'You instruct the Communications Officer to send a distress signal. Hopefully, someone will come to your aid.')
    game.distressSignalSent = True
    print()
    return game


# Third scene


def attack(game: Game) -> None:
    pass


def retreat(game: Game) -> None:
    io.printWithTypingAnimation(
        'Knowing that you cannot win and fearing for your life, you decide to retreat.')
    print()
    io.printDialogue(
        'First Officer', 'What are you doing, captain? We can\'t just run away!', 'asks')
    print()
    match io.prompt('What do you answer?', ['I\'m sorry, but I have to do this.', 'You\'re right. We can\'t run away.']):
        case 'I\'m sorry, but I have to do this.':
            io.printDialogue(
                'You', 'I\'m sorry, but I have to do this.', 'say')
            io.printDialogue(
                'You', 'All power to the engines and rear shields. We\'re retreating. That is an order!', 'say')
            io.printDialogue(
                'First Officer', 'But captain, that will leave the colonies defenseless!', 'exclaims')
            io.printDialogue(
                'You', 'Then so be it. I won\'t risk the lives of my crew to fight a losing battle.', 'answer')
            print()
            io.printWithTypingAnimation(
                f'The engines roar to life and the ship starts to move away from the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLine=False)

            # Fastes enemy ship
            canCatchUp = False
            for enemySpaceship in game.enemySpaceships:
                if enemySpaceship.speed > game.playerSpaceship.speed:
                    canCatchUp = True
                    break

            if canCatchUp:
                io.printWithTypingAnimation(
                    f'The enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} {"catches" if len(game.enemySpaceships) == 1 else "catch"} up to you.', newLine=False)
                io.printWithTypingAnimation(
                    'A feeling of dread fills you.')
                print()
                damage = randint(30, 80)
                io.takeDamage(choice(game.enemySpaceships).name,
                              f'your ship ({game.playerSpaceship.name})', 'hull', damage)
                game.playerSpaceship.hull -= damage
                if game.playerSpaceship.hull <= 0:
                    shipExplodes(game)
                io.printWithTypingAnimation(
                    'You don\'t have a choice. You are forced to surrender.')
                finalSurrender(game)
            else:
                io.printWithTypingAnimation(
                    f'You are able to outrun the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"}. Your rear shields can withstand the fire.', newLine=False)
                io.printWithTypingAnimation(
                    'As soon as you are out of range, you jump to the nearest allied system to report the attack.')
                print()
                io.printWithTypingAnimation('The end.')
        case 'You\'re right. We can\'t run away.':
            pass
            # TODO: Implement this


def surrender(game: Game) -> None:
    io.printWithTypingAnimation(
        'This is too much for you. You know you don\'t stand a chance against the enemy, so you decide to surrender.')
    print()
    surrenderInTime = choice([False, False])
    if surrenderInTime:
        prisonerEnding(game)
    else:
        io.printWithTypingAnimation(
            f'You\'r about to hail the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} but they have already opened fire.')
        print()
        damage = randint(30, 80)
        io.takeDamage(choice(game.enemySpaceships).name,
                      f'your ship ({game.playerSpaceship.name})', 'hull', damage)
        game.playerSpaceship.hull -= damage
        if game.playerSpaceship.hull <= 0:
            shipExplodes(game)
        io.printWithTypingAnimation(
            'The whole ship shakes violently. You are thrown out of your chair.', newLine=False)
        io.printWithTypingAnimation('You lie on the floor dazed and bleeding.')
        print()
        options = ['Attack', 'Retreat']
        if not game.distressSignalSent:
            options += ['Send a distress signal']
        match io.prompt('You are desperate. You have to do something.', options):
            case 'Attack':
                io.printWithTypingAnimation(
                    'You didn\'t want to do this, but you have no choice.')
                attack(game)
            case 'Retreat':
                retreat(game)
            case 'Send a distress signal':
                sendDistressSignal(game)
                match io.prompt('You doubt that anyone will come to help you. You will have to do something anyway.', ['Attack', 'Retreat']):
                    case 'Attack':
                        attack(game)
                    case 'Retreat':
                        retreat(game)


def finalSurrender(game: Game) -> None:
    surrenderInTime = choice([False, False])
    if surrenderInTime:
        prisonerEnding(game)
    else:
        io.printWithTypingAnimation(
            f'You\'r about to hail the enemy {"ship" if len(game.enemySpaceships) == 1 else "ships"} but then ...')
        print()
        while game.playerSpaceship.hull > 0:
            damage = randint(30, 80)
            io.takeDamage(choice(game.enemySpaceships).name,
                          f'your ship ({game.playerSpaceship.name})', 'hull', damage)
            game.playerSpaceship.hull -= damage
        shipExplodes(game)


def prisonerEnding(game: Game) -> None:
    io.printDialogue(
        'You', f'Hail the enemy ship {"ship" if len(game.enemySpaceships) == 1 else "ships"}. We surrender.', 'instruct')
    print()
    io.printWithTypingAnimation(
        f'Your first officer looks at you in disbelief, but he does as you say. He sends a message to the enemy ship {"ship" if len(game.enemySpaceships) == 1 else "ships"}.', newLine=False)
    io.printWithTypingAnimation(
        'The enemies board your ship and take you and your crew prisoner.', newLine=False)
    io.printWithTypingAnimation(
        'It\'s not the end you had hoped for, but at least you\'re alive.')
    print()
    io.printWithTypingAnimation('The end.')


def shipExplodes(game: Game) -> None:
    io.printWithTypingAnimation(
        'It\'s over. The damage inflicted on your ship is too much. You take a last breath, then the ship explodes violently.', newLine=False)
    io.printWithTypingAnimation(
        'The explosion instantly kills you and your crew. The shattered hull of your ship floats through space as the enemy now sets course for the now unprotected colonies.')
    print()
    io.printWithTypingAnimation('The end.')
