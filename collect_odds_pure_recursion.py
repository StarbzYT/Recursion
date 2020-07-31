# pure recursive way to get odds in a list
# no extra variables/ re-assignment needed

def get_odds(nums):
    odds = [] # this WILL be reset each time func is called again recursively
    if not nums:  # if nums is empty (careful of making a None object!)
        return []  # return [] otherwise it will return None!
    if nums[0] % 2 != 0:  # if first index is odd
        odds.append(nums[0])
    new_odds = odds + get_odds(nums[1:])  # adds odds num add calls get_odds on the rest of nums (not including that current num!)
    return new_odds
 

print(get_odds([1, 2, 3, 4, 5]))  # [1, 3, 5]

# Steps:
# if first index is odd...
# it adds that num to odds
# otherwise, the odds list remains empty for that iteration
# add the end (once base case is reached) it adds all the lists together containing odds or no nums
