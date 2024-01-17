def decimal_to_base_n(decimal_number, base):
    if not 2 <= base <= 36:
        return "Base out of range (2-36)"
    
    if decimal_number == 0:
        return '0'

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    converted_number = ''

    while decimal_number > 0:
        remainder = decimal_number % base
        converted_number = digits[remainder] + converted_number
        decimal_number //= base

    return converted_number

decimal_number = 123  
desired_base = 8       

result = decimal_to_base_n(decimal_number, desired_base)
print(f"{decimal_number} soninig {desired_base} sanoq sistemasidagi natijasi {result}")