def main():
    list=[]
    before=""
    while(True):
        try:
            item=str(input(""))
            if(item==""):
                break
            list.append(item.strip().upper())
        except EOFError:
            break
    list.sort()
    for item in list:
        if item==before:
            pass
        else:
            times=list.count(item)
            print(times ,item)
            before=item


main()
