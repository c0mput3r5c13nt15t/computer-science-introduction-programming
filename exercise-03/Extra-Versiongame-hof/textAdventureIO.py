import os
from random import choice
from gtts import gTTS
from progress.bar import Bar
import time
from art import tprint
from threading import Thread


def speak(text):
    currentPath = os.path.dirname(os.path.abspath(__file__))
    tts = gTTS(text=text, lang='en')

    filename = f"{currentPath}/tmp-audio-{str(time.time())}.mp3"
    tts.save(filename)
    os.system("play \"" + filename + "\" -q -t alsa")
    os.remove(filename)


def makeStringSpecificLength(string: str, length: int, fill: str = ' ') -> str:
    return string + fill * (length - len(string))


def printWithTypingAnimation(text: str, speed: float = 0.08, newLine=True) -> None:
    thread = Thread(target=speak, args=(text,))
    thread.start()
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(speed)
    thread.join()
    if newLine:
        print('')
    else:
        print(' ', end='')


def printDialogue(character: str, text: str, verb: str = "says") -> None:
    # Print name of NPC and animate text
    printWithTypingAnimation(f'{character} {verb}:', newLine=False)
    printWithTypingAnimation('"' + text + '"')


def takeDamage(dealDamageShipName: str, takeDamageShipName: str, damageTo: str, damage: int) -> None:
    match choice(["laser", "missile", "railgun", "torpedo", "cannon"]):
        case "laser":
            printWithTypingAnimation(
                f"{dealDamageShipName} fires a laser at {takeDamageShipName} dealing {damage} damage to the {damageTo}.")
        case "missile":
            printWithTypingAnimation(
                f"{dealDamageShipName} fires a missile at {takeDamageShipName}. The missile swirls around {takeDamageShipName} and explodes dealing {damage} damage to the {damageTo}.")
        case "railgun":
            printWithTypingAnimation(
                f"{dealDamageShipName} charges up it's railgun and fires it at {takeDamageShipName} dealing {damage} damage to the {damageTo}.")
        case "torpedo":
            printWithTypingAnimation(
                f"{dealDamageShipName} opens a torpedo bay and fires a torpedo at {takeDamageShipName}. The torpedo bursts through the {damageTo} of {takeDamageShipName} dealing {damage} damage to it.")
        case "cannon":
            printWithTypingAnimation(
                f"{dealDamageShipName} orients its cannon towards {takeDamageShipName} and fires it. The projectile explodes on impact dealing {damage} damage to the {damageTo}.")
    print()


def printProgessBar(title: str, fill: str = '#', speed: float = 0.1) -> None:
    thread = Thread(target=speak, args=(title,))
    thread.start()
    bar = Bar(title, max=20, fill=fill, suffix='%(percent)d%%', )
    for i in range(20):
        time.sleep(speed)
        bar.next()
    thread.join()
    bar.finish()


def prompt(question: str, options: list[str] | None = None) -> str:
    printWithTypingAnimation(question)
    if options is not None:
        thread = Thread(target=speak, args=(
            f"{', '.join([options[i] for i in range(len(options)-1)] + ['or ' + options[-1]])}",))
        thread.start()
        print(
            '[', f"{' / '.join([options[i] for i in range(len(options))])}", ']', sep='')
        thread.join()
        while True:
            try:
                choice = input("> ")
                if choice in options:
                    print()
                    return choice
                else:
                    thread = Thread(target=speak, args=("Invalid choice",))
                    thread.start()
                    printWithTypingAnimation("Invalid choice")
                    thread.join()
            except ValueError:
                thread = Thread(target=speak, args=("Invalid choice",))
                thread.start()
                printWithTypingAnimation("Invalid choice")
                thread.join()
    else:
        returnInput = input("> ")
        print()
        return returnInput


if __name__ == '__main__':
    print('Typing animation:')
    printWithTypingAnimation('Hello world!')
    print('\nDialogue:')
    printDialogue('Bob', 'Hello world!')
    print('\nProgress bar:')
    printProgessBar('Loading', fill='=', speed=0.05)
    print('\nPrompt:')
    prompt('What is your name?')
    print('\nPrompt with Options:')
    prompt('What is your favorite color?', ['Red', 'Blue', 'Green'])
