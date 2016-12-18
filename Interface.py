import os, sys, platform
from MainLibary import *
from pwn import *
import datetime
from subprocess import call


banner = G + """
  NETWORK FRAME.

"""



# Gobals
time = datetime.datetime.now().time()
if not os.getuid() == 0:
    sys.exit("[-=+] You Are NOT ROOT. [!!!!]")
print banner
table_data = [
    ["Time: ", str(time)],
    ["Network Info", ""],
    ["Private IP Info", str(private_ip)],
    ["Public IP Address: ", str(public_ip)],
    ["Mac Address: ", str(mac_address)],
    [R + "Target Address: ", str(target_ip) + G],
    ]


table = AsciiTable(table_data)
print table.table

def main():
    while True:
        try:
            option = raw_input(">> ").strip('\n')
            if option == "target":
                    target()
            if option == "recon":
                    Reconaissance()
            elif option == "exploit":
                ExploitationTest()
            elif option == "help":
                  helpmenu()
            elif option == "clear":
                call(["clear"])
                continue
            elif option == "exit":
                raise KeyboardInterrupt
            else:
                continue
        except KeyboardInterrupt:
            sys.exit(0)

if __name__ == "__main__":
    main()
