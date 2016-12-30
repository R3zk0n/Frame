## To be used in a pentest, Logs are dumped and kept, automation of alot of stuff.

import os, sys, platform
from MainLibary import *
from pwn import *
import datetime
from subprocess import call


banner = G + """

"""



# Gobals
time = datetime.datetime.now().time()
if not os.getuid() == 0:
    sys.exit(R + "[-=+] You Are NOT ROOT. [!!!!]" + W)
print banner

# Fix time if you can.
table_data = [
    ["Time: ", str(time).strip('.')],
    ['Platform: ', str(platform_system)],
    ['==================================', "======================"],
    ["Private IP Info:", str(lan_ip)],
    ["Public IP Address: ", str(public_ip)],
    ["Mac Address: ", str(mac_address)],
    ['Gateway: ', str(gateway_ip)],
    [R + "Target Address: ", str(target_ip) + G],
    ]


table = AsciiTable(table_data)
print table.table

def main():
    while True:
        try:
            option = raw_input(">> ").strip('\n')
            if option == "recon":
                    Reconaissance()
            elif option == "help":
                  helpmenu()
            elif option == "clear":
                call(["clear"])
                continue
            elif option == "Exit":
                raise KeyboardInterrupt
            else:
                continue
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
