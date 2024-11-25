def main():
    greeting=str(input("Greeting: "))
    money=value(greeting)
    print (f"${money}")

def value(greeting):
    sentence=""
    i=100
    for word in greeting:
        sentence+=word
        if sentence.strip()=="Hello" or sentence.strip()=="hello":
            i=0;
        elif sentence=="H" or sentence=="h":
            i=20
    return i

main()
