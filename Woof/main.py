import os
import time

#!/usr/bin/env python3


def main():
    print("PALAMAGOO DATING SIM")
    print("===--------------===")

    print("===========")
    print("=  o   o  =")
    print("=    |    =")
    print("=         =")
    print("=  \___/  =")
    print("===========")
    print()
    print("Welcome to the game")
    print("Enter your name down below.")
    name = str(input("> "))
    print()
    time.sleep(2)
    os.system('clear')
    if name.lower() == "palamagoo":
        print("===\===/===")
        print("=  o   o  =")
        print("=    |    =")
        print("=   ___   =")
        print("=  /   \  =")
        print("===========")
        print()
        print("Thats... MY NAME!!!! YOU LITTLE PIECE OF SHIT")
        print("You were brutally stabbed 28.3 times")
    else:
        print("So, you're name is " + name + "? What a loveeeeely name. My name Palamagoo!!")
        print("So what do you wanna do today my lovely little darling lovely?")
    


if __name__ == '__main__': main()