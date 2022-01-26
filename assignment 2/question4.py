"""4. Write a python program to find the greatest of three numbers entered by the
user."""
x=int(input("numb1"))
y=int(input("numb2"))
z=int(input("numb3"))
if x>y:
    if x>z:
        print(x,"is the greatest no")
    else:
        print(z,"is the greatest number")
else:
    if y>z:
        print(y,"is the greatest number")
    else:
        print(z,"is the greatest number")