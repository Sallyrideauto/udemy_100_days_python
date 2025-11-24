from importlib.resources import is_resource
from platform import machine

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
    "money": 0
}

machine_turn_off = False

# TODO: Check resources sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! there is not enough {item}.")
            return False
    return True

# TODO: Process Coins
def process_coins(menu, cost, order_ingredients):
    print("Please insert coins.")
    insert_quarter = int(input("how many quarters?: "))
    insert_dime = int(input("how many dimes?: "))
    insert_nickle = int(input("how many nickles?: "))
    insert_penny = int(input("how many pennies?: "))

    insert_quarter *= 0.25
    insert_dime *= 0.10
    insert_nickle *= 0.05
    insert_penny *= 0.01

    insert_total = insert_quarter + insert_dime + insert_nickle + insert_penny

    # TODO: Check transaction successful
    if insert_total >= cost:
        insert_total -= cost
        resources["money"] += cost
        insert_total = '{:.2f}'.format(insert_total)
        # TODO: Make coffee
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
        print(f"Here is ${insert_total} in change.\nHere is your {menu}☕️. Enjoy!")
    else:
        print(f"Sorry that's not enough money. Money refunded.")

while not machine_turn_off:
    machine_menu = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: Print report of coffee machine resources
    if machine_menu == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
    elif machine_menu == "off":
        machine_turn_off = True
    else:
        drink = MENU[machine_menu]
        if is_resource_sufficient(drink["ingredients"]):
            process_coins(machine_menu, drink["cost"], drink["ingredients"])