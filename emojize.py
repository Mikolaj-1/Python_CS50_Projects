import emoji
def main():
    prompt=str(input("Input: "))
    print(emoji.emojize(prompt,language ="alias"))
main()