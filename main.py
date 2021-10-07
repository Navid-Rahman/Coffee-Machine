from coffee_machine_inventory import MENU
from coffee_machine_inventory import resources

continue_program = True
profit = 0


# TODO 2. Check if resources are sufficient
def is_enough_resources(customer_choice):
    for item in customer_choice:
        if resources[item] < customer_choice[item]:
            print(f"Sorry! there is not enough {item}")
            return False
    return True


# TODO 3. Process input coins
def process_coins():
    quarters = int(input("How many quarters?\n"
          "==>"))
    dimes = int(input("How many dimes?\n"
          "==>"))
    nickels = int(input("How many nickels?\n"
          "==>"))
    pennies = int(input("How many pennies?\n"
          "==>"))

    coins = round((0.25*quarters) + (0.10*dimes) + (0.05*nickels) + (0.01*pennies), 2)
    return coins


# TODO 4. Check if transactions are successful
def is_transaction_successful(customer_paid, drink_price):
    if customer_paid == drink_price:
        return True
    elif customer_paid > drink_price:
        global profit
        change = round(customer_paid - drink_price, 2)
        profit += (customer_paid-change)
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money.☹☹☹\n"
              "Money refunded.")


# TODO 5. Make Coffee
def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    return True


# TODO 1. Print Report
while continue_program:
    order = input("What would you like? (Cappuccino/Latte/Espresso)\n"
                  "==>").lower()
    if order == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}gm\n"
              f"Money: ${profit}")
    elif order == "off":
        continue_program = False
    else:
        drink = MENU[order]
        if is_enough_resources(drink["ingredients"]):
            customer_payment = process_coins()
            if is_transaction_successful(customer_payment, drink["cost"]):
                if make_coffee(drink["ingredients"]):
                    print(f"Here is your {order}!☕☕☕\n"
                          f"Enjoy\n")
