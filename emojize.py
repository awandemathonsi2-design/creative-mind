#Import the emoji module
import emoji

#Type in a string
user_input = input("Input: ")
#emojize function takes a language parameter set to alias which will recognize and convert emoji code/s (user input) into emoji/s
out = emoji.emojize(user_input, language="alias")
print(f"Output: {out}")