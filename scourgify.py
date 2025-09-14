import sys, csv

def main():
    command_line_arg()
    students = []
    #Trys to open the file then create first name and last name which will be added to the students dictionary
    try:
        with open(sys.argv[1], "r") as before:
            reader = csv.DictReader(before)
            for row in reader:
                last, first = row["name"].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})

        #Writes a new csv file
        with open(sys.argv[2], "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

#Function checks how many arguments are in the command line
def command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #Checks that it is a csv file
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()