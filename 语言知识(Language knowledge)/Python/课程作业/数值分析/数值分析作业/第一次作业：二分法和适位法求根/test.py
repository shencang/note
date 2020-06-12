def function_composition(x):
    """函数表示和结果求值"""
    fc = -0.1 * pow(x, 4) - 0.15 * pow(x, 3) - 0.5 * pow(x, 2) - 0.25 * x + 1.2
    return fc


def async_function_composition(x):
    """函数表示和结果求值"""
    fc = -0.4 * pow(x, 3) - 0.45 * pow(x, 2) - pow(x, 1) - 0.25
    return fc


print(function_composition(0))
print(function_composition(1))
print(function_composition(0.5))

print(function_composition(0.25))
print(function_composition(0.75))
print(async_function_composition(0.5))
