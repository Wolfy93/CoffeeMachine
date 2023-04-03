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

money = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}


def calc_total_money(mon):
    return (mon["pennies"] * 0.01) + (mon["nickels"] * 0.05) + (mon["dimes"] * 0.10) + (mon["quarters"] * 0.25)


def print_report(res, mon):
    print("Water: ", res["water"])
    print("Milk: ", res["milk"])
    print("Coffee: ", res["coffee"])
    print("Money: ", calc_total_money(mon))


def process_input(inp_string, menu):
    req = dict()
    if inp_string.lower() == "espresso":
        req["drink"] = "espresso"
        req["water"] = menu["espresso"]["ingredients"].get("water", 0)
        req["milk"] = menu["espresso"]["ingredients"].get("milk", 0)
        req["coffee"] = menu["espresso"]["ingredients"].get("coffee", 0)
        req["money"] = menu["espresso"].get("cost", 0)
    elif inp_string.lower() == "latte":
        req["drink"] = "latte"
        req["water"] = menu["latte"]["ingredients"].get("water", 0)
        req["milk"] = menu["latte"]["ingredients"].get("milk", 0)
        req["coffee"] = menu["latte"]["ingredients"].get("coffee", 0)
        req["money"] = menu["latte"].get("cost", 0)
    elif inp_string.lower() == "cappuccino":
        req["drink"] = "cappuccino"
        req["water"] = menu["cappuccino"]["ingredients"].get("water", 0)
        req["milk"] = menu["cappuccino"]["ingredients"].get("milk", 0)
        req["coffee"] = menu["cappuccino"]["ingredients"].get("coffee", 0)
        req["money"] = menu["cappuccino"].get("cost", 0)
    return req


def check_resources(req, res):
    if req["water"] <= res["water"] and req["water"] <= res["water"] and req["water"] <= res["water"]:
        return True
    else:
        # Todo: Optimise print if more than one resources are depleted
        if req["water"] > res["water"]:
            print("Sorry there is not enough water")
        elif req["milk"] > res["milk"]:
            print("Sorry there is not enough milk")
        elif req["coffee"] > res["coffee"]:
            print("Sorry there is not enough coffee")
        return False


# Todo: 4. Check Transaction

def check_transaction(req, inp, mon):
    global money
    money = mon
    change = inp["money"] - req["money"]
    tot_money = dict()
    # adding coins input to money
    tot_money["quarters"] = mon["quarters"] + inp["quarters"]
    tot_money["dimes"] = mon["dimes"] + inp["dimes"]
    tot_money["nickels"] = mon["nickels"] + inp["nickels"]
    tot_money["pennies"] = mon["pennies"] + inp["pennies"]

    # dispensing change
    int_change = change
    quarters_to_dispense = int_change // 0.25
    if tot_money["quarters"] > quarters_to_dispense:
        tot_money["quarters"] -= quarters_to_dispense
        int_change = int_change - quarters_to_dispense * 0.25
    else:
        int_change = int_change - (tot_money["quarters"] * 0.25)
        tot_money["quarters"] = 0
    dimes_to_dispense = int_change // 0.10
    if tot_money["dimes"] > dimes_to_dispense:
        tot_money["dimes"] -= dimes_to_dispense
        int_change = int_change - dimes_to_dispense * 0.10
    else:
        int_change = int_change - (tot_money["dimes"] * 0.10)
        tot_money["dimes"] = 0
    nickels_to_dispense = int_change // 0.05
    if tot_money["nickels"] > nickels_to_dispense:
        tot_money["nickels"] -= nickels_to_dispense
        int_change = int_change - nickels_to_dispense * 0.05
    else:
        int_change = int_change - (tot_money["nickels"] * 0.05)
        tot_money["nickels"] = 0
    pennies_to_dispense = int_change // 0.01
    if tot_money["pennies"] > pennies_to_dispense:
        tot_money["pennies"] -= pennies_to_dispense

        money["quarters"] = tot_money["quarters"]
        money["nickels"] = tot_money["nickels"]
        money["dimes"] = tot_money["dimes"]
        money["pennies"] = tot_money["pennies"]
        print(f"Here is ${round(change,2)} dollars in change.")
        return True
    else:
        int_change = int_change - (tot_money["pennies"] * 0.01)
        tot_money["nickels"] = -100 * int_change
        print("Sorry not enough coins to provide change.")
        return False


def make_coffee(res, req):
    res["water"] -= req["water"]
    res["milk"] -= req["milk"]
    res["coffee"] -= req["coffee"]
    print(f'Here is your {req["drink"]}. Enjoy!')
    return res


def main():
    while(1):
        global resources
        global money
        global MENU
        inp_string = input("What would you like? (espresso/latte/cappuccino):")
        if inp_string.lower() == "off":
            exit(0)
        elif inp_string.lower() == "report":
            print_report(resources, money)
        else:
            req = process_input(inp_string, MENU)
            if check_resources(req, resources):
                print("Please insert coins.")
                inp = dict()
                inp["quarters"] = int(input("How many quarters?: "))
                inp["dimes"] = int(input("How many dimes?: "))
                inp["pennies"] = int(input("How many pennies?: "))
                inp["nickels"] = int(input("How many nickels?: "))
                inp["money"] = (inp["quarters"] * 0.25)+(inp["dimes"] * 0.10)+(inp["nickels"] * 0.05)+(inp["pennies"] * 0.01)

                if req["money"] <= (inp["money"]):
                    if check_transaction(req, inp, money):
                        resources = make_coffee(resources, req)
                else:
                    print("Sorry that's not enough money. Money refunded.")

main()


