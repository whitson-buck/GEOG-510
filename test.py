def forwardorback(lists):
    userinput = input("Forward or reverse? [f]/r: ")
    if userinput != "f" or "r":
        print("Unexpected character. Try again.")
    elif userinput == "f":
        for i in range(len(lists)):
            print(lists[i])
    else:
        for i in range(len(lists)):
            print(lists[::-i])


forwardorback([3,5,6,3])