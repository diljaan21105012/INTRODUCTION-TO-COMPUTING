"""6. For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”)."""
x=int(input("length of first side\n"))
y=int(input("length of second side\n"))
z=int(input("length of third side\n"))
if x+y<=z or y+z<=x or x+z<=y:
    print("no")
else:
    print("yes")