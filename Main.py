import os
import pyfiglet

# --- #


def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def Banner():
    Clear()
    print("""                   _ _                            _                 _____                           _             
    /\            (_|_)                /\        | |               / ____|                         | |            
   /  \   ___  ___ _ _    ______      /  \   _ __| |_    ______   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
  / /\ \ / __|/ __| | |  |______|    / /\ \ | '__| __|  |______|  | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 / ____ \\\__ \ (__| | |             / ____ \| |  | |_             | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
/_/    \_\___/\___|_|_|            /_/    \_\_|   \__|             \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                  
Created By : Pale-Hacker\n""")

# --- #


Banner()
Text = input("Enter Text : ")

# --- #

Clear()
Ascii_Art = pyfiglet.figlet_format(Text)

print(Ascii_Art)

# --- #

input("Press \"Enter\" To Exit ! ")

# --- #
