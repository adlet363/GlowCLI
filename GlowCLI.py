import sys
import time
from datetime import datetime, date
import platform
import os
import locale
# Text color
def Black(Blacktext):
    return("\033[30m{}\033[0m".format(Blacktext))

def Red(Redtext):
    return("\033[31m{}\033[0m".format(Redtext))

def Green(Greentext):
    return("\033[32m{}\033[0m".format(Greentext))

def Yellow(Yellowtext):
    return("\033[33m{}\033[0m".format(Yellowtext))

def Blue(Bluetext):
    return("\033[34m{}\033[0m".format(Bluetext))

def Purple(Purpletext):
    return("\033[35m{}\033[0m".format(Purpletext))

def Cyan(Cyantext):
    return("\033[36m{}\033[0m".format(Cyantext))

def White(Whitetext):
    return("\033[37m{}\033[0m".format(Whitetext))


# Watch ASCII
digits = {
    "0": [" ### ", "#   #", "#   #", "#   #", " ### "],
    "1": ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],
    "2": [" ### ", "    #", " ### ", "#    ", "#####"],
    "3": [" ### ", "    #", " ### ", "    #", " ### "],
    "4": ["#   #", "#   #", " ### ", "    #", "    #"],
    "5": [" ### ", "#    ", " ### ", "    #", " ### "],
    "6": ["#####", "#    ", "#####", "#   #", "#####"],
    "7": ["#####", "   ##", "  ## ", " ##  ", "##   "],
    "8": [" ### ", "#   #", " ### ", "#   #", " ### "],
    "9": ["#####", "#   #", "#####", "    #", " ####"],
    ":": ["  ## ", "  ## ", "     ", "  ## ", "  ## "]
}


os.system("cls" if os.name == "nt" else "clear")

current_time = time.strftime("%H:%M")

def time():
        for row in range(5):
            for char in current_time:
                print(Green(digits[char][row]), end="  ")
            print()
        
#Saturn

username = os.environ.get('USERNAME')
now = datetime.now()
Saturn = f'''
                                              _.oo.       
                    _.uuuu[[[/;:,.         .odMMMMMM'     
                 .o888UUUUU[[[[/;:-.   .o@P^   MMM^       {Red("Username:")} {Yellow(username)}
                ON88888UUUUU[[[[/;::-.        dP^         {Red("Rython virsion:")} {Yellow(sys.version.split()[0])}
               dNMMNN888UUUUU[[[[/;:--.   .o@P^           {Red("GlowCLI virsion")}: {Yellow("0.0.1")}
              MMMMMMN888UUUUU[[[/;::-. o@^                {Red("Date")}: {Yellow(now.strftime('%Y-%m-%d'))}
              NNMMMNN888UUUUU[[[[/~.o@P^                  {Red("Time:")}: {Yellow(now.strftime('%H-%M-%S'))}
              888888888UUUUU[[[[/o@^-..                   {Red("Os:")} {Yellow(platform.system())}
             oI8888UUUUU[[[[/o@P^:--..                    {Red("country:")} {Yellow(locale.getlocale()[0])}
          .@^  YUUUUU[[[[/o@^;::---..                     
        oMP     YUUU[[/oo@P^;:::--..                      {Red('##')}{Yellow('##')}{Purple('##')}{Black('##')}{Cyan('##')}{Green('##')}{Blue('##')}##
     .dMMM        ^/oo@^ ^;:-..                           ##{Red('##')}{Yellow('##')}{Purple('##')}{Black('##')}{Cyan('##')}{Green('##')}{Blue('##')}
    dMMMMMMMMMMMMMM@^  ^^^^^                              
     YMMMMMMUP^
       ^^^^  

'''
def CLI():
    print(Saturn)
