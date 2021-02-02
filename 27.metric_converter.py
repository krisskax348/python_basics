number = float(input())
convert_from = input()
convert_to = input()
conversion = f"{convert_from}:{convert_to}"
if conversion == "m:mm":
    converted_number = number * 1000
    print(f"{converted_number:.3f}")
elif conversion == "mm:m":
    converted_number = number / 1000
    print(f"{converted_number:.3f}")
elif conversion == "m:cm":
    converted_number = number * 100
    print(f"{converted_number:.3f}")
elif conversion == "cm:m":
    converted_number = number / 100
    print(f"{converted_number:.3f}")
elif conversion == "mm:cm":
    converted_number = number / 10
    print(f"{converted_number:.3f}")
elif conversion == "cm:mm":
    converted_number = number * 10
    print(f"{converted_number:.3f}")