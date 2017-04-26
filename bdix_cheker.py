# coding: utf-8
# Imports
import os
import sys
import shutil
import win_unicode_console
from colorama import init, Fore, Style

# Basic settings
BDIX_PING = 15 # Maximum ping for bdix connections
NODES = ["dhakacom.com", "naturalbd.com", "mojaloss.net"] # Nodes to check against
PING_COUNT = 2 # No. of pings per node

# Ping
def ping():
    try:
        print(Fore.WHITE + "\nChecking ping...")
        results = []
        for i in NODES:
            try:
                result = int(os.popen("ping -n {} {}".format(PING_COUNT, i)).read().strip().split("Average = ")[1][:-2])
                results.append(result)
            except:
                print(Fore.RED + "Network error.")
                return 0

        result = sum(results) / len(results)
        return result

    except Exception as e:
        print(Fore.RED + "Unpexted error: {}".format(e))
        return 0

if __name__ == "__main__":
    win_unicode_console.enable()
    init()

    try:
        terminal_width = shutil.get_terminal_size().columns

        title = ["██████╗ ██████╗ ██╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗", "██╔══██╗██╔══██╗██║╚██╗██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗", "██████╔╝██║  ██║██║ ╚███╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝", "██╔══██╗██║  ██║██║ ██╔██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗", "██████╔╝██████╔╝██║██╔╝ ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║", "╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"]

        [print(Style.BRIGHT + Fore.CYAN + x.center(terminal_width-1)) for x in title]

        print(Fore.YELLOW + "Credit: ιηvαδεя & sιlvεя jαςκαl".center(terminal_width))

        result = ping()

        if result == 0:
            input(Fore.WHITE + "\nPress Enter to Exit.")
            sys.exit()

        if result <= BDIX_PING:
            print(Fore.GREEN + "\nCongratulation, your internet is connected to BDIX!")

        else:
            print(Fore.RED + "\nSorry, your internet is not connected to BDIX!")

        input(Fore.WHITE + "\nPress Enter to Exit.")

    except Exception as e:
        print(Fore.RED + "Unpexted error: {}".format(e))
        input(Fore.WHITE + "\nPress Enter to Exit.")
        sys.exit()
