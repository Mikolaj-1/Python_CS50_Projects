def main():
    number=convert(input("What time is it? "))
    if number>=7 and number<=8:
        print ("breakfast time")
    elif number>=12 and number<=13:
        print ("lunch time")
    elif number>=18 and number<=19:
        print ("dinner time")

def convert(time):
    try:
        list=time.split(":")
        hours=list[0]
        minutes=list[1]
        number=float(hours)+(float(minutes)/60)
        return number
    except IndexError:
        return "Something went wrong"

if __name__ == "__main__":
    main()