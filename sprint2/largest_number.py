def largest_number(n: int, numbers: str) -> str:
    numbers_arr = numbers.split(' ')
    for i in range(n - 1):
        for j in range(n - i - 1):
            tmp_var1 = numbers_arr[j] + numbers_arr[j + 1]
            tmp_var2 = numbers_arr[j + 1] + numbers_arr[j]
            if tmp_var1 < tmp_var2:
                numbers_arr[j], numbers_arr[j + 1] = numbers_arr[j + 1], numbers_arr[j]
    return "".join(numbers_arr)


print(largest_number(int(input()), input()))
