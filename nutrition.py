nutrition={"apple":130,"banana":110,"grapefruit":60,"honeydew melon":50,"lemon":15,
       "nectarine":60,"peach":60,"pineapple":50,"strawberries":50,"tangerine":50,"avocado california":50,
       "cantaloupe":50,"grapes":90,"kiwifruit":90,"lime":20,"orange":80,"pear":100,"plums":70,"sweet cherries":100,"watermelon":80}

def main():
    item=str(input("Item: "))
    if item.lower() in nutrition:
        print(f"Calories: {nutrition[item.lower()]}")
main()