from resource import MENU,resources

power_on = True
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        for key,value in resources.items():
            print(f"{key.title()}: {value}")
    elif choice == "off":
        power_on = False
        break
    else:
        print("Please insert coins.")
        quarters = input("how many quarters?: ")
        dimes = input("how many dimes?: ")
        nickles = input("how many nickles?: ")
        pennies = input("how many pennies?: ")
        quarters = int(quarters) * 0.25
        dimes = int(dimes) * 0.10
        nickles = int(nickles) * 0.05
        pennies = int(pennies) * 0.01
        #print(quarters, dimes, nickles, pennies)
        total = quarters + dimes + nickles + pennies
        if total > MENU[choice]["cost"]:
            total -= MENU[choice]["cost"]
            print(f"Here is ${round(total, 2)} in change.")
        else:
            print("Sorry, you don't have enough money! Money refunded.")
            break
        drink_type = MENU[choice]["ingredients"]
        sufficient = True
        for key, required in drink_type.items():
            if required > resources.get(key, 0):
                print(f"Sorry, not enough {key}.")
                sufficient = False
                break
        if sufficient:
            for key, required in drink_type.items():
                resources[key] -= required
            print(f"Enjoy your {choice}!")
            # print(resources)