"""
Coding Exercise 18 - Factorial function
The factorial of a number is the product of all the values from 1 to the number, inclusive.
Thus 4 factorial, which is written as 4!, is calculated as
1 * 2 * 3 * 4 = 24

5! is
1 * 2 * 3 * 4 * 5 = 120
The convention is that 0! = 1 (not zero, as you might expect).

Write a function called factorial, that will return the factorial of the number passed as its argument.
You must include a Docstring, and function annotations, in your function.

Use a for loop to call your factorial function, to print out the first 36 factorials (0 to 35).
Your results should be:
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
11 39916800
12 479001600
13 6227020800
14 87178291200
15 1307674368000
16 20922789888000
17 355687428096000
18 6402373705728000
19 121645100408832000
20 2432902008176640000
21 51090942171709440000
22 1124000727777607680000
23 25852016738884976640000
24 620448401733239439360000
25 15511210043330985984000000
26 403291461126605635584000000
27 10888869450418352160768000000
28 304888344611713860501504000000
29 8841761993739701954543616000000
30 265252859812191058636308480000000
31 8222838654177922817725562880000000
32 263130836933693530167218012160000000
33 8683317618811886495518194401280000000
34 295232799039604140847618609643520000000
35 10333147966386144929666651337523200000000
"""


def factorial(n: int) -> int:
    """
    Return n! (0! is 1).

    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if n <= 1:
        return 1

    return n * factorial(n - 1)


for i in range(36):
    print(i, factorial(i))

