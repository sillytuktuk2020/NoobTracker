# -*- coding: utf-8 -*-

__version__ = 6.0

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style

init()
warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"

def checkVersion():
	version = sys.version[:1]
	if int(version) == 3:
		pass
	else:
		sys.exit(warning+" Please run python version 3.")

checkVersion()

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def loadlib():

	import requests, json

	import datetime

	# fonction
	from core.bssidFinder import bssidFinder
	from core.employee_lookup import employee_lookup
	from core.google import google
	from core.hashDecrypt import hashdecrypt
	from core.ipFinder import ipFinder
	from core.mailToIP import mailToIP
	from core.profilerFunc import profilerFunc
	from core.searchAdresse import searchAdresse
	from core.searchTwitter import searchTwitter
	from core.searchPersonne import searchPersonne
	from core.searchInstagram import searchInstagram
	from core.searchUserName import searchUserName
	from core.searchNumber import searchNumber
	from core.searchEmail import SearchEmail
	from core.Profiler import Profiler
	from core.facebookStalk import facebookStalk

	global monip, monpays, codemonpays, pathDatabase
	global bssidFinder, employee_lookup, google, hashdecrypt, ipFinder, mailToIP, profilerFunc
	global searchPersonne, SearchEmail, searchInstagram, searchTwitter, searchNumber, searchAdresse, searchUserName, facebookStalk
	global Profiler


	monip = requests.get("https://api.ipify.org/").text

	monpays = requests.get("http://ip-api.com/json/"+monip).text
	value = json.loads(monpays)
	monpays = value['country']
	codemonpays = value['countryCode']

	pathDatabase = os.path.abspath(__file__).split("\\")[:-1]
	pathDatabase = "\\".join(pathDatabase)+"\\Watched"

	if not os.path.exists(pathDatabase):
		os.mkdir(pathDatabase)

def loadingHack(importlib):
	chaine = "[*]"+' Start  NoobTracker...'
	charspec = "$*.X^%_/\\#~!?;"

	while importlib.is_alive():
		chainehack = ""
		for c in chaine:
			chainehack += c
			r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
			if len(chainehack+r) <= len(chaine):
				pass
			else:
				r = ""
			sys.stdout.write('\r'+chainehack+r)
			time.sleep(0.06)

def loadingUpper(importlib):

	string = "Start NoobTracker"
	string = list(string)
	nb = len(string)

	while importlib.is_alive():
		x = 0
		while x < nb:
			c = string[x]
			c = c.upper()
			string[x] = c
			sys.stdout.write("\r[*] "+''.join(string) +'...')
			time.sleep(0.1)
			c = string[x]
			c = c.lower()
			string[x] = c
			x += 1

def loadingTextPrint(importlib):
	string = "Start NoobTracker"

	while importlib.is_alive():

		space = " " * 100
		sys.stdout.write("\r"+space)
		
		x = 1

		while x <= len(string):
			times = "0."
			times += str(random.choice(range(1, 3)))
			sys.stdout.write("\rroot@NoobTracker:~$ "+string[:x]+"|")
			time.sleep(float(times))
			x += 1

def thread_loading():

	num = random.choice([1, 2, 3])

	importlib = threading.Thread(target=loadlib)
	importlib.start()

	if num == 1:
		load = threading.Thread(target=loadingHack(importlib))
	elif num == 2:
		load = threading.Thread(target=loadingUpper(importlib))
	elif num == 3:
		load = threading.Thread(target=loadingTextPrint(importlib))

	load.start()
	importlib.join()
	load.join()

thread_loading()

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)


from datetime import date
today_date = date.today()

