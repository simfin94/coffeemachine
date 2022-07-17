from data import MENU
from data import resources

initial_water = resources['water']
initial_milk = resources['milk']
initial_coffee = resources['coffee']
initial_money = 0


def start(water, milk, coffee, money):
    # Ask the user which coffee they want.
    # Making the answer all lower case
    which_coffee = input("What would you like? (espresso, latte, cappuccino): ").lower()

    # If the user types 'report', the coffee machine will print out how much resources it has left
    if which_coffee == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${round(money, 2)}")

        # After the report i displayed, the coffee machine will ask the user to choose a coffee again
        start(water, milk, coffee, money)

    # If the user types 'off', the coffee machine turns itself off,
    # and when it's started again, it will have filled up it's resources
    elif which_coffee == "off":
        return
    else:
        # Passes user's input along with the resources left in the coffee machine
        machine(which_coffee, water, milk, coffee, money)


def machine(drink, water_left, milk_left, coffee_left, money):

    # Water required for the drink the user wanted
    water_req = MENU[drink]["ingredients"]["water"]

    if drink == "espresso":
        # If the user chooses 'espresso', set the milk to 0
        milk_req = 0
    else:
        milk_req = MENU[drink]["ingredients"]["milk"]
    coffee_req = MENU[drink]["ingredients"]["coffee"]

    #Checks if the coffee machine has enough water
    if water_left < water_req:
        print("Sorry, not enough water")
        return

    # Checks if the coffee machine has enough milk
    elif milk_left < milk_req:
        print("Sorry, not enough milk")
        return

    # Checks if the coffee machine has enough coffee
    elif coffee_left < coffee_req:
        print("Sorry, not enough coffee")
        return

    print("Please insert coins.")

    # Asks the user how many quarters, dimes, nickels, and pennies they are inserting
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))

    # Calculates how much money the user inserted
    quarter_sum = 0.25 * quarter
    dime_sum = 0.10 * dime
    nickel_sum = 0.05 * nickel
    penny_sum = 0.01 * penny
    money_inserted = quarter_sum + dime_sum + nickel_sum + penny_sum
    cost = MENU[drink]["cost"]

    # Rounds the total up with two decimals
    change = round((money_inserted - cost), 2)

    # Checks if the user inserted enough money
    if money_inserted >= cost:
        print(f"Here is ${change} in change\nEnjoy your coffee☕")
    else:
        print("Sorry, that's not enough money. Money refunded")

    # Recalculates the coffee machine's resources and how much money it now contains
    water_left -= water_req
    milk_left -= milk_req
    coffee_left -= coffee_req
    money_inserted -= change
    money += money_inserted

    # The coffee machine will now ask the user again for which coffee they want,
    # now with adjusted resources
    start(water_left, milk_left, coffee_left, money)

# Start
start(initial_water, initial_milk, initial_coffee, initial_money)
