import random 
import time

def displayIntro():
    print('Вы находитесь в землях, заселенных драконами.')
    print('Перед собой вы видите две пешеры. В одной из них - дружелюбный дракон')
    print('который готов поделиться с вами своими сокровищами. Во второй -')
    print('жадный и голодный дракон, который мигом вас съест.')
    print()

def chooseCave():
    cave = ''   
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавищу 1 или 2)') 
        cave = input()

    return cave

def checkCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('...делится с вами сокровищами!')
    else:
        print('...моментально вас съедает!')    

playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()
    caveNamber = chooseCave()
    checkCave(caveNamber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()