from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = CoffeeMaker()
my_menu = Menu()
money_process = MoneyMachine()

machine_turn_off = False

while not machine_turn_off:
    options = my_menu.get_items()
    select = input(f"What would you like? ({options}): ")

    if select == "report":
        my_machine.report()
        money_process.report()
    elif select == "off":
        machine_turn_off = True
    else:
        drink = my_menu.find_drink(select)
        if my_machine.is_resource_sufficient(drink) and money_process.make_payment(drink.cost):
            my_machine.make_coffee(drink)