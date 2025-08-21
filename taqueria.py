#A dictionary with the keys being a food item and values being the price
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

#Confirm the total amount
total = 0

#While true loop to prompt the user incase they enter an invalid input
while True:
     try:
        item = input("Item: ").title()
        #Checks if the input is in the dictionary and retrieves the value of that key
        if item in menu:
            price = menu.get(item)
            #Adds the price to the total amount then prints the current total amount
            total += price
            print(f"Total: ${total:.2f}")

    #If the input is not in the dictionary, it will prompt the user again for a valid key
     except KeyError:
         pass
     #Cntrl D: Prints a new line and breaks out of the loop when EOFError is raised
     except EOFError:
        print()
        break