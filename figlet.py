from pyfiglet import Figlet
import random
import requests
import sys


figlet=Figlet()
if(len(sys.argv)!=1 or len(sys.argv)!=3):
    sys.exit()
if(len(sys.argv)==3):
    if(sys.argv[1]!="-f" or sys.argv[1]!="--font"):
        print("Invalid usage")
        sys.exit()
        
    text=input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))
if(len(sys.argv)==1):
    text=input("Input: ")
    font=random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(figlet.renderText(text))