header1 = """
 
  ________  __    ___      ___       ___  ___  ___________  ____  ____  __   ___  ___________  ____  ____  __   ___  
 /"       )|" \  |"  |    |"  |     |"  \/"  |("     _   ")("  _||_ " ||/"| /  ")("     _   ")("  _||_ " ||/"| /  ") 
(:   \___/ ||  | ||  |    ||  |      \   \  /  )__/  \\__/ |   (  ) : |(: |/   /  )__/  \\__/ |   (  ) : |(: |/   /  
 \___  \   |:  | |:  |    |:  |       \\  \/      \\_ /    (:  |  | . )|    __/      \\_ /    (:  |  | . )|    __/   
  __/  \\  |.  |  \  |___  \  |___    /   /       |.  |     \\ \__/ // (// _  \      |.  |     \\ \__/ // (// _  \   
 /" \   :) /\  |\( \_|:  \( \_|:  \  /   /        \:  |     /\\ __ //\ |: | \  \     \:  |     /\\ __ //\ |: | \  \  
(_______/ (__\_|_)\_______)\_______)|___/          \__|    (__________)(__|  \__)     \__|    (__________)(__|  \__) 
                                                                                                                     
 
"""

header2 = """

 
  /$$$$$$  /$$ /$$ /$$        /$$$$$$$$        /$$    /$$$$$$$$        /$$      
 /$$__  $$|__/| $$| $$       |__  $$__/       | $$   |__  $$__/       | $$      
| $$  \__/ /$$| $$| $$ /$$   /$$| $$ /$$   /$$| $$   /$$| $$ /$$   /$$| $$   /$$
|  $$$$$$ | $$| $$| $$| $$  | $$| $$| $$  | $$| $$  /$$/| $$| $$  | $$| $$  /$$/
 \____  $$| $$| $$| $$| $$  | $$| $$| $$  | $$| $$$$$$/ | $$| $$  | $$| $$$$$$/ 
 /$$  \ $$| $$| $$| $$| $$  | $$| $$| $$  | $$| $$_  $$ | $$| $$  | $$| $$_  $$ 
|  $$$$$$/| $$| $$| $$|  $$$$$$$| $$|  $$$$$$/| $$ \  $$| $$|  $$$$$$/| $$ \  $$
 \______/ |__/|__/|__/ \____  $$|__/ \______/ |__/  \__/|__/ \______/ |__/  \__/
                       /$$  | $$                                                
                      |  $$$$$$/                                                
                       \______/                                                 
                                                                                                          
"""

header5 = """
 ___    
        _           _          _             _    _        _        _      _                  _            _      _                  _        
       / /\        /\ \       _\ \          _\ \ /\ \     /\_\     /\ \   /\_\               /\_\         /\ \   /\_\               /\_\      
      / /  \       \ \ \     /\__ \        /\__ \\ \ \   / / /     \_\ \ / / /         _    / / /  _      \_\ \ / / /         _    / / /  _   
     / / /\ \__    /\ \_\   / /_ \_\      / /_ \_\\ \ \_/ / /      /\__ \\ \ \__      /\_\ / / /  /\_\    /\__ \\ \ \__      /\_\ / / /  /\_\ 
    / / /\ \___\  / /\/_/  / / /\/_/     / / /\/_/ \ \___/ /      / /_ \ \\ \___\    / / // / /__/ / /   / /_ \ \\ \___\    / / // / /__/ / / 
    \ \ \ \/___/ / / /    / / /         / / /       \ \ \_/      / / /\ \ \\__  /   / / // /\_____/ /   / / /\ \ \\__  /   / / // /\_____/ /  
     \ \ \      / / /    / / /         / / /         \ \ \      / / /  \/_// / /   / / // /\_______/   / / /  \/_// / /   / / // /\_______/   
 _    \ \ \    / / /    / / / ____    / / / ____      \ \ \    / / /      / / /   / / // / /\ \ \     / / /      / / /   / / // / /\ \ \      
/_/\__/ / /___/ / /__  / /_/_/ ___/\ / /_/_/ ___/\     \ \ \  / / /      / / /___/ / // / /  \ \ \   / / /      / / /___/ / // / /  \ \ \     
\ \/___/ //\__\/_/___\/_______/\__\//_______/\__\/      \ \_\/_/ /      / / /____\/ // / /    \ \ \ /_/ /      / / /____\/ // / /    \ \ \    
 \_____\/ \/_________/\_______\/    \_______\/           \/_/\_\/       \/_________/ \/_/      \_\_\\_\/       \/_________/ \/_/      \_\_\   
                                                                                                                                              

"""

