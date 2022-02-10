from time import sleep
from design import *
from modules.decrypt import *
from modules.encrypt import *
from sys import exit as sysexit

try:
    from colorama import Fore, init
except ModuleNotFoundError:
    print("Please install the required modules")
    sleep(0.1)
    print("Use 'python -m pip install -r requirements.txt' or 'python3 -m pip install -r requirements.txt'")


def main():
    bold = '\033[1m'
    endbold = '\033[0m'
    try:
        init()
        introduce()
        startBanner()
        startMenu()
        print(Fore.BLUE + bold + "\nSelect an action:" + endbold)
        while True:
            try:
                sleep(0.1)
                num = int(input(Fore.LIGHTYELLOW_EX + ">>> " + Fore.GREEN))
                if num not in range(4):
                    raise ValueError
                fAction = num
                break
            except ValueError:
                sleep(0.1)
                print(Fore.RED + "Invalid Input")
                continue
        if fAction == 0:
            raise KeyboardInterrupt
        elif fAction == 3:
            infoPage()
            print(Fore.BLUE + bold + "Press Enter to exit..." + endbold)
            input(Fore.GREEN + "")
            raise KeyboardInterrupt
        elif fAction == 1:
            menu()
            print(Fore.BLUE + bold + "\nSelect an action:" + endbold)
            while True:
                try:
                    sleep(0.1)
                    num = int(input(Fore.LIGHTYELLOW_EX + ">>> " + Fore.GREEN))
                    if num not in range(5):
                        raise ValueError
                    sAction = num
                    break
                except ValueError:
                    sleep(0.1)
                    print(Fore.RED + "Invalid Input")
                    continue
            if sAction == 1:
                introduce("Base64 Encoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        encoded = encodeBase64(txt)
                        if not encoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(encoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 2:
                introduce("Hex Encoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        encoded = encodeHex(txt)
                        if not encoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(encoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 3:
                introduce("Rot13 Encoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        encoded = encodeRot13(txt)
                        if not encoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(encoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 4:
                main()
            elif sAction == 0:
                raise KeyboardInterrupt
        elif fAction == 2:
            menu(False)
            print(Fore.BLUE + bold + "\nSelect an action:" + endbold)
            while True:
                try:
                    sleep(0.1)
                    num = int(input(Fore.LIGHTYELLOW_EX + ">>> " + Fore.GREEN))
                    if num not in range(5):
                        raise ValueError
                    sAction = num
                    break
                except ValueError:
                    sleep(0.1)
                    print(Fore.RED + "Invalid Input")
                    continue
            if sAction == 1:
                introduce("Base64 Decoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        decoded = decodeBase64(txt)
                        if not decoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(decoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 2:
                introduce("Hex Decoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        decoded = decodeHex(txt)
                        if not decoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(decoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 3:
                introduce("Rot13 Decoder")
                sleep(0.1)
                print(Fore.LIGHTYELLOW_EX + "\nPress Ctrl + C to exit")
                sleep(0.1)
                print(Fore.BLUE + bold + "\n\nEnter Text:" + endbold)
                try:
                    while True:
                        sleep(0.1)
                        txt = input(Fore.LIGHTYELLOW_EX + ">>>" + Fore.GREEN)
                        decoded = decodeRot13(txt)
                        if not decoded:
                            sleep(0.1)
                            print(Fore.RED + bold + "Error" + endbold)
                        else:
                            sleep(0.1)
                            print(Fore.MAGENTA + f"{str(decoded)}")
                except KeyboardInterrupt:
                    sleep(0.1)
                    print(Fore.RED + "\nExiting...")
                    sleep(0.3)
                    sysexit()
            elif sAction == 4:
                main()
            elif sAction == 0:
                raise KeyboardInterrupt
    except KeyboardInterrupt:
        sleep(0.1)
        print(Fore.RED + "\nExiting...")
        sleep(0.3)
        sysexit()



if __name__ == "__main__":
    main()
