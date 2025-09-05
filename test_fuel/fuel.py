def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction )
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(percentage))

def convert(fraction):
        #Splits the fraction then converts it into integers
        x , y = fraction.split("/")
        x = int(x)
        y = int(y)

        #Checks if the denominator is equal to zero which raises a ZeroDivisionError
        if y == 0:
            raise ZeroDivisionError
        #Checks if the numerator is greater than the denominator or the numerator is less then zero which raises a ValueError
        elif x > y or x < 0:
            raise ValueError
        else:
            #The fraction is then multiplied by 100 then the percentage is returned
            percentage = round((x / y) * 100)
            return percentage

def gauge(percentage):
    #Checks if the percentage is less than 2 which would return "E"
    if percentage <= 1:
        return "E"
    #Checks if the percentage is more than 98 which would return "F"
    elif percentage >= 99:
        return"F"
    else:
        #Otherwise returns the percentage
        return f"{(percentage)}%"

if __name__ == "__main__":
    main()