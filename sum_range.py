# a recursive function that sums the num and and sum_num of num - 1 until it reaches the base case


def sum_range(num):
    if num == 1:  # base case
        return 1  # if base case reached, return 1
    return num + sum_range(num - 1)


print(sum_range(5))
# call stack
#  first checks if 5 is one (false!)
# then returns 5 and waits for sum_range(4)
# checks if 4 is one (false!)
# then returns 4 and waits for sum_range(3)
# checks if 3 is one (false!)
# returns 3 and waits for sum_range(2)
# checks if 2 is one (false!)
# returns 2 and waits for sum_range(1)
# checks if 1 is 1 (true!), so the base case is reached!
# now, it goes back and removes from the call stack (all waiting is done!)
# sum_range(1) is 1 so...
# 2 + sum_range(1) is 3
# sum_range(2) is 3 so...
# 3 + sum_range(2) is 6
# sum_range(3) is 6 so...
# 4 + sum_range(3) is 10
# sum_range(4) is 10 so...
# 5 + sum_range(4) is 15
# therefore, sum_range(5) is 15!





