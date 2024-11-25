def main():
    sum=50
    coins=[25,10,5]
    while(sum>0):
        print(f"Amount due: {sum}")
        coin=int(input(f"Insert coin: "))
        if coin in coins:
            sum=sum-coin
        else: pass
    print(f"Change Owed: {-sum}")

main()