def coin_return(cents):
    quarters = 0
    dimes = 0
    nickles = 0
    if cents >= 25:
        quarters = cents // 25
        cents = cents % 25
    if cents >= 10:
        dimes = cents // 10
        cents = cents % 10
    if cents >= 5:
        nickles = cents // 5
        cents = cents % 5
    return "You need: {} quarters, {} dimes, {} nickles, {} pennies".format(quarters, dimes, nickles, cents)


# print(coin_return(99))
# print(coin_return(26))
# print(coin_return(77))
# print(coin_return(22))



""" Super Advanced

* Store how many of each coin is in the cash register, 
then allow the change algorithm to deal with when you don't have enough coins to optimally give change.

"""


def coin_return_inventory(cents):
    quarters_needed = 0
    dimes_needed = 0
    nickles_needed = 0
    inventory = {"quarters": 2,
                 "dimes": 2,
                 "nickles": 2,
                 "cents": 100}
    if cents >= 25:
        quarters_needed = cents // 25
        if quarters_needed <= inventory["quarters"]:
            inventory["quarters"] = inventory["quarters"] - quarters_needed
            cents = cents % 25
        elif quarters_needed > inventory["quarters"]:
            quarters_left = quarters_needed - inventory["quarters"]
            quarters_needed = inventory["quarters"]
            inventory["quarters"] = 0
            cents = cents % 25 + (quarters_left * 25)
    if cents >= 10:
        dimes_needed = cents // 10
        if dimes_needed <= inventory["dimes"]:
            inventory["dimes"] = inventory["dimes"] - dimes_needed
            cents = cents % 10
        elif dimes_needed > inventory["dimes"]:
            dimes_left = dimes_needed - inventory["dimes"]
            dimes_needed = inventory["dimes"]
            inventory["dimes"] = 0
            cents = cents % 10 + (dimes_left * 10)
    if cents >= 5:
        nickles_needed = cents // 5
        if nickles_needed <= inventory["nickles"]:
            inventory["nickles"] = inventory["nickles"] - nickles_needed
            cents = cents % 5
        elif nickles_needed > inventory["nickles"]:
            nickles_left = nickles_needed - inventory["nickles"]
            nickles_needed = inventory["nickles"]
            inventory["nickles"] = 0
            cents = cents % 5 + (nickles_left * 5)

    return "You need {} quarters, {} dimes, {} nickles, and {} pennies.".format(quarters_needed, dimes_needed,
                                                                                nickles_needed, cents)


def coin_return_inventory2(cents):
    inventory = {"quarters": {"worth": 25, "needed": 0, "drawer": 2},
                 "dimes": {"worth": 10, "needed": 0, "drawer": 2},
                 "nickles": {"worth": 5, "needed": 0, "drawer": 2}
                 }
    order = ["quarters", "dimes", "nickles"]
    for i in order:
        inventory[i]["needed"] = cents // inventory[i]["worth"]
        if inventory[i]["needed"] <= inventory[i]["drawer"]:
            inventory[i]["drawer"] = inventory[i]["drawer"] - inventory[i]["needed"]
            cents = cents % inventory[i]["worth"]
        elif inventory[i]["needed"] > inventory[i]["drawer"]:
            left = inventory[i]["needed"] - inventory[i]["drawer"]
            inventory[i]["needed"] = inventory[i]["drawer"]
            inventory[i]["drawer"] = 0
            cents = cents % inventory[i]["worth"] + (left * inventory[i]["worth"])
    return "You need {} quarters, {} dimes, {} nickles, and {} pennies.".format(inventory["quarters"]["needed"],
                                                                                inventory["dimes"]["needed"],
                                                                                inventory["nickles"]["needed"], cents)