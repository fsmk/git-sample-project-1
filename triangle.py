#
# triangle.py
#

# triangle.py accepts the lenghts of 3 sides and outputs the kind of triangle

a=input("Enter side 1 : ")
b=input("Enter side 2 : ")
c=input("Enter side 3 : ")

if ( a*a + b*b == c*c ) or ( b*b + c*c == a*a ) :
    print("Right Angled Triangle")

if a == b :
    print("Isosceles Triangle")

if a != b and b != c :
    print("Scalene Triangle")