header6 = """

  ________  __    ___      ___       ___  ___  ___________  ____  ____  __   ___  ___________  ____  ____  __   ___  
 /"       )|" \  |"  |    |"  |     |"  \/"  |("     _   ")("  _||_ " ||/"| /  ")("     _   ")("  _||_ " ||/"| /  ") 
(:   \___/ ||  | ||  |    ||  |      \   \  /  )__/  \\__/ |   (  ) : |(: |/   /  )__/  \\__/ |   (  ) : |(: |/   /  
 \___  \   |:  | |:  |    |:  |       \\  \/      \\_ /    (:  |  | . )|    __/      \\_ /    (:  |  | . )|    __/   
  __/  \\  |.  |  \  |___  \  |___    /   /       |.  |     \\ \__/ // (// _  \      |.  |     \\ \__/ // (// _  \   
 /" \   :) /\  |\( \_|:  \( \_|:  \  /   /        \:  |     /\\ __ //\ |: | \  \     \:  |     /\\ __ //\ |: | \  \  
(_______/ (__\_|_)\_______)\_______)|___/          \__|    (__________)(__|  \__)     \__|    (__________)(__|  \__) 
                                                                                                                     

"""

header7 = """

 __ _ _ _      _____       _    _____       _    
/ _(_) | |_   /__   \_   _| | _/__   \_   _| | __
\ \| | | | | | |/ /\/ | | | |/ / / /\/ | | | |/ /
_\ \ | | | |_| / /  | |_| |   < / /  | |_| |   < 
\__/_|_|_|\__, \/    \__,_|_|\_\\/    \__,_|_|\_\
          |___/                                  
                                            
"""

header8 = """
     
                                             
 _____ _ _ _     _____     _   _____     _   
|   __|_| | |_ _|_   _|_ _| |_|_   _|_ _| |_ 
|__   | | | | | | | | | | | '_| | | | | | '_|
|_____|_|_|_|_  | |_| |___|_,_| |_| |___|_,_|
            |___|                            
                             
"""

header9 = """
   
   _____ _ ____     ______      __  ______      __  
  / ___/(_) / /_  _/_  __/_  __/ /_/_  __/_  __/ /__
  \__ \/ / / / / / // / / / / / //_// / / / / / //_/
 ___/ / / / / /_/ // / / /_/ / ,<  / / / /_/ / ,<   
/____/_/_/_/\__, //_/  \__,_/_/|_|/_/  \__,_/_/|_|  
           /____/                                   
                                                     
"""

header11 = """

  _________.__.__  .__         ___________     __   ___________     __    
 /   _____/|__|  | |  | ___.__.\__    ___/_ __|  | _\__    ___/_ __|  | __
 \_____  \ |  |  | |  |<   |  |  |    | |  |  \  |/ / |    | |  |  \  |/ /
 /        \|  |  |_|  |_\___  |  |    | |  |  /    <  |    | |  |  /    < 
/_______  /|__|____/____/ ____|  |____| |____/|__|_ \ |____| |____/|__|_ \
        \/              \/                         \/                   \/
 
"""

