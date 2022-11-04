def prompt(question: str, options) -> str:
    returnValue = input(f'{question} [{options}]\n> ')
    print()
    return returnValue


def printWithTwoNewlines(string: str) -> None:
    print(string, end='\n\n')


printWithTwoNewlines(
    'Per Anhalter durch die Galaxis - eine kurze Zusammenfassung')

known = prompt('Kennst du die Geschichte?', 'j / n') == 'j'

if known:
    printWithTwoNewlines('Super, dann geht\'s los!')
else:
    printWithTwoNewlines(
        'Das solltest du dringend ändern! Nein wirklich, das ist so ne Art Pflichtlektüre für jeden Informatiker. Naja, jetzt erst einmal weiter mit dem Spiel.')

printWithTwoNewlines(
    'Donnerstagmorgen um acht fühlte sich Arthur Dent nicht sehr gut.')

action1 = prompt('Er wachte benommen auf, schlurfte benommen in seinem Zimmer herum, machte ein Fenster auf, sah einen Bulldozer, fand seine Pantoffeln und ...',
                 'schlurfte ins Badezimmer / legte sich wieder hin')

if action1 == 'legte sich wieder hin':
    action2 = prompt('Einige Stunden später wachte er wieder auf. Die donnernden Bulldozer um sein Haus herum waren gerade dabei dieses Abzureißen, also ...',
                     'verschanzte er seinen Kopf in einem Kissen / sprang er auf')

    if action2 == 'sprang er auf':
        printWithTwoNewlines(
            'Doch es war bereits zu spät. Sein Haus war bereits größtenteils abgerissen, bevor wenige Minuten später die ganze Erde abgerissen wurde.')
    elif action2 == 'verschanzte er seinen Kopf in einem Kissen':
        printWithTwoNewlines('Arthur Dent sollte aus diesem Schlaf nie wieder erwachen. Nicht etwa weil er von einem Bulldozer erschlagen wurde, sondern weil die gesamte Erde abgerissen wurde. Vermutlich war es besser so, er ersparte sich so nämlich eine Menge Ärger.')
    else:
        printWithTwoNewlines(
            'Machte er etwas, dass der Programmierer nicht vorgesehen hatte, weswegen er sogleich unter mysteriösen Umständen ums Leben kam ...')
elif action1 == 'schlurfte ins Badezimmer':
    if known:
        printWithTwoNewlines(
            'Du weißt ja bereits was jetzt passiert. Stell dir also einfach vor, ich hätte eine Urheberrechtsverletzung begangen und den gesamten Text einfach hierher kopiert. Arthur wird nun also aus dem Vogonen Raumschiff geworfen')
    else:
        printWithTwoNewlines('Die folgenden Ereignisse waren spannend und wären aufwendig zu programmieren, weswegen ich sie hier nicht weiter ausführen werde. Es sei nur soviel gesagt, dass Arthur Dent wenige Minuten später aus einem Vogonen Raumschiff geworfen wird.')

    action2 = prompt('Das Universum entscheidet sich jedoch ...',
                     'ihn zu retten / ihn sterben zu lassen / ihm seine Geheimnisse zu offenbaren')

    if action2 == 'ihn zu retten':
        printWithTwoNewlines(
            'Arthur Dent und Ford werden unwahrscheinlicher weise gerettet und erleben noch viele weitere Abenteuer...')
    elif action2 == 'ihn sterben zu lassen':
        printWithTwoNewlines(
            'Arthur Dent und Ford sterben einfach, naja, was soll\'s, es ist ja nicht so, als hätten sie noch irgendwelche Abenteuer erlebt.')
    elif action2 == 'ihm seine Geheimnisse zu offenbaren':
        if known:
            printWithTwoNewlines('42.')
        else:
            printWithTwoNewlines(
                'Für einen kurzen Augenblick sieht Arthur DIE ABSOLUTE WAHRHEIT des Universums, doch dann erstickt er auch schon.')
    else:
        printWithTwoNewlines(
            'Etwas zu tun, was der Programmierer nicht vorgesehen hatte, weswegen es plötzlich und ohne guten Grund aufhörte zu existieren ...')
elif action1 == '42':
    printWithTwoNewlines(
        'Hey, nicht spoilern! Menno, jetzt hast du alles ruiniert!')
else:
    printWithTwoNewlines(
        'Machte er etwas, dass der Programmierer nicht vorgesehen hatte, weswegen er sogleich unter mysteriösen Umständen ums Leben kam ...')
print('Ende')
