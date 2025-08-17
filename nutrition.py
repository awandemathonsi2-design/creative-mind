#Create a dictionary with the key being the fruites and values being the calories
dict = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
    }

#Type in a fruit that will be removed of any spaces and brought down to a lowercase
def main():
    fruit = input("Item: ").lower().strip(' ')

#Checks that the fruit typed in is one of the keys in the dictionary and if present,it accesses the value of that key
    if fruit in dict:
        calories = dict.get(fruit)
        print(f"Calories: {calories}")

main()
