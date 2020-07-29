Where things go wrong!

1. No base case

   - your recursive function does not have a stopping point.

2. Forgetting to return or returning the wrong thing!

   - in order to remove from the call stack, you must return NOT print! (common mistake)

3. Stack overflow! (no NOT the website!)

   - in other words, your recursive function does not end! (exceeds call stack)

Either way, make sure your recursive function does not exceed the call stack. Have a base case!
