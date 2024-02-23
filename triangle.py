#
# triangle.py
#

# triangle.py accepts the lenghts of 3 sides and outputs the kind of triangle

a=float(input("Enter side 1 : "))
b=float(input("Enter side 2 : "))
c=float(input("Enter side 3 : "))

if ( a*a + b*b == c*c ) or ( b*b + c*c == a*a ) or ( c*c + a*a == b*b ):
    print("Right Angled Triangle")

if a == b or b == c or c == a:
    print("Isosceles Triangle")

if a == b and b == c:
    print("Equilateral Triangle")

if a != b and b != c :
    print("Scalene Triangle")

