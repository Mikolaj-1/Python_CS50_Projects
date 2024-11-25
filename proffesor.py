import random

def main():
    get_level()
    
def get_level():
    try:
        level=int(input("Level: "))
    except ValueError:
        main()
    if(1<=level<=3):
        generate_integer(level)
    else: main()


def generate_integer(level):
    score=10
    if level==1:
        for i in range(10):
            num1=random.choice(range(0,10))
            num2=random.choice(range(0,10))
            for attempt in range(3):
                try:
                    print(f"{num1} + {num2} =",end=" ")
                    answer=int(input(" "))
                except ValueError:
                    print("EEE")
                if(answer==num1+num2):
                    break
                else: print("EEE")
                if(attempt==2):
                    print(f"{num1} + {num2} = {num1+num2}")
                    score=score-1
        print(f"score: {score}")
    elif level==2:
        for i in range(10):
            num1=random.choice(range(10,100))
            num2=random.choice(range(10,100))
            for attempt in range(3):
                try:
                    print(f"{num1} + {num2} =",end=" ")
                    answer=int(input(" "))
                except ValueError:
                    print("EEE")
                if(answer==num1+num2):
                    break
                else: print("EEE")
                if(attempt==2):
                    print(f"{num1} + {num2} = {num1+num2}")
                    score=score-1
        print(f"score: {score}")
    else:
        for i in range(10):
            num1=random.choice(range(100,1000))
            num2=random.choice(range(100,1000))
            for attempt in range(3):
                try:
                    print(f"{num1} + {num2} =",end=" ")
                    answer=int(input(" "))
                except ValueError:
                    print("EEE")
                if(answer==num1+num2):
                    break
                else: print("EEE")
                if(attempt==2):
                    print(f"{num1} + {num2} = {num1+num2}")
                    score=score-1
        print(f"score: {score}")

    


if __name__ == "__main__":
    main()