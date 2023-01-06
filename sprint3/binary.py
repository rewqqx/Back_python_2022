def binary(number: int) -> str:
    binary_number = ''
    if number == 0:
        return '0'
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number


print(binary(int(input())))
