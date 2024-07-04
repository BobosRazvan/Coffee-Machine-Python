import data

turn_off = False
money = 0.0


def check_resources(choice):
    for item in data.MENU[choice]["ingredients"]:
        if data.MENU[choice]["ingredients"][item] > data.resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def choice_selected(choice):
    global money

    if check_resources(choice):
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        money += total
        if money >= data.MENU[choice]["cost"]:
            money = money - data.MENU[choice]["cost"]
            print(f"Here is ${money} in change.")
            return 1
        else:
            print("Sorry that's not enough money. Money refunded.")
            return 0
    else:
        return 0


while not turn_off:
    print("What would you like? (espresso/latte/cappuccino/report/turn off the coffee machine): ")
    choice = input()

    if choice == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${money}")

    elif choice == "espresso":
        if choice_selected(choice) == 0:
            continue
        else:
            data.resources["water"] -= data.MENU[choice]["ingredients"]["water"]
            data.resources["coffee"] -= data.MENU[choice]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")

    elif choice == "latte":
        if choice_selected(choice) == 0:
            continue
        else:
            data.resources["water"] -= data.MENU[choice]["ingredients"]["water"]
            data.resources["milk"] -= data.MENU[choice]["ingredients"]["milk"]
            data.resources["coffee"] -= data.MENU[choice]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")

    elif choice == "cappuccino":
        if choice_selected(choice) == 0:
            continue
        else:
            data.resources["water"] -= data.MENU[choice]["ingredients"]["water"]
            data.resources["milk"] -= data.MENU[choice]["ingredients"]["milk"]
            data.resources["coffee"] -= data.MENU[choice]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")

    elif choice == "turn off the coffee machine":
        turn_off = True
        print("Goodbye! Thank you for using the Coffee Machine.")
    else:
        print("Invalid choice. Please try again.")
