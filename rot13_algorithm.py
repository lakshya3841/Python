import string
alpha1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
alpha2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def encode(strEnc):
     return strEnc.translate(str.maketrans(alpha1, alpha2))
def decode(strEnc):
    return strEnc.translate(str.maketrans(alpha2, alpha1))

print("Choose One: ")
print()
print("Enter 1 to Encode")
print("Enter 2 to Decode\n")
inpWhich = int(input("Enter Your Choice: "))
if inpWhich == 1:
    inpSent = str(input("Enter the string to encode: "))
    print(encode(inpSent))
elif inpWhich == 2:
    inpSent = str(input("Enter the string to decode: "))
    print(decode(inpSent))
else:
    print("An unexpected error occured while making your request\n")