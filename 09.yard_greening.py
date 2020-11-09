yard_square_meters = float(input())
square_meter_price = 7.61
discount = 0.18
price = yard_square_meters * square_meter_price
discount_price = round(price * discount, 2)
final_price = round(price - discount_price, 2)
print(f'The final price is {final_price} lv.')
print(f'The discount is {discount_price} lv.')
