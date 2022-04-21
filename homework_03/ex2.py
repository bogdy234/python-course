# First bullet

def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n-1)


print(sum_recursive(5))

# Second bullet


def sum_recursive_even(n):
    if n == 0:
        return 0
    if not n % 2 == 0:
        return sum_recursive_even(n-1)
    else:
        return n + sum_recursive_even(n-1)


print(sum_recursive_even(5))

# Third bullet


def sum_recursive_odd(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return sum_recursive_odd(n-1)
    else:
        return n + sum_recursive_odd(n-1)


print(sum_recursive_odd(5))
