import sys, csv
from tabulate import tabulate

def main():
    command_line_arg()
    #Table data will be stored in the variable
    data = []
    #Trys to open the file then prints it out as a table
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        print(tabulate(data[1:], headers=data[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")

#Function checks how many arguments are in the command line
def command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #Checks that it is a csv file
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()