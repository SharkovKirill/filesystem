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


def main():
    while True:
        print(os.getcwd())
        print(loc.MENU)
        command = acceptCommand()
        #runCommand(command)
        #if command == QUIT:
        #    print(loc.quit)
#    break

main()