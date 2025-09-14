import sys

def main():
    command_line_arg()
    #Trys to open the file and checks to see if each line starts with a # or whitespace
    try:
        with open(sys.argv[1], "r", newline='') as f:
            lines = f.readlines()

            counter = 0
            for line in lines:
               if check_line(line) == False:
                counter += 1
            print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")

#Function checks how many arguments are in the command line
def command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #Checks that it is a python file
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a Python file")

#Function checks to see if aline starts with a # or whitespace
def check_line(line):
    if line.lstrip().startswith('#'):
        return True
    elif line.isspace():
        return True
    return False

main()
