strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())
raspberries_price_per_kilo = strawberries_price / 2
oranges_price_per_kilo = raspberries_price_per_kilo - (raspberries_price_per_kilo * 0.4)
bananas_price_per_kilo = raspberries_price_per_kilo - (raspberries_price_per_kilo * 0.8)
sum_raspberries = raspberries_quantity * raspberries_price_per_kilo
sum_oranges = oranges_quantity * oranges_price_per_kilo
sum_bananas = bananas_quantity * bananas_price_per_kilo
sum_strawberries = strawberries_price * strawberries_quantity
total = sum_raspberries + sum_oranges + sum_bananas + sum_strawberries
print(total)