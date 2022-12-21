def psp_next(last_str: str) -> str:
    count_close = 0
    count_open = 0
    for i in range(len(last_str) - 1, -1, -1):
        if last_str[i] == '(':
            count_open += 1
            if count_close > count_open:
                break
        else:
            count_close += 1
    next_str = last_str[:len(last_str) - count_open - count_close]
    if next_str == "":
        return "End solution"
    else:
        next_str += ')'
        for j in range(count_open):
            next_str += '('
        for j in range(count_close - 1):
            next_str += ')'
        return next_str


def psp(n: int) -> str:
    psp_str = ""
    tmp_str = ""
    for j in range(n):
        tmp_str += '('
    for j in range(n):
        tmp_str += ')'
    psp_str += tmp_str
    while psp_next(tmp_str) != "End solution":
        tmp_str = psp_next(tmp_str)
        psp_str += "\n" + tmp_str
    return psp_str


print(psp(int(input())))
