#Enter an expression which will be split into three strings assuming that the user puts whitespaces
def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")

#The numbers in place of x and z will be changed into float numbers, this way the answer automatically becomes a float
    number1 = float(x)
    number2 = float(z)

#Operator/sign that is inputted will determine the output of the expression
    operator = y
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    else:
        print(number1 / number2)

main()