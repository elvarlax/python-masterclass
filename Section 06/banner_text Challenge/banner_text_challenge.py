"""
Section 6 Challenge - banner_text
Modify the banner_text function so that it takes another argument, the width for the banner.
You'll need to provide that argument in all the lines that call the function.
"""


def banner_text(text, screen_width=80):
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
banner_text(" ")
banner_text("When you're felling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")
