# classic factorial example with iterative approach (can be done with recursion!)
# without recursion
# multiplies all the numbers from num down to one


def factorial(num):
    total = 1
    while num > 1:  # since total starts of as 1, there is no need to set num to 1
        total *= num
        num -= 1
    return total


print(factorial(4))  # 24 = 4 * 3 * 2 (remember that the while loop stops when num is 1)

