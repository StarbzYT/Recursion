Recursion

What is recursion?
A process (function in our case) that calls itself.

Advantages of Recursion:

Recursive functions make the code look clean and elegant.
A complex task can be broken down into simpler sub-problems using recursion.
Sequence generation is easier with recursion than using some nested iteration.

Disadvantages of Recursion:
Sometimes the logic behind recursion is hard to follow through.
Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
Recursive functions are hard to debug.

What is the time complexity of recursive functions?

The time complexity, in Big O notation, for each function, is in numerical order: The first function is being called recursively n times before reaching base case so its O(n) (linear time).

It shows up a lot and many functions built into python are recursive, including algorithms!

Base Case:
The condition when the recursion ends. It does not run infinitely!

The two important conditions are the base case and the different inputs required to call the function over and over until the base case is reached.

Where things go wrong!

1. No base case

   - your recursive function does not have a stopping point.

2. Forgetting to return or returning the wrong thing!

   - in order to remove from the call stack, you must return NOT print! (common mistake)

3. Stack overflow! (no NOT the website!)

   - in other words, your recursive function does not end! (exceeds call stack)

Either way, make sure your recursive function does not exceed the call stack. Have a base case!

Helper Method Recursion

Most times, recursion problems are difficult to wrap your head around. In that case, it is easier to add a helper function. Of course, this is not mandatory, but it allows for more clarity especially with more diifcult problems. Include a pattern that has a parent function that is not recursive, but has a helper function inside that is.

Pure Recursion Tips

- For arrays/lists, use methods that make copies of arrays/lists so you do not mutate them.

- Remember that strings are immutable, so you will need to use methods to make copies of strings.

END
