import random

#Calls the get_level function and starts the score at 0
def main():
     level = get_level()
     score = 0

     #Creates a sum ten times for the user to answer with the number of tries being 0 for each
     for _ in range(10):
          x = generate_integer(level)
          y = generate_integer(level)
          result = x + y
          tries = 0
          #While the number of tries is below 3, it will prompt the user for the answer and if correct will increase the score by 1
          while tries < 3:
               try:
                   ans = int(input(f"{x} + {y} = "))
                   if ans == result:
                     score += 1
                     break
                   #If the answer is incorrect or is not an integer, it will print EEE and increase the tries by 1
                   else:
                       print("EEE")
                       tries += 1
               except ValueError:
                   print("EEE")
                   tries += 1

               #Prints the sum and answer if the number of tries has reached 3 and the score remains the same
               if tries == 3:
                    print(f"{x} + {y} = {result}")

     #Once all ten sums have been answered, the score will be printed
     print("Score: ", score)

#The get_level function with a while True loop to prompt the user for a level from 1 to 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            continue
        else:
            continue
    return level

#The generate_integer function returns a randomly generated positive integer with level digits
def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)

if __name__ == "__main__":
    main()