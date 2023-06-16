from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
power_on = True
while power_on:
    answer = input(f"What would you like? {menu.get_items()}: ").lower()
    if answer == "off":
        power_on = False
    elif answer == "report":
        maker.report()
        money.report()
    else:
        drink = menu.find_drink(answer)
        if maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)
