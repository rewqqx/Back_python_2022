def sleight_of_hand(k: int) -> int:
    arr = [0] * 9
    result = 0
    for _ in range(4):
        for i in input():
            if i != '.':
                arr[int(i) - 1] += 1
                if arr[int(i) - 1] == 2 * k + 1:
                    result -= 1
                elif arr[int(i) - 1] == 1:
                    result += 1
    return result


k = int(input())

print(sleight_of_hand(k))