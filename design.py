from os import system
from sys import platform
from colorama import Fore, init
from time import sleep


init()

bold = '\033[1m'
endbold = '\033[0m'


def clearFunc():
    if platform.lower() == "win32":
        return "cls"
    return "clear"


def introduce(text="Welcome to CRYPTOGRAPHER!\nEnjoy!!!!", clear=True):
    if bool(clear):
        text = str(text)
        system(clearFunc())
    else:
        text = str(text)
    for i in text:
        print(bold + Fore.RED + i + endbold, flush=True, end="")
        sleep(0.1)


def startBanner():
    system(clearFunc())
    print(Fore.RED + """
   ____                  _                              _                
  / ___|_ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__   ___ _ __  
 | |   | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__| 
 | |___| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | |  __/ |    
  \____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\___|_|    
             |___/|_|             |___/          |_|           
                                                      base64|hex|rot13
""")
    sleep(0.2)
    print(Fore.WHITE + bold +
          """            ---------------------------------------------""")
    sleep(0.1)
    print("""            |                                           |""")
    sleep(0.1)
    print("""            |          __NAME__ = Cryptographer         |""")
    sleep(0.1)
    print("""            |          __AUTHOR__ = Parham              |""")
    sleep(0.1)
    print("""            |          __VERSION__ = 1.0                |""")
    sleep(0.1)
    print("""            |          __LICENSE__ = MIT                |""")
    sleep(0.1)
    print("""            |                                           |""")
    sleep(0.1)
    print("""            ---------------------------------------------""" + endbold)
    sleep(0.5)


def startMenu():
    print("\n")
    print(Fore.WHITE + bold + " [1]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Encoder")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [2]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Decoder")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [3]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Info")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [0]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Exit")
    sleep(0.1)


def menu(EncodePage=True):
    system(clearFunc())
    if bool(EncodePage):
        print(Fore.RED + """
   ____                  _                              _                
  / ___|_ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__   ___ _ __  
 | |   | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__| 
 | |___| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | |  __/ |    
  \____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\___|_|    
             |___/|_|             |___/          |_|           
                                                                Encode
""")
    else:
        print(Fore.RED + """
   ____                  _                              _                
  / ___|_ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__   ___ _ __  
 | |   | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__| 
 | |___| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | |  __/ |    
  \____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\___|_|    
             |___/|_|             |___/          |_|           
                                                                Decode
""")
    print("\n")
    print(Fore.WHITE + bold + " [1]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Base64")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [2]  " + endbold + Fore.LIGHTYELLOW_EX + "Hex")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [3]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Rot13")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [4]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Back")
    sleep(0.1)
    print(Fore.GREEN + bold + "-----------------" + endbold)
    sleep(0.1)
    print(Fore.WHITE + bold + " [0]  " +
          endbold + Fore.LIGHTYELLOW_EX + "Exit")
    sleep(0.1)


def infoPage():
    print(Fore.GREEN + """---------------------------------------------------------""")
    sleep(0.1)
    print("""   NAME = Cryptographer""")
    sleep(0.1)
    print("""   AUTHOR = Parham""")
    sleep(0.1)
    print("""   Github = https://github.com/parhamTheDeveloper""")
    sleep(0.1)
    print("""   VERSION = 1.0""")
    sleep(0.1)
    print("""   LICENSE = MIT""")
    sleep(0.1)
    print("""---------------------------------------------------------""")
    sleep(0.1)
