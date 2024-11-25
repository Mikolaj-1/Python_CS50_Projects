months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while(True):
        date=input("Date: ")
        try:
            list=date.split("/")
            day=int(list[1])
            if day>31 or day<1:
                day=0
            if day>0 and day<10:
                day=f"0{day}"
            if list[0] in months:
                    month=int(months.index(list[0])+1)
                    if month>12 or month<1:
                        month=0
                    if month>0 and month<10:
                        month=f"0{month}"
                    else: month=0
            else:
                month=int(list[0])
                if month>12 or month<1:
                    month=0
                if month>0 and month<10:
                    month=f"0{month}"
            year=int(list[2])
            if day==0 or month==0:
                pass
            else: 
                print(f"{year}-{month}-{day}")
                break
        except IndexError:
            try:
                list=date.split(" ")
                if list[0] in months:
                    month=int(months.index(list[0])+1)
                    if month>12 or month<1:
                        month=0
                    if month>0 and month<10:
                        month=f"0{month}"
                    year=int(list[2])
                    if "," in list[1]:
                        i=list[1].find(",")
                        day=int(list[1][0:i])
                    else:
                        day=0
                        month=0
                    if day>31 or day<1:
                        day=0
                    if day>0 and day<10:
                        day=f"0{day}"
                else:
                    day=0
                    month=0
                if day==0 or month==0:
                    pass
                else: 
                    print(f"{year}-{month}-{day}")
                    break
            except IndexError:
                pass

main()