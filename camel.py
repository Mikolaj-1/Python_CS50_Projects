def main():
    snake_case=""
    camel=str(input("camelCase: "))
    for case in camel:
        if case.isupper():
            snake_case+=f"_{case.lower()}"
        else: snake_case+=case
    print (f"snake_case: {snake_case}")
main()