campaign_duration = int(input())
bakers = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
sum_cakes = cakes * 45
sum_waffles = waffles * 5.80
sum_pancakes = pancakes * 3.20
money_for_the_day = (sum_cakes + sum_waffles + sum_pancakes) * bakers
sum_money = money_for_the_day * campaign_duration
money_after_expenses = sum_money - (sum_money / 8)
print(money_after_expenses)