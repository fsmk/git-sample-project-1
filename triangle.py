#
# triangle.py
#

# triangle.py accepts the lenghts of 3 sides and outputs the kind of triangle
import sys

a = float(input("Enter side 1 : "))
b = float(input("Enter side 2 : "))
c = float(input("Enter side 3 : "))

if ( a*a + b*b == c*c ) or ( b*b + c*c == a*a ) or ( c**2 + a**2 == b**2 ):
    print("Right Angled Triangle")
    sys.exit()
    
if a == b == c :
    print("Equilateral Triangle")
    sys.exit()
    
if a == b or b==c or a == c:
    print("Isosceles Triangle")
    
if a != b and b != c and a != c:
    print("Scalene Triangle")