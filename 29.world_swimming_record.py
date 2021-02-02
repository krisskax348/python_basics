import math

record_in_seconds = float(input())
distance = float(input())
seconds_per_m = float(input())
extra_seconds = math.floor(distance/15) * 12.5
total_seconds = distance * seconds_per_m + extra_seconds
if total_seconds < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_seconds:.2f} seconds.")
else:
    remaining_seconds = total_seconds - record_in_seconds
    print(f"No, he failed! He was {remaining_seconds:.2f} seconds slower.")


