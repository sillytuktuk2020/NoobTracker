import sys, os, time, random
from core.Profiler import *
from colorama import Fore
import settings
from datetime import date
from txt.text import text
from txt.header import lb_header 
Green = Fore.GREEN
Red = Fore.RED
def daemon():
    I = """
             ,        ,
            /(        )`
            \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\\
           / /   | `    \\
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \\
<----|====O)))==) \) /====
<----'    `--' `.__,' \\
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \\
      `--{__________)        \/
      """
    return I 
def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Run this with python3.")

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def menu():
	pr = Profiler()
	pr.loadDatabase(settings.pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """ 
        \n 
        Modify By :  AKSHAY DHAWAN 
        version : 6.0.2
        Pays : [India : in] 
        [1] Lookup 
        [2] Other Tool 
        [3] Profiler 
        [4] Change Country 
        [e] Exit 
        [h] Help 
        [c] Clear Screen 
        """.format("Red+daemon(),Green+date")

	print(lb_header())
	print(menu)
