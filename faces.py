#Type in a sentence with emoticon in order to go through a conversion
def main():
    function = convert(input())
    print(function)

#This replaces the text/emoticon to an emoji
def convert(words):
    words = words.replace(':)', '🙂').replace(':(', '🙁')
    return words

main()