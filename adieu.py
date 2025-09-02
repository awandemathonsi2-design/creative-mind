import inflect
p = inflect.engine()

#Create empty list where the input/s will be stored
names = []

#While true loop to prompt the user for a name
while True:
    try:
        person = input("Name: ").strip().title()
        #The name is added to the list
        names.append(person)
    #Cntrl D: Breaks out of the loop
    except EOFError:
        break

#On the next line it prints 'Adieu, adieu...' with the appropriate spacing, separator and conjunction
print()
print(f"Adieu, adieu, to {p.join(names)}")