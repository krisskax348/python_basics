budget = float(input())
number_of_extras = int(input())
price_per_outfit = float(input())
decor_budget = budget * 0.1
outfit_budget = number_of_extras * price_per_outfit
if number_of_extras > 150:
    outfit_budget = outfit_budget * 0.9
total_cost = decor_budget + outfit_budget
if total_cost > budget:
    remaining = total_cost - budget
    print("Not enough money!")
    print(f"Wingard needs {remaining:.2f} leva more.")
else:
    remaining = budget - total_cost
    print("Action!")
    print(f"Wingard starts filming with {remaining:.2f} leva left.")