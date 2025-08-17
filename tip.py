def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    decimal = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * decimal
    print(f"Leave ${tip:.2f}")

#Converting dollar strings to float
def dollars_to_float(d):
    dollars = d.strip('$')
    return float(dollars)

#Converting the percentage to an integer
def percent_to_float(p):
    percent = p.strip('%')
    perc_num = int(percent)

#Converting the integer to a decimal
    decimal = perc_num / 100
    return float(decimal)

main()