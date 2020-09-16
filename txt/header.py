import os ,random,colorama 
fore = colorama.Fore
try :
    header1 =fore.GREEN+str(os.popen("figlet -f big sillytuktuk").read())
except : 
    os.system("pkg install figlet")
    header1 =fore.GREEN+str(os.popen("figlet -f big sillytuktuk").read())
def lb_header():
    headers = [header1]
    return(random.choice(headers))

