import os

print("Basic Mathematics Calculations")
 
#Keep asking for numbers until valid input is entered.
while True:
   try:
     num_1=float(input("Enter the Number A:"))
     num_2=float(input("Enter the Number B:"))
     break
   except ValueError:
    print("Invalid input! , Please enter a valid number.")
  
#Choosing an operator
while True:
    operator = input("\nEnter the Operator (+, -, *, /): ")
    if operator in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operator! Please enter one of (+, -, *, /).")
 
#Perform Calculation
if operator=="+":
    result=f"\nSum:{num_1 + num_2 }"

elif operator =="-":
    result=f"\nDifference:{num_1 - num_2 }"

elif operator =="/":
  if num_2==0:
    result=f"\nDivision by zero is not allowed!"
  else:
    result=f"\nDivision:{num_1 / num_2 }"

elif operator =="*":
    result=f"\nProduct:{num_1 * num_2 }"

else:
    result="\nInvalid operator!"

# Get the directory where this script is located
folder_path = os.path.dirname(os.path.abspath(__file__))

# Create the file path inside the same folder
file_path = os.path.join(folder_path, "math.txt")
print("Saving file to:", file_path)

#Display and save result

print(result)
with open(file_path,"w") as file:
       content=file.write(result)
print("\nResult saved in file.")