header12 = """                                             
 
  ??????  ??? ???     ???   ???   ???????????? ?    ??  ?? ???????????? ?    ??  ?? ???
???    ? ????????    ????    ???  ????  ??? ?? ??  ???? ????? ?  ??? ?? ??  ???? ????? 
? ????   ????????    ????     ??? ???? ???? ?????  ?????????? ? ???? ?????  ?????????? 
  ?   ???????????    ????     ? ?????? ???? ? ???  ??????? ?? ? ???? ? ???  ??????? ?? 
????????????????????????????? ? ?????  ???? ? ???????? ???? ??  ???? ? ???????? ???? ??
? ??? ? ???  ? ???  ?? ???  ?  ?????   ? ??   ???? ? ? ? ?? ??  ? ??   ???? ? ? ? ?? ??
? ??  ? ? ? ?? ? ?  ?? ? ?  ???? ???     ?    ???? ? ? ? ?? ??    ?    ???? ? ? ? ?? ??
?  ?  ?   ? ?  ? ?     ? ?   ? ? ??    ?       ??? ? ? ? ?? ?   ?       ??? ? ? ? ?? ? 
      ?   ?      ?  ?    ?  ?? ?                 ?     ?  ?               ?     ?  ?   
                             ? ?                                                       

"""

header13 = """
 
   ?????????  ??   ??        ??       ???   ?       ???     ???    ??     ??   ???     ???     ???    ??     ??   ??? 
  ???    ??? ???  ???       ???       ???   ??? ??????????? ???    ???   ??? ????? ??????????? ???    ???   ??? ????? 
  ???    ??  ???? ???       ???       ?????????    ???????? ???    ???   ???????      ???????? ???    ???   ???????   
  ???        ???? ???       ???       ?????????     ???   ? ???    ???  ???????        ???   ? ???    ???  ???????    
???????????? ???? ???       ???       ???   ???     ???     ???    ??? ????????        ???     ???    ??? ????????    
         ??? ???  ???       ???       ???   ???     ???     ???    ???   ???????       ???     ???    ???   ???????   
   ??    ??? ???  ????    ? ????    ? ???   ???     ???     ???    ???   ??? ?????     ???     ???    ???   ??? ????? 
 ??????????  ??   ????????? ?????????  ???????     ??????   ?????????    ???   ???    ??????   ?????????    ???   ??? 
                  ?         ?                                            ?                                  ?         

"""

header14 = """

   ?????   ?? ?    ?    ??    ?   ????? ?   ?  ??  ????? ?   ?  ?? 
  ?     ?? ?? ?    ?      ?  ? ??? ?     ?  ??? ??? ?     ?  ???   
?  ?????   ?? ?    ?       ??      ?  ?   ? ???     ?  ?   ? ???   
 ??????    ?? ???? ????    ?      ?   ?   ? ?  ?   ?   ?   ? ?  ?  
            ?     ?    ? ??      ?    ?? ??   ?   ?    ?? ??   ?   
                                       ???   ?          ???   ?    
                                                                   
      
"""

header15 = """                                                                                             

:'######::'####:'##:::::::'##:::::::'##:::'##:'########:'##::::'##:'##:::'##:'########:'##::::'##:'##:::'##:
'##... ##:. ##:: ##::::::: ##:::::::. ##:'##::... ##..:: ##:::: ##: ##::'##::... ##..:: ##:::: ##: ##::'##::
 ##:::..::: ##:: ##::::::: ##::::::::. ####:::::: ##:::: ##:::: ##: ##:'##:::::: ##:::: ##:::: ##: ##:'##:::
. ######::: ##:: ##::::::: ##:::::::::. ##::::::: ##:::: ##:::: ##: #####::::::: ##:::: ##:::: ##: #####::::
:..... ##:: ##:: ##::::::: ##:::::::::: ##::::::: ##:::: ##:::: ##: ##. ##:::::: ##:::: ##:::: ##: ##. ##:::
'##::: ##:: ##:: ##::::::: ##:::::::::: ##::::::: ##:::: ##:::: ##: ##:. ##::::: ##:::: ##:::: ##: ##:. ##::
. ######::'####: ########: ########:::: ##::::::: ##::::. #######:: ##::. ##:::: ##::::. #######:: ##::. ##:
:......:::....::........::........:::::..::::::::..::::::.......:::..::::..:::::..::::::.......:::..::::..::
                                                                                          
"""

