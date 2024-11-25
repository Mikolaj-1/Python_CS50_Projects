import sys

def main():
    Total=0
    menu={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    while(True):
        try:
            order=input("Item: ")
        except EOFError:
            print("/n")
            sys.exit(0)
        try:
            Total=Total+menu[order.title()]
            print(f"Total: ${Total:.2f}")
        except KeyError:
            pass
    

main()
