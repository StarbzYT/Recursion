# factorial example using recursive approach


def factorial(num):
    if num == 1:  # base case
        return 1
    return num * factorial(num - 1)


print(factorial(5))  # 120 = 5 * 4 * 3 * 2 * 1 (this time we multiply by one!)




