MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# TODO 1. Prompt user
while True:
    # print("What would you like?(espresso/latte/cappuccino): ")
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print("Water: %dml" % resources["water"])
        print("Milk: %dml" % resources["milk"])
        print("Coffee: %dgm" % resources["coffee"])
        print("Money: $%0.2f" % resources["money"])
    elif choice == "latte":
        if MENU["latte"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please Insert Coins")
            quarters = int(input("How many quarters?: "))
            nickels = int(input("How many nickels?: "))
            dimes = int(input("How many dimes?: "))
            pennies = int(input("How many pennies?: "))
            total_money = float((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25))
            if total_money >= MENU["latte"]["cost"]:
                print("Here is $%0.2f in change" % (total_money - MENU["latte"]["cost"]))
                print("Here is your latte ☕ Enjoy")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + MENU["latte"]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
        elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please Insert Coins")
            quarters = int(input("How many quarters?: "))
            nickels = int(input("How many nickels?: "))
            dimes = int(input("How many dimes?: "))
            pennies = int(input("How many pennies?: "))
            total_money = float((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25))
            if total_money >= MENU["cappuccino"]["cost"]:
                print("Here is $%0.2f in change" % (total_money - MENU["cappuccino"]["cost"]))
                print("Here is your cappuccino ☕ Enjoy")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + MENU["cappuccino"]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            print("Sorry there is not enough water.")
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please Insert Coins")
            quarters = int(input("How many quarters?: "))
            nickels = int(input("How many nickels?: "))
            dimes = int(input("How many dimes?: "))
            pennies = int(input("How many pennies?: "))
            total_money = float((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25))
            if total_money >= MENU["espresso"]["cost"]:
                print("Here is $%0.2f in change" % (total_money - MENU["espresso"]["cost"]))
                print("Here is your espresso ☕ Enjoy")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] = resources["money"] + MENU["espresso"]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Wrong Input")
