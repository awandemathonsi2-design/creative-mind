import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    command_line_arg()
    #Trys to open the image
    try:
        img_file = Image.open(sys.argv[1])
        #Opens shirt then gets the size of the shirt
        shirt_file = Image.open("shirt.png")
        size = shirt_file.size
        #Resizes muppet image to fit shirt then pastes shirt in muppet
        muppet = ImageOps.fit(img_file, size)
        muppet.paste(shirt_file, shirt_file)
        #Creates output image
        muppet.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

#Function checks how many arguments are in the command line
def command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    first_file = splitext(sys.argv[1])
    second_file = splitext(sys.argv[2])
    #Checks if it is a Image file
    if extensions(first_file[1]) == False:
        sys.exit("Invalid intput")
    elif extensions(second_file[1]) == False:
        sys.exit("Invalid output")
    #Checks if the extentions of both the files are the same
    elif first_file[1] != second_file[1]:
        sys.exit("Input and output have different extensions")

#Function that checks if the end of the input's and output's names end with specific extentions
def extensions(file):
    if file.lower() in {".jpg", ".jpeg", ".png"}:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
