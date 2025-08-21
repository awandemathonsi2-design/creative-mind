#A list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#While true loop to prompt the user incase they enter an invalid input
while True:
    #User inputs a date in middle-endian order and removes all outer whitespaces
    date = input("Date: ").strip()
        #Checks for this date format "--/--/----" which will be split into strings where the user puts backsplash
    if "/" in date:
        month, day, year = date.split('/')

        #Checks for a comma and splits into strings where there is a whitespace
    elif ',' in date:
        month, day, year = date.split()
        #if the month is found in the list, the position will be returned with an addition of 1 since the list starts at 0
        if month in months:
            month = months.index(month)
            month += 1
            #The comma is removed from the day string
            day = day.strip(',')
        #Any other kind of input will result in prompting the user again
    else:
        continue
        #Checks that day does not exceed 31 and month does not exceed 12 otherwise it reprompts the user
    try:
        if int(day) > 31 or int(month) > 12:
            continue
        #If all is valid, it prints the ISO date format with leading zeros and breaks out of the loop
        else:
            month = int(month)
            day = int(day)

            print(f"{year}-{month:02}-{day:02}")
            break

        #If user inputs an invalid value it reprompts the user
    except ValueError:
        continue