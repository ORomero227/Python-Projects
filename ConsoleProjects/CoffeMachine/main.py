from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_menu = Menu()
coffee_maker = CoffeeMaker()
coins_machine = MoneyMachine()

is_coffee_maker_off = False
while not is_coffee_maker_off:
    user_choice = input(f"What would you like? ({coffee_maker_menu.get_items()}): ").lower()

    if user_choice == "off":
        is_coffee_maker_off = True
    elif user_choice == "report":
        coffee_maker.report()
        coins_machine.report()
    else:
        coffee = coffee_maker_menu.find_drink(user_choice)

        if coffee_maker.is_resource_sufficient(coffee) and coins_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
