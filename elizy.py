# eliza.py
import random
PHRASEN = ['Kannst du mir das Problem näher erklären?',
           'Erzähle mir mehr darüber!',
           'Warum ist das wichtig für dich?']
print('Eliza: Hallo, ich bin Eliza.Was hast du auf dem Herzen?')
eingabe ='x'
while eingabe != '':  
    eingabe = input('Du: ')
    eingabe = eingabe.lower()
    if 'hass' in eingabe:
        print('Eliza: Hass kann Wertvolles zerstören. ')
    elif 'liebe' in eingabe:
        print('Eliza: Liebe ist wunderbar')
    elif 'schlaf' in eingabe:
        print('Eliza: Schlaf ist wichtig')
    elif eingabe != '':
        text = random.choice(PHRASEN)
        print('Eilza: ', text)
print('Es war wunderbar, mit dir zu reden. Bis bald!')