header16 = """

 .----..-..-.   .-. .-.  .-..-----..-. .-..-..-..-----..-. .-..-..-. 
{ {__-`{ |} |   } |  \ \/ / `-' '-'| } { || ' / `-' '-'| } { || ' /  
.-._} }| }} '--.} '--.`-\ }   } {  \ `-' /| . \   } {  \ `-' /| . \  
`----' `-'`----'`----'  `-'   `-'   `---' `-'`-`  `-'   `---' `-'`-` 
                                                                     
              
"""

header17 = """

 .d8888b.  d8b 888 888      88888888888       888  88888888888       888      
d88P  Y88b Y8P 888 888          888           888      888           888      
Y88b.          888 888          888           888      888           888      
 "Y888b.   888 888 888 888  888 888  888  888 888  888 888  888  888 888  888 
    "Y88b. 888 888 888 888  888 888  888  888 888 .88P 888  888  888 888 .88P 
      "888 888 888 888 888  888 888  888  888 888888K  888  888  888 888888K  
Y88b  d88P 888 888 888 Y88b 888 888  Y88b 888 888 "88b 888  Y88b 888 888 "88b 
 "Y8888P"  888 888 888  "Y88888 888   "Y88888 888  888 888   "Y88888 888  888 
                            888                                               
                       Y8b d88P                                               
                        "Y88P"                                                

"""

header18 = """
                                                              
 
      ___                       ___       ___       ___           ___           ___           ___           ___           ___           ___     
     /\  \          ___        /\__\     /\__\     |\__\         /\  \         /\__\         /\__\         /\  \         /\__\         /\__\    
    /::\  \        /\  \      /:/  /    /:/  /     |:|  |        \:\  \       /:/  /        /:/  /         \:\  \       /:/  /        /:/  /    
   /:/\ \  \       \:\  \    /:/  /    /:/  /      |:|  |         \:\  \     /:/  /        /:/__/           \:\  \     /:/  /        /:/__/     
  _\:\~\ \  \      /::\__\  /:/  /    /:/  /       |:|__|__       /::\  \   /:/  /  ___   /::\__\____       /::\  \   /:/  /  ___   /::\__\____ 
 /\ \:\ \ \__\  __/:/\/__/ /:/__/    /:/__/        /::::\__\     /:/\:\__\ /:/__/  /\__\ /:/\:::::\__\     /:/\:\__\ /:/__/  /\__\ /:/\:::::\__\
 \:\ \:\ \/__/ /\/:/  /    \:\  \    \:\  \       /:/~~/~       /:/  \/__/ \:\  \ /:/  / \/_|:|~~|~       /:/  \/__/ \:\  \ /:/  / \/_|:|~~|~   
  \:\ \:\__\   \::/__/      \:\  \    \:\  \     /:/  /        /:/  /       \:\  /:/  /     |:|  |       /:/  /       \:\  /:/  /     |:|  |    
   \:\/:/  /    \:\__\       \:\  \    \:\  \    \/__/         \/__/         \:\/:/  /      |:|  |       \/__/         \:\/:/  /      |:|  |    
    \::/  /      \/__/        \:\__\    \:\__\                                \::/  /       |:|  |                      \::/  /       |:|  |    
     \/__/                     \/__/     \/__/                                 \/__/         \|__|                       \/__/         \|__|    

"""

def lb_header():

    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))

helpMain = """
 Name                       Action
 ----                       ------
 Lookup                     Faire des recherches sur une personne. 
 Social engineering         Utiliser des outils pour du social engineering.
 Make file                  Creer un fichier '.txt' pour y ecrire les infos obtenu.
 Show Database              Accedez a la base de donnee.

 Exit                       Quitter le logiciel.
 Help                       Affiche se message.
 Clear                      Efface l'ecran."""

