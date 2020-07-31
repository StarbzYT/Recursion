# helper method recursion
# have a helper func in the original recursive func to keep track of changes or updates to variables


def get_odds(nums):  # nums list
    odds = []  # var to keep track of odds in nums
# we want to get all odds in nums but, we need a new var list to keep track of all nums
# we can not have a regular var in one recursive func since it will be reset each time the func is called!
    def helper(helper_input):
        if len(helper_input) == 0:  # base case (if length of list is 0)
            return
        elif helper_input[0] % 2 != 0:  # if first index is not even (odd)
            odds.append(helper_input[0])

        helper(helper_input[1::])
    
    helper(nums)  # get_odds calls helper on nums
    return odds  # get_odds returns all odd values in nums

# the helper (recursive) func is called again, slicing the first index (if odd added to odds) until nums has a length of 0


print(get_odds([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [1, 3, 5, 7, 9]

# What is helper method recursion? It is a pattern which has a parent func that is not recursive, which calls a helper func that IS recursive.