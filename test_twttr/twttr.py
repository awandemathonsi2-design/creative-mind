#User inputs their tweet which then is removed of all vowels and the result is printed
def main():
    text = input("Input: ")
    tweet = shorten(text)
    print("Output: ", tweet)

#Iterates through each letter in the text to check if the letter matches with a vowel in the list and replaces the vowel without leaving any whitespaces
def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for vowel in word:
        if vowel in vowels:
            word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()