import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

#The user would like the text to be in a random font
if len(sys.argv) == 1:
    f = choice(figlet.getFonts())
    figlet.setFont(font=f)

#The user would like the text to be in a specific font
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])

#Anything else will result in exiting with an error message
else:
    sys.exit("Invalid usage")

#User types in a text
text = input("Input: ")
#Output will be the font that the user randomly or specifically chose
print(f"Output: {figlet.renderText(text)}")