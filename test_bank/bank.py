def main():
    greeting = input("Greetings: ")
    dollar = value(greeting)
    print(f"${dollar}")

def value(greeting):
    #Greeting is converted to lowercase with no outer whitespaces
    greeting = greeting.lower().strip()
    #If the greeting starts with "hello" then 0 is returned
    if "hello" in greeting:
        return 0
    #If the greeting starts with "h" then 20 is returned
    elif greeting.startswith("h"):
        return 20
    #Otherwise return 100
    else:
         return 100

if __name__ == "__main__":
    main()