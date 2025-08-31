key=input("Digite uma senha base: ")

password=""
for letra in key:
    if letra in "Aa0":
        password = password + "9"
    elif letra in "Ee1":
        password = password +"3&"
    elif letra in "Ii2":
        password = password +":"
    elif letra in "Oo7":
        password = password +"2"
    elif letra in "Uu5":
        password = password +"e6"
    elif letra in "Ff3":
        password = password +"@"
    elif letra in "Ss6":
        password = password + "#"
    elif letra in "Mm8":
        password = password + "A@"
    elif letra in "Cc4":
        password = password + "&*"
    elif letra in "Dd":
        password = password + "H!"
    else: password = password + letra

print(password)