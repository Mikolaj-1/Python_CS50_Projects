def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    chars=set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums=set("123456789")
    j=0
    n=0
    if len(s)>6 or len(s)<2 :
        return False
    else:
        for i in s:
            if(i in nums):
                n+=1
            if(i.upper() in chars):
                j+=1
            if(i.upper() in chars and n!=0):
                return False
            if(i in nums and j==0):
                return False
            if n==0 and i=="0":
                return False
            if(i=="," or i=="." or i=="/"):
                return False
        if j>1:
            return True
        else: return False


main()