helpLookup = """
 Name                             Action
 ----                             ------
 Personne lookup                  Faire des recherches avec un nom, prenom et (ville).
 Username lookup                  Faire des recherches avec un pseudonyme.  
 Adresse lookup                   Faire des recherches avec une adresse.
 Phone lookup                     Faire des recherches avec un numero de telephone.
 IP lookup                        Faire des recherches avec une adresse IP.
 SSID locator                     Faire des recherches avec une adresse MAC/BSSID
 Email lookup                     Faire des recherches avec une adresse email.
 Mail tracer                      Faire des recherches avec l'entete d'un mail.
 Employés recherche               Recherche les employés d'une entreprise.
 Google search                    Faire des recherches sur google.
 Facebook graphSearch             Faire des recherche grace au graphSearch.
 twitter info                     Recuperer les informations d'un compte Twitter.
 instagram info                   Recuperer les informations d'un compte Instagram.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

helpOtherTool = """
 Name                             Action
 ----                             ------
 Hash decrypter                   Essaye de décrypter un hash via une base de donnée en ligne.

 Back main menu                   Revenir au menu principal.
 Exit script                      Pour quitter le logiciel.
 Clear screen                     Efface l'ecran."""

helpProfiler = """
 Name                      Action
 ----                      ------
 Search Profiles           Recherche un profile dans la base de donnee.
 Show all Profiles         Affiche tout les profiles de la base de donnee.

 Exit Database             Quitte la base de donnee pour retourner au menu principal.
 Help message              Affiche se message
"""

helpCountry = """
 Name                      Action
 ----                      ------
 FR                        Utiliser les services Francais.
 BE                        Utiliser les services Belge.
 CH                        Utiliser les services Suisse.
 LU                        Utiliser les services Luxembourgeois.
 All                       Utiliser tout les services.

 Back main menu            Revenir au menu principal.
 Exit script               Pour quitter le logiciel.
 Clear screen              Efface l'ecran."""

mainOption = """
 [1] Lookup
 [2] Other tool
 [3] Profiler
 [4] Change country

 [e] Exit script    [h] Help Message    [c] Clear Screen"""

text = ['Press F to hack', 'LEAVE ME HERE', 'The security is an illusion.', 'Profiler ctOS v2.0', 'DedSec takeover', 'Fsociety00.dat', 'Evil Corp',
 'Hello, friend', 'Hacking is our weapon', 'Hello, World', 'Login the world...', 'Big Brother is watching you.', 'Fuck Society', 'Wrench is calling...',
 'The control is an illusion.', 'install google_crack.exe...', 'you are free ! lol no, it was a joke.', 'you are a 1 or a 0 ?', 'Matraque: 1 - Genou: 0', 'Je veux que tu comprenne... Que tu ne sera plus jamais libre..', 'Tu pense être intouchable... Je vais briser tes illusion...',
 'je veux que tu sache... que tu n\'es plus anonyme...', 'Snapchat: T-Bone sent you a new message.', 'LulzSec <3 <3', '<3 Kraken Security OS is bae <3', 'DedSec is now in LinkedIn !',
 'FRANCE World champion 2018 !!', '~~(8:> is Defalt ~~(8:>', 'Facebook: Neo in a relationship with Elliot Alderson.', 'Just.. fuck the society.', 'locating 127.0.0.1 ... No match found', 
 '101100100101100 01100110010110011001', '101100 0110011001', 'c2V5cHRvbyBteSBsb3Zl', '1 item in your web hisotry: \'Fkk cuckold how to make your wife a hotwife zootube\'', '49 20 4c 4f 56 45 20 55', 'NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6VUS3OKVZGQYSLJQ3GO===', 'Regarde derrière toi...',
 'dW4gZCdldXggdHJvdWUgw6AgcXUnYSB0J3JlIHNlaW4gcXVlIHNpIGNlIGNldHRl', 'Send me nudes: Harry.Truman@nsa.gov', "Access point 'AP-Zone51' was found nearby."]

lookupOption = """
 [1] Personne lookup          [8] Mail tracer                     
 [2] Username lookup          [9] Employés recherche
 [3] Adresse lookup           [10] Google search
 [4] Phone lookup             [11] Facebook GraphSearch          
 [5] IP lookup                [12] twitter info
 [6] SSID locator             [13] instagram info
 [7] Email lookup             

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen"""

