# first example using recursion ( a func that counts from from num)
# Without recursion:


def count_down(num):
    while num > 0:  # if the num is 0
        print(num)  # display num
        num -= 1  # decrement and update num
    print("All done!")  # once at 0


# count_down(20)

# with recursion


def count_down2(num):
    if num <= 0:  # base case 0
        print("All done!")  # if base case is reached, print "All done!"
        return  # once base case is reached, stop.
    else:  # otherwise print num
        print(num)
        num -= 1
        count_down2(num)


count_down2(5)
# Steps:
# print 5
# count_down2(4)
# print(4)
# count_down(3)
# print(3)
# count_down2(2)
# print(2)
# count_down(1)
# print(1)
# count_down(0) (base case!)
# print("All done")




