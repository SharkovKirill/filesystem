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


# TODO:(Sveta) defs: countBytes(path), moveUp()
# TODO:(Vladimir) defs: countFiles(path), moveDown(currentDir)

def countBytes(path):
    pass
def moveUp():
    pass
def countFiles(path):
    pass
def moveDown(currentDir):
    pass
def findFiles(target,path):
    pass

def runCommand(command):
    if command == 1:
        os.listdir(os.getcwd())
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:
        countFiles(path)
    elif command == 5:
        countBytes(path)
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
        if command ==7:
            break
main()