otherToolOption = """
 [1] Hash decrypter

 [b] back main menu    [e] Exit script    [h] Help Message    [c] Clear Screen 
"""

profilerOption = """
 [1] Profiler
 [2] Show all Profiles   
 [3] Create profile

 [b] back main menu    [c] Clear screen   [h] Help message
"""

countryMenu = """
 [1] FR (France)     [4] LU (Luxembourg) 
 [2] BE (Belgique)   [5] All (FR, BE, CH, LU)
 [3] CH (Suisse)

 [e] back main menu   [c] Clear screen   [h] Help message
"""

def menu():

	pr = Profiler()
	pr.loadDatabase(pathDatabase)
	sizeOfDB = pr.size
	nbProfilesBDD = pr.count

	menu = """
                         
        ____  
        o8%8888,    
      o88%8888888.  
     8'-    -:8888b                         Time:      [ %s | %s ]
    8'         8888                           Author:    [ Akshay Dhawan ]      
   d8.-=. ,==-.:888b                    Version:   [ %s ]              
   >8 `~` :`~' d8888                   Pays:      [ %s | %s ]
   88         ,88888                       Database:  [ %s | %s Ko ]  
   88b. `-~  ':88888                                    %s
   888b ~==~ .:88888 
   88888o--:':::8888      
   `88888| :::' 8888b  
   8888^^'       8888b  
  d888           ,%888b.   
 d88%            %%%8--'-.  
/88:.__ ,       _%-' ---  -  
    '''::===..-'   =  --.                                       
"""
 % (Fore.YELLOW+str(today_date)+Fore.RESET, Fore.YELLOW+times()+Fore.RESET, 
		   Fore.YELLOW+str(__version__)+Fore.RESET, 
		   Fore.CYAN+monpays+Fore.RESET, codemonpays,
		   Fore.GREEN+str(nbProfilesBDD)+Fore.RESET, Fore.RED+str(sizeOfDB)+Fore.RESET,
		   random.choice(text)
		  )
	
	print(lb_header())
	print(menu)

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n NoobTracker("+Fore.BLUE + "~" + Fore.RESET + ")$ ")
	
		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = Profiler()
				pr.loadDatabase(pathDatabase)
				database = pr.database
				
				choix = input("\n NoobTracker("+Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")

				if choix.lower() == 'h':
					print(helpMsg)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e':
					sys.exit("\n"+information+" Bye ! :)")
				elif choix.lower() == "1":
					profile = input(" Profil: ")
					data = pr.searchDatabase(profile, database=database)
					profilerFunc(data, path=pathDatabase)
					
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Format: Prenom Nom)"+Fore.RESET)
					name = input(" Nom du Profil: ")
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					twitter = input(" Twitter: ")
					# print(found+" %s" % (twitter))
					instagram = input(" Instagram: ")
					# print(found+" %s" % (instagram))
					facebook = input(" Facebook: ")
					# print(found+" %s" % (facebook))

					info = {"URL": {"Twitter": twitter, "Facebook":facebook, "Instagram": instagram}}
					create = pr.writeProfile(fileName=name, path=pathDatabase, info=info)

					if create:
						print("\n"+found+" Le profil '%s' a été créé avec succès." % (name))
					else:
						print("\n"+warning+" Une erreur est survenue. Le profil '%s' n'a pas pu être créé." % (name))

		elif choix.lower() == 'e':
			sys.exit("\n"+information+" Bye ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n NoonbTracker("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '4':
					searchNumber(codemonpays)
				elif lookup.lower() == '7':
					SearchEmail()
				#  ...
				elif lookup.lower() == '3':
					searchAdresse(codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Commande introuvable")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n NoonbTracker("+Fore.BLUE+"OtherTool"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n NoobTracker("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					codemonpays = "FR"
					monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					codemonpays = "BE"
					monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					codemonpays = "CH"
					monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					codemonpays = "LU"
					monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					codemonpays = "XX"
					monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMsg)
		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Bye ! :)")