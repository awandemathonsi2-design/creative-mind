#Enter file name which will be changed to lowercase and stripped of whitespaces
#This will split the string from the right side of the string into a list of substrings at the period then take the last element of the list
def main():
    file_name = input("File name: ").lower().strip()
    file_ext = file_name.rsplit('.', 1)[-1]

#If the file extension is found in a case then the print will be executed
    match file_ext:
        case "gif" | "png" | "jpeg":
            print(f'image/{file_ext}')

        case "pdf" | "zip":
            print(f'application/{file_ext}')

        case "jpg":
            print("image/jpeg")

        case "txt":
            print("text/plain")

        case _:
            print("application/octet-stream")

main()