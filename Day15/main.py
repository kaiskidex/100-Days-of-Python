# Coffee Machine Program

resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0
    }

MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "money": 1.5},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "money": 2.5},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "money": 3.0}
    }


def check_resources(order):
    recipe = MENU[order]
    for item in recipe:
        if item == "money":
            continue
        if recipe[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickles = int(input("Insert nickles: "))
    pennies = int(input("Insert pennies: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    return total

def transaction(pay, order_cost):
    if pay >= order_cost:
        change = round(pay - order_cost, 2)
        global resources 
        resources['money'] += order_cost

        if change > 0:
            print(f"Here is ${change:.2f} change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

def make_coffee(drink_choice):
    drink = MENU[drink_choice]

    resources['water'] -= drink['water']
    resources['milk'] -= drink['milk']
    resources['coffee'] -= drink['coffee']

    print(f"Here is your {drink_choice} ☕. Enjoy!")

#main loop
def coffee_machine():
    is_on = True

    while is_on:
        print(f"===MENU===\nEspresso: ${MENU['espresso']['money']}\nLatte: ${MENU['latte']['money']}\nCappuccino: ${MENU['cappuccino']['money']}")
        choice = input("What would you like? (espresso/latte/cappucino): ")

        if choice == 'off':
            print('Shutting down the coffee machine...☕🔌')
            is_on = False
        elif choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")

        elif choice in MENU:
            drink = MENU[choice]

            if check_resources(choice):
                payment = process_coins()
                if transaction(payment, drink['money']):
                    make_coffee(choice)
        else:
            print("Invalid selection. Please try again")

coffee_machine()
