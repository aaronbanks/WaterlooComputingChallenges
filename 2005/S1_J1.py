def main():

    daytime_minutes = float(input("Number of daytime minutes?"))
    evening_minutes = float(input("Number of evening minutes?"))
    weekend_minutes = float(input("Number of weekend minutes"))

    plan_a_cost = 0

    if daytime_minutes > 100:
        plan_a_cost += (daytime_minutes - 100) * 25

    plan_a_cost += evening_minutes * 25
    plan_a_cost += weekend_minutes * 20

    plan_b_cost = 0

    if daytime_minutes > 250:
        plan_b_cost += (daytime_minutes - 250) * 45

    plan_b_cost += evening_minutes * 35
    plan_b_cost += weekend_minutes * 25


    if plan_a_cost < plan_b_cost:
        print(f"Plan A is cheapest at: ${plan_a_cost / 100}")

    if plan_b_cost < plan_a_cost:
        print(f"Plan B is cheapest at: ${plan_b_cost / 100}")

    if plan_a_cost == plan_b_cost:
        print(f"Both plans cost the same")


main()
