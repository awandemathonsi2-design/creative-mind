#While true loop to prompt the user incase they enter an invalid input
while True:
    try:
        #The fraction will be split into numerator and denominator then converted into numbers
        fuel = input("Fraction: ")
        x, y = fuel.split('/')
        x = int(x)
        y = int(y)
        #If the numerator is greater than the denominator it will prompt the user again
        if x > y:
            continue
        #If the numerator is less than zero it will prompt the user again
        if x < 0:
            continue
        #Finds and rounds off the percentage to the nearest integer
        percent = round((x / y) * 100)
        
        #Depending on the percentage will  determine the output which then breaks out of the loop
        if percent <= 1:
             print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{int(percent)}%")
        break

    #If something is invalid, it will prompt the user again for a valid fraction
    except (ValueError, ZeroDivisionError):
        pass