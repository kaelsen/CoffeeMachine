from resource import MENU,resources

profit = 0
power_on = True

def insert_coins(drink):
    while True:
        print("Please insert coins.")
        try:
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if total > MENU[drink]["cost"]:
                total -= MENU[drink]["cost"]
                print(f"Here is ${round(total, 2)} in change.")
                return True
            else:
                print("Sorry, you don't have enough money! Money refunded.")
                return False
        except ValueError:
            print("Sorry, type numbers only.")

def drink_select(drink):
    drink_type = MENU[drink]["ingredients"]
    sufficient = True
    for keys, required in drink_type.items():
        if required > resources.get(keys, 0):
            print(f"Sorry, not enough {keys}.")
            sufficient = False
            break
    can_afford = insert_coins(drink)
    if sufficient and can_afford:
        for keys, required in drink_type.items():
            resources[keys] -= required
        print(f"Enjoy your {drink}!")
        # print(resources)

while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for key,value in resources.items():
            print(f"{key.title()}: {value}")
    elif choice == "off":
        power_on = False
    else:
        drink_select(choice)
        profit += MENU[choice]["cost"]