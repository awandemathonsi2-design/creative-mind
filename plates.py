def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Checks that the length remains between six and two
def is_valid(plate):
    if not (2 <= len(plate) <=6):
        return False

#Checks that the first two characters are letters
    if not plate[0:2].isalpha():
       return False

#Checks that all characters in the string are alphanumeric
    if not plate.isalnum():
       return False

#Checks that the rest of the plate after the first number appears are entirely numbers
    for char in plate:
        if char.isdigit():
         if not plate[2:].isnumeric:
            return False

#Checks that the first number is not a 0
    for char in plate:
        if char.isdigit():
                if char == "0":
                    return False
                break
    return True

main()