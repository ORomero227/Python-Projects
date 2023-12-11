# Author: Oscar A. Romero Barbosa
# Date: 12/08/2023
# This program simulates a virtual coffee machine
from data import resources
from data import MENU

money_in_machine = 0.0
water_in_machine = resources["water"]
milk_in_machine = resources["milk"]
coffe_in_machine = resources["coffee"]


def save_money_in_machine(money):
    global money_in_machine
    money_in_machine += money


def deduction_resources(water, milk, coffe):
    """Reduces machine resources"""
    global water_in_machine
    global milk_in_machine
    global coffe_in_machine

    water_in_machine -= water
    milk_in_machine -= milk
    coffe_in_machine -= coffe


def print_report():
    """Returns the amount of resources available on the machine"""
    print(f"Water: {water_in_machine}ml")
    print(f"Milk: {milk_in_machine}ml")
    print(f"Coffee: {coffe_in_machine}g")
    print(f"Money: ${format(money_in_machine,'.2f')}")


def check_resources(coffe_name):
    """Returns true if there are enough resources to brew the coffee; otherwise returns false"""
    coffe_recipe = MENU[coffe_name]["ingredients"]

    if "water" in coffe_recipe:
        if water_in_machine < coffe_recipe["water"]:
            print("Sorry there is not enough water.")
            return False

    if "milk" in coffe_recipe:
        if milk_in_machine < coffe_recipe["milk"]:
            print("Sorry there is not enough milk.")
            return False

    if "coffee" in coffe_recipe:
        if coffe_in_machine < coffe_recipe["coffee"]:
            print("Sorry there is not enough coffee.")
            return False

    return True


def process_coins():
    """Process the coins"""
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    total_inserted = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    return total_inserted


def check_transaction(coffe_cost, coins_qty):
    """Check the transaction"""
    if coins_qty == 0:
        print("Sorry that's not enough money.")
        return False
    elif coins_qty < coffe_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif coins_qty > coffe_cost:
        save_money_in_machine(coffe_cost)
        change = coins_qty - coffe_cost
        print(f"Here is ${format(change,'.2f')} dollars in change.")
        return True


def make_coffee(coffee_name):
    coffee_recipe = MENU[coffee_name]["ingredients"]
    water_needed = 0
    milk_needed = 0
    coffee_needed = 0

    if "water" in coffee_recipe:
        water_needed = coffee_recipe["water"]

    if "milk" in coffee_recipe:
        milk_needed = coffee_recipe["milk"]

    if "coffee" in coffee_recipe:
        coffee_needed = coffee_recipe["coffee"]

    deduction_resources(water_needed, milk_needed, coffee_needed)

    print(f"Here is your ☕{coffee_name}. Enjoy it!")


def start_machine(coffe_name):
    if check_resources(coffe_name):
        coins_inserted = process_coins()
        cost = MENU[coffe_name]["cost"]
        if check_transaction(cost, coins_inserted):
            make_coffee(coffe_name)


is_machine_off = False
while not is_machine_off:
    coffee = input("What would you like? (expresso / latte / cappuccino): ").lower()

    if coffee == "report":
        print_report()
    elif coffee == "off":
        is_machine_off = True

    if coffee == "expresso" or coffee == "latte" or coffee == "cappuccino":
        start_machine(coffee)
