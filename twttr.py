#A list of uppercase and lowercase vowels
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

#Type in a text
tweet = input("Input: ")

#Iterate through each letter in the text and replace the vowel without leaving any whitespaces
for vowel in tweet:
    if vowel in vowels:
        tweet = tweet.replace(vowel, '')

#Print the output
print("Output: ", tweet)
