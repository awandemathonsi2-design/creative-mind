#A dictionary where the key will be the item and value will be the count
grocery_list = {}

#While true loop to prompt the user for an item which will be changed to uppercase
while True:
    try:
        item = input().upper()
        #Checks if the item matches a key inside the dictionary
        if item in grocery_list:
            #Increases count if the item exist else it adds a new item with the count of 1
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    #If the input is not in the dictionary, it will prompt the user again for a valid key
    except KeyError:
        pass
    #Cntrl D: Prints a new line
    except EOFError:
        print()
        #Sorts the items in the dictionary alphabetically and prints the count and item
        for item in sorted(grocery_list):
            print(grocery_list[item], item)
        #Breaks out the loop when EOFError is raised
        break