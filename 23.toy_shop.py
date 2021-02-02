vacation_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
total = puzzles * 2.60 + talking_dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
amount_of_toys = puzzles + talking_dolls + bears + minions + trucks
if amount_of_toys >= 50:
    total = total - (total * 0.25)
profit = total - (total * 0.10)
if profit >= vacation_price:
    money_left = profit - vacation_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = vacation_price - profit
    print(f"Not enough money! {money_left:.2f} lv needed.")
