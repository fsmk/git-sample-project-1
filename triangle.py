#
# triangle.py
#

# triangle.py accepts the lenghts of 3 sides and outputs the kind of triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
    print("Right Angled Triangle")

elif a == b or b == c or a == c:
    print("Isosceles Triangle")

elif a != b and b != c and a != c:
    print("Scalene Triangle")