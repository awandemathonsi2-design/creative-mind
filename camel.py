#Enter camel case and print snake_case which will let the output end on the same line
def camel2snake():
    camel = input("camelCase: ")
    print("snake_case: ", end='')

#Loop through every letter and if it's an uppercase, put an underscore and make it a lowercase while not leaving any whitespaces in between
    for i in camel:
         if i.isupper():
            print('_' + i.lower(), end='')
         else:
            print(i, end='')

camel2snake()

#The output and command prompt are on the same line, tried using \n but it's raising errors