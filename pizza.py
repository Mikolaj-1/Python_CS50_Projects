import sys
import csv
from tabulate import tabulate


def main():
    type=sys.argv[1].split(".")
    if(len(sys.argv)<2):
        print("Too less argumnets")
        sys.exit()
    if(len(sys.argv)>2):
        print("Too much argumnets")
        sys.exit()
    if(type[1]!="csv"):
        print("Wrong type")
        sys.exit(1)

    with open(sys.argv[1]) as file:
        reader=csv.reader(file)
        i=0
        menu=[]
        for pizza,small,big in reader:
            menu.append([pizza,small,big])

        print(tabulate(menu, headers="firstrow" ,tablefmt="grid"))

main()
