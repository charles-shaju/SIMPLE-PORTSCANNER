#!/data/data/com.termux/files/usr/bin/python

import socket
import subprocess
import concurrent.futures
import sys
from datetime import datetime
import threading
import colorama
from colorama import Fore
colorama.init()
subprocess.call('clear',shell=True)

host= input("Enter the host to scan : ")
ip= socket.gethostbyname(host)
print (Fore.YELLOW + "-"*60)
print ("Please wait, scanning remote host ",ip)
print (Fore.YELLOW + "-"*60+Fore.WHITE)

t1=datetime.now()
def scan(ip,port):
 try:
       s=socket.getservbyport(port)
       sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       result=sock.connect_ex((ip, port))
       if result == 0:
           print(Fore.WHITE+"port" f'[{port}]:'+ Fore.GREEN+ "open   service="f'[{s}]' .format(port,s))
           #print("port %d :" + Fore.GREEN + " Open " %(port))
           print(Style.RESET)
       sock.close()  
 except socket.gaierror:
     print( Fore.RED + "couldn't connect to server")
     sys.exit()

with concurrent.futures.ThreadPoolExecutor(max_workers=250) as executor:
    for port in range(1,8080):  
      executor.submit(scan,ip,port)


t2= datetime.now()
total= t2-t1
print ("Scanning completed in :",total)
print (" Use me often :)")

