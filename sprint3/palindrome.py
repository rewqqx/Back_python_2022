from re import sub


def palindrome(input_string: str) -> bool:
    tmp_string = sub(r'[\W_]', '', input_string).lower()
    tmp_string_revers = tmp_string[::-1]
    if tmp_string == tmp_string_revers:
        return True
    return False


print(palindrome(input()))
