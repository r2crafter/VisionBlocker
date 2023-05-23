import os, signal
import time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)
TIME = 0.5

#defines the function for quickly making a new line (i'm lazy)
def newline():
    print('\n')


def toolslist():
    print(Fore.YELLOW + '1. Block ClassroomWindows' + '\n' + 'debug. Block Notepad (for debug)')


# defining function for closing ClassroomWindows program
def closeCW():
    while True:
        os.system('taskkill /im ClassroomWindows.exe')
        os.system('cls')
        time.sleep(TIME)
# defining function for closing ClassroomWindows program
def closeDebug():
    while True:
        os.system('taskkill /im Notepad.exe')
        os.system('cls')
        time.sleep(TIME)


#displays the visionblocker is running logo
def displayrunninglogo():
    f = open('logo.txt', 'r')
    logo = f.read()
    print(Fore.YELLOW + logo)
    print(Fore.GREEN + '\nis running ' + Fore.RED + '\n\nPress the X to close the program ' + Fore.YELLOW + '\nRelaunch the program to go back to the main menu')
    f.close()


#printing welcome screen
#print(Fore.YELLOW + '\n' + 'Welcome to')
#f = open('logo.txt', 'r')
#logo = f.read()
#print(Fore.YELLOW + logo)
#f.close()


# displays the list of tools available to the user
newline()
toolslist()
newline()

#feedback text
#print(Fore.BLUE + 'If you have any feedback or issues please post the in the issues tab on the github' + Fore.GREEN + '\n' + 'If you would like another program added to the list please contact my discord ' + Fore.WHITE + 'Switch#3252')

newline()
newline()

#asks what tool the user would like to use
oinput = input(Fore.YELLOW + 'Enter the number corresponding to what you would like to do \n\n' + Fore.WHITE)




if oinput == '1':
    closeCW()
if oinput == 'debug':
    closeDebug()