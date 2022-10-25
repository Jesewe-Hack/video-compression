import time
import colorama
import ctypes
import os
import moviepy.editor as mp
from colorama import init, Fore
init()
ctypes.windll.kernel32.SetConsoleTitleW('Video Compression | By Jesewe Hack')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner="""
             ▌ ▐·▪  ·▄▄▄▄  ▄▄▄ .           ▄▄·       • ▌ ▄ ·.  ▄▄▄·▄▄▄  ▄▄▄ ..▄▄ · .▄▄ · ▪         ▐ ▄ 
            ▪█·█▌██ ██▪ ██ ▀▄.▀·▪         ▐█ ▌▪▪     ·██ ▐███▪▐█ ▄█▀▄ █·▀▄.▀·▐█ ▀. ▐█ ▀. ██ ▪     •█▌▐█
            ▐█▐█•▐█·▐█· ▐█▌▐▀▀▪▄ ▄█▀▄     ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█· ██▀·▐▀▀▄ ▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌
             ███ ▐█▌██. ██ ▐█▄▄▌▐█▌.▐▌    ▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▪·•▐█•█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌
            . ▀  ▀▀▀▀▀▀▀▀•  ▀▀▀  ▀█▄▀▪    ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀.▀   .▀  ▀ ▀▀▀  ▀▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪
"""

while True:
    os.system("cls")
    print(bcolors.OKGREEN + banner)
    print(bcolors.OKBLUE + """
                                [ Made by Jesewe Hack : https://github.com/Jesewe-Hack ]
    """ + bcolors.ENDC)
    try:
        fname = input(bcolors.OKCYAN + 'Please enter a file name (example: test): ')
        ftype = input(bcolors.OKCYAN + 'Please specify the file extension (example: .mp4): ')
        print('')
        clip = mp.VideoFileClip(fname + ftype)
        clip.write_videofile("output" + ftype)
    except Exception as e:
        os.system('cls')
        print(bcolors.FAIL + '\n[!] Error: Video compression error')
        input(bcolors.OKGREEN + "\nPress Enter to exit the menu... ")
    else:
        print(bcolors.OKGREEN + '\n[+] Video successfully compressed!')
        print(bcolors.OKGREEN + f'\n[+] Video saved as output' + ftype)
        input(bcolors.OKGREEN + "\nPress Enter to exit the menu... ")
