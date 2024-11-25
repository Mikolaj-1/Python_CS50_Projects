def main():
    try:
        expression=input("Expression: ")
        list=expression.split(' ')
        x=int(list[0])
        type=list[1]
        y=int(list[2])
        match type:
            case "+":
                print(float(x+y))
            case "-":
                print(float(x-y))
            case "*":
                print(float(x*y))
            case "/":
                print(float(x/y))
            case _:
                print("Something went wrong")
    except IndexError:
        ...
    
main()