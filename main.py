from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# menu_item = MenuItem


is_run = True
while is_run :
    choice = input(f"What would you like? ({menu.get_items()}) ").lower()
    if choice == "report" :
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_run = False
    else :
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

