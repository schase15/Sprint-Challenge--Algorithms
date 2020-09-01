#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime for this is O(n). This is because the number of times the loop needs to run is equal to the size of n. So as n increases, the amount of loops (and therefore the time) will increase equivalently.


b) The runtime for this is O(n log n). This is the result of having nested loops. For the outer loop (for i in range(n)) the runtime is O(n). This is because this loop will itereate through a range of length n. As n increases, the amount of loops it has to do increases linearly. The inner loop is O(log n). This is because it has an upper limit set at j. Each pass it makes through the inner loop it multiplies j by 2 and checks if j is still less than n. So as n increases, the numer of times the inner loop runs increases, but at a slower pace than n.

Outer loop * inner loop: O(n) * O(log n)
Runtime is O(n log n)


c) The runtime for this is O(n). This is a recursive call that is subtracting 1 from the original input on each pass and running until it hits 0. This means that it will loop as many times as the value that is passed in (n). As the value of bunnies increases, the runtime will increase linearly with it. 

## Exercise II

For this problem I would implement binary search. I would start by dropping an egg from the middle floor. If it breaks, we need to go lower. If it doesn't break, we need to go higher. After dropping the first egg you can throw out half of the building floors, and repeat the process on the appropriate half. Dropping from the middle of the remaining floors and narrowing in on the last floor that doesn't break the egg.


The runtime for this would be O(log n). The runtime increases as n increases, but does so at a reduced rate because we are cutting the search area in half on every pass. 



<!-- I wrote a hypothetical function that does an egg drop on an egg class -->
<!-- It is on the egg_drop.py page in this folder -->

