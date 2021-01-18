#This Program was made just for some basic understanding
phone_numbers = {"David": 6260}
print(phone_numbers["Lak"])
USER_INPUT = str(input("DO YOU WANT TO ADD A USER "))
if USER_INPUT == "Yes":
    x = str(input("enter the name "))
    y = int(input("enter the phone number"))
    phone_numbers[x] = y
else:
    print("ERRORS PLEASE FIX ME ")
l1 = ["David"]
l1.append(x)
noo = input("DO you want to extract a existing contact")
if noo == "Yes":
    print(l1)
    print("Whose number you want")
    yes = str(input(" "))
    print(phone_numbers[yes])
else:
    print("fix me")
