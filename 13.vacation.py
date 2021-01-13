pages_in_book = int(input())
pages_per_hour = int(input())
days_needed = int(input())
total_reading_time = pages_in_book / pages_per_hour
needed_hours = total_reading_time / days_needed
print(needed_hours)