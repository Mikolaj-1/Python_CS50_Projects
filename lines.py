import sys

def main():
    lines=0
    type=sys.argv[1].split(".")
    try:
        if(len(sys.argv)>2):
            print("Too much argumnets")
            sys.exit(1)
        if(len(sys.argv)<2):
            print("Too less argumnets")
            sys.exit(1)
        if type[-1]!="py":
            print("Not a python file")
            sys.exit(1)
        with open(sys.argv[1]) as file:
            for row in file:
                if row.lstrip().startswith("#") or row.rstrip()=="":
                    pass
                else: lines=lines+1
        print(lines)
    except FileNotFoundError:
        print('File do not found')
        sys.exit(1)
    

main()