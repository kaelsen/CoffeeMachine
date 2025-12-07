from resource import MENU,resources

# TODO: 1. print report of coffee machine resources

# TODO: 2. ask what the user would like (espresso/latte/cappuccino)
power_on = True
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for key,value in resources.items():
            print(f"{key.title()}: {value}")
    elif choice == "off":
        power_on = False
    else:
        drink_type = MENU[choice]["ingredients"]
        sufficient = True
        for key, required in drink_type.items():
            if required > resources.get(key,0):
                print(f"Sorry, not enough {key}.")
                sufficient = False
                break
        if sufficient:
            for key, required in drink_type.items():
                resources[key] -= required
            print(f"Enjoy your {choice}!")
            print(resources)
# TODO: 3. check if there's enough resources to create the users drink, if not exit and print not enough of x resource
# TODO: 4. insert coins if there's enough resources. quarter 0.25, dime 0.10, nickle 0.05, penny 0.01
# TODO: 5. check if enough coins were inserted to continue transaction
# TODO: 6. If enough coins subtract ingredients required from resources and output requested drink.