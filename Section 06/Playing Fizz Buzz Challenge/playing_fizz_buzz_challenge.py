"""
Section 6 Challenge - Playing Fizz Buzz
For this challenge, you'll use the function that you wrote in the last exercise.

You'll do this in your IDE, because the on-line Python interpreter can't accept input from the keyboard.

The Python interpreter for Udemy's code exercises is running on a remote server.
That means your not sitting at it's keyboard, and have no way to type in your input.

For this challenge, replace that loop (the one I showed) with a loop that will play the game.
The computer will start with the value 1.
The player and the computer will then take turns.
The player will type in their response, and the computer will print out its next value.
And so on.
The game ends when the player makes a mistake, or gets to 100.
If the player gets it wrong, they lose.

This challenge doesn't involve writing another function - you're using a function that you've
already written, in the previous exercise.

My solution will be in the next video. In the remainder of this video, I'll plan the program,
so that we know what we're trying to do.

You may want to have a go at that yourself.
Write the steps in whichever language you think in. In my case, that's English - or Australian.
When plannig a program, write in your native language.
That way, you'll produce clear steps describing what the program is going to do.

If you dive straight in and start writing code, you'll find it very difficult.
Write the steps in the language that you think in.

A good rule is, reach for a pen and paper before you reach for your keyboard.
"""


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
             'buzz' if it's divisible by 5.
             'fizz buzz' if it's divisible by both 3 and 5.
             The number, as a string, otherwise.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz.   Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))
