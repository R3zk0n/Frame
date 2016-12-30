import os, sys, socket, logging, random, platform, subprocess
from pwn import *
import paramiko
import nmap
from terminaltables import AsciiTable
import time
import requests

W = '\033[0m' # white.
R = '\033[31m' # Red
G = '\033[32m' # Green

#Global Variables XOREd.


TagChoice = raw_input('Would you like to use a Target IP? (Y/N) \n').strip('\n')
if TagChoice == 'Y':
        target_ip = raw_input('Please enter a Target IP Address \n').strip('\n')
else:
    target_NA = R + 'Target Not Set\n'
    print target_NA
    target_ip = ""


# Stole the regex's because they work well and i regexs
platform_system = platform.system()
lan_ip = os.popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'").read()
public_ip = os.popen("wget http://ipinfo.io/ip -qO -").read()
if platform.system() == "Darwin":
	mac_address = os.popen("ifconfig en1 | awk '/ether/{print $2}'").read()
	gateway_ip = os.popen("netstat -nr | grep default | grep -oE '\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b'").read()
else:
	mac_address = os.popen("cat /sys/class/net/eth0/address").read()
	gateway_ip = os.popen("/sbin/ip route | awk '/default/ { printf $3 }'").read()


# Work it out shiva..it means if your run windows.
if platform.system() == "Windows":
    ## Get it?!?!?
    print 'Dont bother...'
else:
    print "Welcome to Network FrameWork"


# Im lazy.. I should do this like first.. but...eh.
def helpmenu():
    print 'Well Fuck, This doesnt exist yet'
    print 'Umm..Have a good day?'
# Curl Option check, Not really needed now because of Nikto.
def CheckOptions():
    print 'Checking Options.'
    Check_IP = raw_input('Please enter the Address to check.\n').strip('\n')
    Check = os.system('curl -i -X OPTIONS %s' % Check_IP)
# Nmap..
def NNmap():
    get_ips = socket.gethostbyname(target_ip)
    # Changing to a string.
    hosts_list = str(get_ips)
    Nscanner = nmap.PortScanner()
    Nscanner.scan(hosts= target_ip, arguments='-PE -sn -oN %s.log' % (target_ip)) # Function, dump logs.
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))



#Nikto with html output.
def Nikto():
    nik = subprocess.Popen(["nikto +host %s -o %s.html" % (target_ip, target_ip)], stdout=subprocess.PIPE, shell=True)
    print R + 'Please wait Nikto is running..\n' + G
    (output, error) = nik.communicate()
    print output

# TLSSED automatically dumps logs in a file system. its great. checks for BEAST, HEARTBLEED, ETC.
def TLSSSL():
    TLSPORT = input('Enter a Port For SSL \n')
    print R + 'Please wait TLSSED Is running and creating logs..\n' + W
    SSL = subprocess.Popen(['tlssled %s %s' % (target_ip, TLSPORT)], stdout=subprocess.PIPE, shell=True)
    (output, error) = SSL.communicate()
    print output
# Table to print Recon info..# are modules that im planning to inlcude soon.
def Reconaissance():
    while True:
        table_info = [
        ["Recon Modules", "Commands"],
        ["List", "Show all available commands"],
        ["Exit", "Exit the module"],
        ['Nikto', 'Use Nikto..'],
        ['SSL', 'Check SSL/TLS Cerf'],
        ["Scan", "Use Nmap To scan.."],
        #["Hosts", "Discover active hosts on the network"],
        #["Domain", "Use Jhaddix Recon-Ng Script"],
        ]

        table = AsciiTable(table_info)
        print table.table
        try:
            recon_options = raw_input("Reconaissance>> ").strip('\n')
            if recon_options == 'Scan':
                NNmap()
            if recon_options == 'Info':
                CheckOptions()
            if recon_options == 'Nikto':
                Nikto()
            if recon_options == 'SSL':
                TLSSSL()
            if recon_options == 'exit':
                sys.exit(0)
                break
            if recon_options == 'List':
                Reconaissance()
        except KeyboardInterrupt:
            print "You asked to leave.. goodbye.\n"
            sys.exit(0)
# Target ip is for selection, instend of re-entering ip over and over.
def target():
    target_ip = raw_input('Please enter your target\n')
    print 'target: %s' % target_ip
