"""
Section 6 Challenge - banner_text Docstring
We don't have a Docstring for this function, so your challenge is to add one.
You should document the exception that can be raised.
Search on-line for something like python exception in docstring to see how to do that.
Hint: the return value shouldn't be documented - this function doesn't return anything useful.
Add your Docstring, and compare it against our suggestion.
"""


def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Print a string centred, with ** on both sides.

    :param text: The string to print.
                 An asterisk (*) will bring about a row of asterisks.
                 By default, blank lines are printed with ** margins on the left and right margins.
    :param screen_width: The overall width to print within (including the four spaces for the ** on both sides).
    :raises ValueError: If the provided string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError(f"String {text} is larger than specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = f"**{centred_text}**"
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text()
banner_text("When you're felling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
