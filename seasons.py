from datetime import date
import sys
import inflect
p = inflect.engine()


def main():
    print(birth(input("Date of birth: ")))


def birth(birth):
    try:
        today=date.today()
        elem=birth.split("-")
        newdate=date(int(elem[0]),int(elem[1]),int(elem[2]))
        minus=today-newdate
        days=minus.days
        minutes=days*24*60
        return p.number_to_words(minutes, andword="").capitalize() +" minutes"
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
