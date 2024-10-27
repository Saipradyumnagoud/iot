shape=input("Shape : ")
if(shape=="rectangle"):
    length=float(input("Enter length : "))
    width=float(input("Enter width : "))
    area=length*width
    perimeter=2*(length+width)
    print("Area of rectangle : ",area)
    print("Perimeter of rectangle : ",perimeter)
elif(shape=="triangle"):
    base=float(input("Enter base : "))
    height=float(input("Enter height : "))
    area=0.5*base*height
    perimeter=base+base+height
    print("Area of triangle : ",area)
    print("Perimeter of triangle : ",perimeter)
elif(shape=="circle"):
    radius=float(input("Enter radius : "))
    area=3.14*radius*radius
    circumference=2*3.14*radius
    print("Area of circle : ",area)
    print("Circumference of circle : ",circumference)
else:
    print("Invalid shape!")
