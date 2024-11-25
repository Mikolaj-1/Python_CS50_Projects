def main():
    answers=[42,"forty-two","forty two"]
    answer=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if answer.lower() in answers:
        print("Yes")
    else: print("No")
main()