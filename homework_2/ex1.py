# First bullet

def calculate_sum(*args, **kwargs):
    sum = 0
    all_args = list(args) + list(kwargs.values())
    print(all_args)
    for arg in all_args:
        if type(arg) is int:
            sum += arg
    return sum


print(calculate_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(calculate_sum())
print(calculate_sum(2, 4, 'abc', param_1=2))
