import time
import random
import os

def printSlow(text):
    """
    Prints text then sleeps for a second to ensure the player can read what is being outputted, very shrimple
    """
    print(text)
    time.sleep(1)

printSlow("TERMINAL")
printSlow("Made by Josh.")
on = True

while on == True: ## loop of everything that will happen
    try:
        ask = input("->")
        ask = input.lower()

        if ask == "help":
            printSlow("Current list of commands:")
            print("help - ask for help with commands")
            print("list - list all currently available functions")
            print("mini - opens a mini file handler and text writer")

        if ask == "list":
            printSlow("Implemented functions:")
            print("- basic commands")
            print("- very complex list of commands and functions (see here)")

        if ask == "mini":

                    
