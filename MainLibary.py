import os, sys, socket, logging, random, platform, subprocess
from pwn import *
import paramiko
import nmap
from terminaltables import AsciiTable
import time

W = '\033[0m' # white.
R = '\033[31m' # Red
G = '\033[32m' # Green

TagChoice = raw_input('Would you like to use a target Ip \n').strip('\n')
if TagChoice == "yes":
        target_ip = raw_input('Please enter a Target IP Address \n').strip('\n')
else:
    print "Ok using defaults"
    target_ip = ""
private_ip = os.popen('ifconfig | grep "inet"| grep "192"').read()
public_ip = os.popen('wget http://ipinfo.io/ip -qO -').read()
location = os.popen('wget http://ipinfo.io/city -qO -').read()
mac_address = os.popen("cat /sys/class/net/eth0/address").read()


if platform.system() == "Windows":
    ##
    print 'adding functions..'
else:
    print "Welcome to Exploiation FrameWork"

def helpmenu():
    print "TEST"


def Reconaissance():
    while True:
        table_info = [
        ["Recon Modules", "Commands"],
        ["List", "Show all available commands"],
        ["exit", "Exit the module"],
        ["Scan", "Use Nmap To scan.."],
        ["Hosts", "Discover active hosts on the network"],
        ["Domain", "Use Jhaddix Recon-Ng Script"],
        ]

        table = AsciiTable(table_info)
        print table.table
        try:
            recon_options = raw_input("Reconaissance>> ").strip('\n')
            if recon_options == "Hosts":
                while True:
                    print "BLAAAAAAAH"
                    try:
                        nm = nmap.PortScanner()
                        nm.scan(hosts=target_ip + "/24", arguments='-sS -Pn -A')
                        print "INFO"
                        print "-"*64
                        for host in nm.all_hosts():
                            print('| Host | %s (%s) | %s |' % (host, nm[host].hostname(), nm[host].state()))
                            print('+------------------------------+')
                    except KeyboardInterrupt:
                        print "Closing.."
                        break
        except KeyboardInterrupt:
            print "Dead"
            sys.exit(0)

def target():
    target_ip = raw_input('Please enter your target\n')
    print 'target: %s' % target_ip
def DNSStuff():
    table_data = [
    ["DNS Networking", "Available Commands"],
    ["List", "Show all Available commands"],
    ["Exit", "Exit the module.."],
    ["DNSRecon", "Use DNS-Recon to find issues.."]
    ]
    table = AsciiTable(table_data)
    print table.table
