length_in_centimeters = int(input())
width_in_centimeters = int(input())
height_in_centimeters = int(input())
already_full_percent_of_volume = float(input())
volume_fish_tank = length_in_centimeters * width_in_centimeters * height_in_centimeters
fish_tank_liters = volume_fish_tank * 0.001
percent = already_full_percent_of_volume * 0.01
liters_needed = fish_tank_liters * (1 - percent)
print(liters_needed)