import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    i=0
    sentence=s.split(" ")
    for word in sentence:
        if re.search(r"^UM(\.|,|!|\?)?$",word.upper()):
            i=i+1
    return i



if __name__ == "__main__":
    main()