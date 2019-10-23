def plusses(n, cap):
    if n == and n < cap:
        return 1
    elif n == 0 and cap <= 0:
        return 0
    else:
        return plusses(n // 10, cap - (n % 10)) + plusses(n//100, cap - (n % 100))
