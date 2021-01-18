while True:
    try:
        try:
            x = int(input("Enter a number between 2-8 "))
            if x <= 8 and x > 2:
                break
            else:
                print("Try Again")
        except ValueError as err:
            print(err)
    except EOFError as err_2:
        print(err_2)


for i in range(x):
    for j in range(i+1):
        print("*",end="")
    print()

