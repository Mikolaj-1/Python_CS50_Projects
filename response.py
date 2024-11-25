import validators

def main():
    print(valid(input("What's your email adress? ")))

def valid(mail):
    if validators.email(mail):
        return "Valid"
    else: return "Invalid"

if __name__ == "__main__":
    main()