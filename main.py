from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
MU = Menu()
CM = CoffeeMaker()
MM = MoneyMachine()

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CM.report()
        MM.report()
    else:
        drink = MU.find_drink(choice)
        if CM.is_resource_sufficient(drink) and MM.make_payment(drink.cost):
            CM.make_coffee(drink)



