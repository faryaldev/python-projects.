print(" === Circle Geometry Calculator (CLI) === ")

while True:
 print("\nA Program to find the Area/Circumference/Radius/Diameter of Circle")
 print(" ")
 print("What do you want to find?")
 print("Press 1 for Area \nPress 2 for Circumference \nPress 3 for Radius \nPress 4 for Diameter")
 print("Press 5 to exit.\n" "")

 choice=int(input("Enter the Number to find your desired Calculation:"))

 PI=3.14
 
 if choice== 1:
    rad=float(input("Enter the Radius of Circle:"))
    print(f"Area is: {PI*rad**2}")

 elif choice== 2:
    rad=float(input("Enter the Radius of Circle:"))
    print(f"Circumference is: {2*PI*rad}")

 elif choice== 3:
         diameter=float(input("Enter the Diameter of Circle:"))
         print(f"Radius is: {diameter/2}")

 elif choice== 4:
         rad=float(input("Enter the Radius of Circle:"))
         print(f"Diameter is: {2*rad}")

 elif choice== 5:
         print("Exiting Program!")
         break
 
 else:
    print("Invalid Choice Entered!Try entering (1,2,3,4 or 5)")
