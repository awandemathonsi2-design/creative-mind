#Enter greetings then it will be lowered and removed of all outer whitespaces
def main():
    greet = input("Greetings: ")
    lowercase_greeting = greet.lower().strip()

#Condionals are now being applied
    if "hello" in lowercase_greeting:
        print("$0")
    elif lowercase_greeting.startswith('h'):
        print("$20")
    else:
        print("$100")

main()