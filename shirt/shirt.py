import sys
from PIL import Image, ImageOps

def main():
    try:
        size=600,600
        if len(sys.argv)>3:
            print("Too much arguments!")
            sys.exit(1)
        if len(sys.argv)<3:
            print("Too less argumensts!")
            sys.exit(1)
        type1=sys.argv[1].split(".")
        type2=sys.argv[2].split(".")
        if(type1[1]!="jpg" and type1[1]!="jpeg" and type1[1]!="png" and type2[1]!="jpg" and type2[1]!="jpeg" and type2[1]!="png"):
            print("Invalid input data")
            sys.exit(1)
        if(type1[1]!=type2[1]):
            print("Invalid input data")
            sys.exit(1)
    except IndexError:
        print("Invalid input data")
        sys.exit(1)
    try:
        shirt=Image.open("shirt.png")
        image=Image.open(sys.argv[1])
        sizedImage=ImageOps.fit(image,size)
        sizedImage.paste(shirt,shirt)
        sizedImage.save(sys.argv[2])
    except FileNotFoundError:
        print("File do not exist")
        sys.exit(1)

    
    


main()