def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #If the length of the plates range from 2 to 6 characters then return else return false
    if len(s) >= 2 and len(s) <= 6:
        if s.isalpha():
            return True
        #Plates must start with atleast two letters else return false
        elif s.isalnum() and s[0:2].isalpha():
             #Digits must only be at the end
             for char in s:
                 if char.isdigit():
                    position = s.index(char)
                    #If the first digit is not 0 then return true else return false
                    if s[position:].isdigit() and int(char) != 0:
                        return True
                    else:
                        return False

        else:
            return False

    else:
        return False

if __name__ == "__main__":
    main()