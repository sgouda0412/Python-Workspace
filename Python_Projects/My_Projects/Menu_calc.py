burger = {'hamburger': 6.99, 'cheeseburger': 7.99, 'bacon cheeseburger': 8.99}
sides = {'fries': 1.99, 'macncheese': 1.99, 'salad': 0.99}
drink = {'coke': 1.99, 'milkshake': 2.50, 'water': 0.99}

price = 0

userburg = int(input("What burger would you like?:\n1) Hamburger\n2) Cheeseburger\n3) Bacon Cheeseburger\n"))
usersides = int(input("What sides would you like?:\n1) French Fries\n2) Mac and Cheese\n3) Salad\n"))
userdrink = int(input("Which drink would you like?:\n1) Coke\n2) Milkshake\n3) Water\n"))

if userburg == 1:
    price = burger.setdefault('hamburger')
    print(price)
    if usersides == 1:
        price += sides.setdefault('fries')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 2:
        price += sides.setdefault('macncheese')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 3:
        price += sides.setdefault('salad')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
elif userburg == 2:
    price = burger.get('cheeseburger')
    print(price)
    if usersides == 1:
        price += sides.setdefault('fries')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 2:
        price += sides.setdefault('macncheese')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 3:
        price += sides.setdefault('salad')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
elif userburg == 3:
    price = burger.get('bacon cheeseburger')
    print(price)
    if usersides == 1:
        price += sides.setdefault('fries')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 2:
        price += sides.setdefault('macncheese')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
    elif usersides == 3:
        price += sides.setdefault('salad')
        print(price)
        if userdrink == 1:
            price += drink.setdefault('coke')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 2:
            price += drink.setdefault('milkshake')
            print(f"The total price for your meal comes to £{price}")
        elif userdrink == 3:
            price += drink.setdefault('water')
            print(f"The total price for your meal comes to £{price}")
else:
    print("Please choose an item from the menu using the number selector beside it!")


