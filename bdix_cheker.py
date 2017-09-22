# coding: utf-8
# Imports
import os
import sys
import shutil
import win_unicode_console
from colorama import init, Fore, Style

# Basic settings
NODES_FILE = "nodes.txt" # Noedes list file
BDIX_PING = 15 # Maximum ping for bdix connections
PING_COUNT = 3 # No. of pings per node

# Ping
def ping(node):
    try:
        result = int(os.popen("ping -n {} {}".format(PING_COUNT, node)).read().strip().split("Average = ")[1][:-2])
        return result
    except:
        return

if __name__ == "__main__":
    win_unicode_console.enable()
    init()

    try:
        terminal_width = shutil.get_terminal_size().columns

        title = ["██████╗ ██████╗ ██╗██╗  ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗", "██╔══██╗██╔══██╗██║╚██╗██╔╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗", "██████╔╝██║  ██║██║ ╚███╔╝     ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝", "██╔══██╗██║  ██║██║ ██╔██╗     ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗", "██████╔╝██████╔╝██║██╔╝ ██╗    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║", "╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"]

        [print(Style.BRIGHT + Fore.CYAN + x.center(terminal_width-1)) for x in title]

        print(Fore.YELLOW + "Credit: ιηvαδεя & sιlvεя jαςκαl".center(terminal_width))

        if not os.path.exists(NODES_FILE):
            print(Fore.RED + "Nodes file not found. Make sure you have the {} file in the same directory as this tool.".format(NODES_FILE))
            input(Fore.WHITE + "\nPress Enter to Exit.")
            sys.exit()

        print(Fore.WHITE + "\nChecking ping...")
        results = []
        with open(NODES_FILE) as f:
            nodes = [x for x in f.read().split("\n") if x]
            for node in nodes:
                result = ping(node)
                if result:
                    results.append(result)

        if len(results) == 0:
            print(Fore.RED + "Network error.")
            input(Fore.WHITE + "\nPress Enter to Exit.")
            sys.exit()

        avg_result = sum(results) / len(results)

        if avg_result == 0:
            print(Fore.RED + "Network error.")
            input(Fore.WHITE + "\nPress Enter to Exit.")
            sys.exit()

        if avg_result <= BDIX_PING:
            print(Fore.GREEN + "\nCongratulation, your internet is connected to BDIX!")

        else:
            print(Fore.RED + "\nSorry, your internet is not connected to BDIX!")

        input(Fore.WHITE + "\nPress Enter to Exit.")

    except Exception as e:
        print(Fore.RED + "Unpexted error: {}".format(e))
        input(Fore.WHITE + "\nPress Enter to Exit.")
        sys.exit()
