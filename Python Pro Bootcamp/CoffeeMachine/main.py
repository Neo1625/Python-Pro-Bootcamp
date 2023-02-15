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
}

def process_payment(quarters, dimes, nickles, pennies):
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

# Function that process coffee selection
def process_coffee(coffee, total_cash):
    change = total_cash - MENU[coffee]['cost']



    if change >= 0:

       if coffee == 'latte' or coffee == 'cappuccino':
           resources['milk'] = resources['milk'] - MENU[coffee]['ingredients']['milk']
       resources['water'] = resources['water'] - MENU[coffee]['ingredients']['water']
       resources['coffee'] = resources['coffee'] - MENU[coffee]['ingredients']['coffee']

       if resources['coffee'] < 0:
            print("Sorry not enough coffee")
       elif resources['water'] < 0:
            print("Sorry not enough water")
       elif resources['milk'] < 0:
            print("Sorry not enough milk")
       else:
            if change>0:
                print(f"Here is your ${change:.2f} dollars in change.")
            print(f"Here is your {coffee}. Enjoy!")

            global profit
            profit += MENU[coffee]['cost']


    else:
        print("Sorry that's not enough money. Money refunded.")




# Profit_amount
profit = 0

# Turn off the coffee machine by entering 'off' to the prompt.
ON = True
OFF = False
machine_status = ON

while machine_status:

    #Prompt users order.
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == 'off':
        machine_status = OFF

    # Print report.
    elif option == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit:.2f}")

    else:

        # Coin prompt
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        total_cash = process_payment(quarters, dimes, nickles, pennies)

        # Process coffee selection
        process_coffee(option, total_cash)
