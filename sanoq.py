def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return '0'

    binary = ''
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number //= 2

    return binary

decimal_number = 123  

binary_number = decimal_to_binary(decimal_number)

print(f"10 lik sanoq sistemasidagi  {decimal_number} son 2 lik sanoq sistemasida  {binary_number} ga teng")