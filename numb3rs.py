import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        num1,num2,num3,num4=ip.split(".")
        
        if 0<=int(num1)<=255 and 0<=int(num2)<=255 and 0<=int(num3)<=255 and 0<=int(num4)<=255:
            return True
        else: 
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    main()