import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time=""
    if match :=re.search(r"^([1-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([1-9][0-2]?):?([0-5][0-9])? (AM|PM)$",s):
        if(match.group(2)!=None and match.group(5)==None):
            if(match.group(3)=="AM"):
                if(match.group(1)=="12"):
                    time+="0"
                else:time+=match.group(1)
                time+=":"+match.group(2)+ " to "
            else: 
                if match.group(1)==12:
                    time+="12"
                else: time+=str(int(match.group(1))+12)
                time+=":"+match.group(2)+" to "
            if(match.group(6)=="AM"):
                if(match.group(4)=="12"):
                    time+="0"                   
                else:time+=match.group(4)
                time+=":"+"00"
            else: 
                if match.group(4)==12:
                    time+="12"
                else: time+=str(int(match.group(4))+12)
                time+=":"+"00"
            return time
        
        if(match.group(2)==None and match.group(5)!=None):
            if(match.group(3)=="AM"):
                if(match.group(1)=="12"):
                    time+="0"
                else:time+=match.group(1)
                time+=":"+"00"+ " to "
            else: 
                if match.group(1)==12:
                    time+="12"
                else: time+=str(int(match.group(1))+12)
                time+=":"+"00"+" to "
            if(match.group(6)=="AM"):
                if(match.group(4)=="12"):
                    time+="0"                   
                else:time+=match.group(4)
                time+=":"+match.group(5)
            else: 
                if match.group(4)==12:
                    time+="12"
                else: time+=str(int(match.group(4))+12)
                time+=":"+match.group(5)
            return time
                
        if(match.group(5)!=None and match.group(3)!=None):
            if(match.group(3)=="AM"):
                if(match.group(1)=="12"):
                    time+="0"
                else:time+=match.group(1)
                time+=":"+match.group(2)+ " to "
            else: 
                if match.group(1)==12:
                    time+="12"
                else: time+=str(int(match.group(1))+12)
                time+=":"+match.group(2)+" to "
            if(match.group(6)=="AM"):
                if(match.group(4)=="12"):
                    time+="0"                   
                else:time+=match.group(4)
                time+=":"+match.group(5)
            else: 
                if match.group(4)==12:
                    time+="12"
                else: time+=str(int(match.group(4))+12)
                time+=":"+match.group(5)
            return time
    
        else:
            if(match.group(3)=="AM"):
                if(match.group(1)=="12"):
                    time+="0"
                else:time+=match.group(1)
                time+=":"+"00"+ " to "
            else: 
                if match.group(1)==12:
                    time+="12"
                else: time+=str(int(match.group(1))+12)
                time+=":"+"00"+" to "
            if(match.group(6)=="AM"):
                if(match.group(4)=="12"):
                    time+="0"                   
                else:time+=match.group(4)
                time+=":"+"00"
            else: 
                if match.group(4)==12:
                    time+="12"
                else: time+=str(int(match.group(4))+12)
                time+=":"+"00"
            return time
        
    else: return False



if __name__ == "__main__":
    main()