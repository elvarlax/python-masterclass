"""
Coding Exercise 10 - Break
Modify the code so that it stops printing when it reaches a number that's exactly divisible by 11.
That number should be the last value printed.

Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
"""
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break
