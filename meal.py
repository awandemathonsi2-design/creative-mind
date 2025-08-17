#Enter the time and then call the convert function
def main():
   time_input = input("What time is it? ")
   time = convert(time_input)

#Depending on the time inputted between and including two time intervals will result in the specified meal time being printed else it returns none
   if time >= 7 and time <= 8:
    print("breakfast time")

   elif time >= 12 and time <= 13:
    print("lunch time")

   elif time >= 18 and time <= 19:
    print("dinner time")

   else:
     return None

'''
Convert the time to an integer then into a float number.
The time will be split into two substrings of hours and minutes then changed from strings to integers then to float numbers.
Later returning the hours and minutes which can be converted to hours if they exceed 60 minutes
'''
def convert(time):
    hours, minutes = time.split(':')
    hours = int(float(hours))
    minutes = int(float(minutes))
    return hours + (minutes / 60)

if __name__ == "__main__":
    main()
