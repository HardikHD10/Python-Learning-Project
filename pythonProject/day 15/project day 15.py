MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
}

Total_money = 0

flag = True
while(flag):
    # input
    user_input_1 = input("What would you like? (espresso/latte/cappuccino): ").lower()

    #coffee machine
    if user_input_1 == "report":
        print(f"Resources left water : {resources['water']} ml, milk: {resources['milk']} ml, coffee: {resources['coffee']} ml.")
        print(f"TOTAL Money In the Machine ${Total_money}")
    else:
        if resources ["water"] < MENU[user_input_1]["ingredients"]["water"] or resources ["milk"] < MENU[user_input_1]["ingredients"]["milk"] or resources["coffee"] < MENU[user_input_1]["ingredients"]["coffee"] :
            print("Not Enough resources! Machine going to Halt. Please restart the machine.")
            user_input_6 = input("Do you want to Restart the machine.'y' or 'n'. ").lower()
            if user_input_6 == 'n' :
                print(f"Total Money = {Total_money}")
                flag = False
            elif user_input_6 == 'y':
                resources["water"] = 250
                resources["milk"] = 200
                resources["coffee"] =100

        else:
            user_input_2 = float(input("How many quarters?: "))
            user_input_3 = float(input("How many dimes?: "))
            user_input_4 = float(input("How many nickles?: "))
            user_input_5 = float(input("How many pennies?: "))

            # worth of money inserted calculation
            quarter_inserted = user_input_2 * 0.25
            dimes_inserted = user_input_3 * 0.10
            nickles_inserted = user_input_4 * 0.05
            pennies_inserted = user_input_5 * 0.01
            initial_sum = float("{:.2f}".format(quarter_inserted + dimes_inserted + nickles_inserted + pennies_inserted))

            money_required = MENU[user_input_1]["cost"]

            if initial_sum < money_required:
                print("Sorry that's not enough money. Money Refunded.")
            else:
                change = initial_sum - money_required
                print(f"Your coffee is bieng prepared! change of ${change} initiated.")
                Total_money += money_required
                resources["water"] = resources["water"] - MENU[user_input_1]["ingredients"]["water"]
                resources["milk"] = resources["milk"] - MENU[user_input_1]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU[user_input_1]["ingredients"]["coffee"]





