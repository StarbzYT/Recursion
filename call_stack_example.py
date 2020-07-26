from random import choice
# for function that calls othe funcs, python uses the callstack to manage the order of which functions should run
# think of the callstack like a stack of papers, you add to the top and remove from the top. (dev tools include a call stack)
# the latest function called is added to the top of the stack and then removed once python reaches the return keyword.

# example: waking up in the morning


def showering():
    print("I'm showering!")


def eat_breakfast():
    meal = cook_food()  # calls another function that is added to the top of the callstack once this func is reached
    print(f"Eating {meal}!")


def cook_food():
    items = ["eggs", "toast", "waffles", "bacon", "sausages"]
    return choice(items)


def wake_up():
    # calls all other funcs
    showering()
    eat_breakfast()
    print("Okay, ready for work!")


wake_up()


