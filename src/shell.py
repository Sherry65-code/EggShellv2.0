# Made by Parambir Singh
# This program is avaliable on github at https://github.com/Sherry65-code/EggShellv2.0
# This program is licensed under GNU GENERAL PUBLIC LICENSE 3.0

# All Imports <1>

from colorama import Fore
from os import getcwd, name, system, chdir, makedirs, listdir, remove, removedirs
# End 1

# How to edit and where to go <3>

# End 3

# All Variables <4>

name="EggShellv2.0"
ver="1.0.0"
maincolor="white"
# End 4

# All Functions <5>
    

def changeColorTo(colorname):
    if (colorname == "white"):
        print(Fore.WHITE,end="")
    elif (colorname == "green"):
        print(Fore.GREEN,end="")
    elif (colorname == "yellow"):
        print(Fore.YELLOW,end="")
    elif (colorname == "red"):
        print(Fore.RED,end="")
    elif (colorname == "blue"):
        print(Fore.BLUE, end="")
    elif (colorname == "cyan"):
        print(Fore.CYAN, end="")
    elif (colorname == "system"):
        print(Fore.RESET,end="")
    return 0

def getOrignalString(start):
    x=start-1
    data=""
    try:
        while True:
            x+=1
            data+=query[x]+" "
    except Exception as e:
        pass
    return data

# End 5

# Main <2>
if (name == "nt"):
    system("cls")
else:
    system("clear")

changeColorTo("green")
print(f"{name} Version {ver}")
while True:
    changeColorTo("yellow")
    print(f"{getcwd()}>>",end="")
    changeColorTo(maincolor)
    inp = input()
    query = inp.split(" ")
    if (query[0] == "clear"):
        if (name == "nt"):
            system("cls")
        else:
            system("clear")
    elif (query[0] == "invert"):
        x=0
        while (x<=100):
            print(" ")
            x+=1
    elif (query[0] == "bye"):
        break
    elif (query[0] == ""):
        pass
    elif (query[0] == "gcwd"):
        print(f"{getcwd()}")
    elif (query[0] == "cd"):
        chdir(f"{query[1]}")
    elif (query[0] == "show"):
        endr = getOrignalString(1)
        print(endr)
    elif (query[0] == "color"):
        maincolor=f"{query[1]}"
    elif (query[0] == "newdir"):
        x=0
        try:
            while True:
                x+=1
                data=query[x]
                makedirs(f"{data}")
        except Exception as e:
            pass
    elif (query[0] == "remdir"):
        if (query[1] == "-S"):
            endr = getOrignalString(2)
            removedirs(f"{endr.rstrip(endr[-1])}")
        else:
            x=0
            try:
                while True:
                    x+=1
                    data=query[x]
                    removedirs(f"{data}")
            except Exception as e:
                pass
    elif (query[0] == "rem"):
        if (query[1] == "-S"):
            datar = getOrignalString(2)
            remove(datar)
        else:
            x=0
            try:
                while True:
                    x+=1
                    remove(f'{query[x]}')
            except Exception as e:
                pass
    elif (query[0] == "newfile"):
        if (query[1] == "-S"):
            datar = getOrignalString(2)
            fl = open(f"{datar}","w")
            fl.write(" ")
            fl.close()
        else:
            x=0
            try:
                while True:
                    x+=1
                    fl = open(f"{query[x]}","w")
                    fl.write(" ")
                    fl.close()
            except Exception as e:
                pass
    else:
        print(f"'{query[0]}' is an unknown command")
# End 2