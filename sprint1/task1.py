def nearest_zero(array: list) -> str:
    dist_fin_1 = [float('inf')] * len_array
    dist_fin_2 = [float('inf')] * len_array
    flag_1 = 0
    flag_2 = 0
    final = ''
    len_array = len(array)
    for i in range(len_array):
        if array[i] == '0':
            dist_fin_1[i] = 0
            flag_1 = 1
        elif flag_1 == 1:
            dist_fin_1[i] = dist_fin_1[i-1] + 1

        if array[len_array - i - 1] == '0':
            dist_fin_2[len_array - i - 1] = 0
            flag_2 = 1
        elif flag_2 == 1:
            dist_fin_2[len_array - i - 1] = dist_fin_2[len_array - i] + 1

    for i in range(len_array):
        final += str(min(dist_fin_1[i], dist_fin_2[i])) + ' '   

    return final.strip()



n = input().split()
print(nearest_zero(len(n), n))