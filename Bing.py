#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 23:03:41 2021

@author: MR.GREEN
"""



import re , urllib , urllib.request ,os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as SPEED

try:
	from colorama import Fore
except:
	print ("Command : pip install colorama")
	input()
	exit(-1)

#Color
O = Fore.WHITE
G = Fore.GREEN
R = Fore.RED
B = Fore.BLUE
M = G+"[*]"+B
C = B+"[*]"+O


if os.name=="nt":
	os.system("cls")
else:
	os.system("clear")

print (G+"""
    <<<     CODE BY MR.GREEN     >>>
  __  __ ___        ___ ___ ___ ___ _  _ 
 |  \/  | _ \      / __| _ \ __| __| \| |
 | |\/| |   /  _  | (_ |   / _|| _|| .` |
 |_|  |_|_|_\ (_)  \___|_|_\___|___|_|\_|
                                         
	"""+O+"""BING GREB Tools V.1.1
	"""+R+"""Contact : fb.com/GREEN.localhost
""")


Go = urllib.request.build_opener()
Go.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.5 Safari/534.34')]
def Bing(Dork):
	D = Dork.strip()
	Dork = urllib.parse.quote(Dork.strip())
	print Dork
	P = 0
	Cou = 0
	All = []
	while P <= 1000000:
		try:
			Chack = Go.open("https://www.bing.com/search?q="+Dork+"&count=100&first="+str(P)+"&go=Search&qs=ds&form=QBRE").read().decode("utf-8")
			if "There are no results for" in Chack:
				break
			HTTP = re.findall('<h2><a href="http://(.*?)"', Chack)
			HTTPS = re.findall('<h2><a href="https://(.*?)"', Chack)
			if len(HTTP) <= 1:
				break
			for Domain in HTTP:
				#print Domain
				Domain = Domain.split(' ')[0]
				Domain = "http://"+Domain
				All.append(Domain)
			for Domain in HTTPS:
				#print Domain
				Domain = Domain.split(' ')[0]
				Domain = "https://"+Domain
				All.append(Domain)
			#print(P)
			P+=50
			Cou+=1
		except:
			pass
	Count = set(All)
	if len(Count) is not 0:
		PRINT = ("::%s : %sPAGE : %s %sTotal : %s\n" %(D ,B,Cou ,O,len(Count)))
		print (C+" Dork "+G+PRINT)
	for URL in Count:
		open("Domain.txt","a").write(URL+"\n")

try:
	List=open(input(C+M+O+" List DORK : "),"r").readlines()
except:
	print (R+"File Not Found")
Pool = SPEED(100)
Pool.map(Bing, List)
Pool.close() 
Pool.join()
