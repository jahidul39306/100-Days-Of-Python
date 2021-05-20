from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    # menu.get_items()
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        break

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif menu.find_drink(choice):
        drink_name = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_name):
            if money_machine.make_payment(drink_name.cost):
                coffee_maker.make_coffee(drink_name)
