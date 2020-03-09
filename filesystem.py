import os

'''
language = input('Change language: en, ru').lower()
if language == 'en':
    import locen as loc
elif language == 'ru':
    import locru as loc
'''

import locru as loc


def acceptCommand():
    try:
        com = int(input())
    except ValueError:
        acceptCommand()
    if com > 7 or com < 1:
        return acceptCommand()
    else:
        return com


def countBytes():
    try:
        if not os.listdir(os.getcwd()):
            return
        return os.path.getsize(os.getcwd())
    except:
        return acceptCommand()


def moveUp():
    try:
        return os.chdir(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    except:
        return acceptCommand()


def countFiles(path):
    pass


def moveDown():

    print('\n' + 'Choose a directory to get to:' + '\n')
    for n in range(len(os.listdir(os.getcwd()))):
        print(str(n + 1) + '. ' + str(os.listdir(os.getcwd())[n]))
    togo = input()
    os.chdir(os.getcwd() + '/' + os.listdir(os.getcwd())[int(togo)])


def findFiles(target,path):
    pass


def runCommand(command):
    if command == 1:
        os.listdir(os.getcwd())
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown()
    elif command == 4:
        countFiles(path)
    elif command == 5:
        print(countBytes())
    elif command == 6:
        findFiles(target, path)
    elif command == 7:
        print(loc.quit)


def main():
    while True:
        print(os.getcwd())
        print(loc.MENU)
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            break


main()
