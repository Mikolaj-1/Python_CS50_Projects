def main():
    value=str(input("Input: "))
    shorten(value)


def shorten(value):
    out=""
    for word in value:
        if word.upper()=="A" or word.upper()=="E" or word.upper()=="I" or word.upper()=="O" or word.upper()=="U":
            pass
        else:
            out+=word
    print(f"Output: {out}")

if __name__ == "__main__":
    main()

