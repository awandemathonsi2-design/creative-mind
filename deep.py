#Type in the answer which will be changed to lowercase and removed of all outer whitespaces
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    lowercase_ans = answer.lower().strip()

#Condionals are now being applied
    if lowercase_ans == "42":
       print("Yes")
    elif lowercase_ans == "forty two":
       print("Yes")
    elif lowercase_ans == "forty-two":
        print("Yes")
    else:
        print("No")

main()