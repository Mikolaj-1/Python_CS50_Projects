import requests
import sys
def main():
    req=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    json=req.json()
    rate=json["bpi"]["USD"]["rate_float"]
    try:
        if(len(sys.argv)==1):
            print("Missing command-line argument")
            sys.exit(1)
        if(len(sys.argv)>2):
            print("Too much command-line argument")
            sys.exit(1)
        value=float(sys.argv[1])
        print(f"${value*rate:,}")

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    

        

    
            

main()