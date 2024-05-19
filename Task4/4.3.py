def fast_exp(base, exp):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result


base = 2
exp = 10
fast_exp(base, exp)
