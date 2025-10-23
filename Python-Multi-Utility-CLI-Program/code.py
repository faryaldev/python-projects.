print("\n==== MULTI-UTILITY CLI PROGRAM ====")

def num_check(n):
  if n%2==0:
        return "Even!"
  else:
        return "Odd!"

def table(n):
    return(f"{n} * {i} = {n*i}"for i in range (1,11))

def max_min(n):
   if not n:
     raise ValueError("List is Empty!")
   return max(n), min(n)

def vowels(word):
   word.lower()
   print(f"The given word is:{word}")
   count=0
   for char in word:
     if char in"aeiou":
       count+=1
   print(f"The number of vowels are:{count}")

def is_palindrome(word):
    return word == word[::-1]
    

def sum_avg(n):
   total=sum(n)
   average=total/len(n)
   return(total,average)

def get_number_list():
    """Helper function to input a list of numbers from the user"""
    while True:
        nums = input("Enter numbers separated by spaces: ").strip()
        if not nums:
            print("Please enter at least one number.")
            continue
        try:
            return [int(x) for x in nums.split()]
        except ValueError:
            print("Invalid input. Make sure you enter integers separated by spaces.")

def greeting(n,a):
  return [f"\nHello {n.title()} , You're {a} years old!"]

while True:
 print ("\nWhich Function do you want to execute?")
 print("1. Check Even/Odd\n2. Multiplication Table\n3. Maximum and Minimum\n4. Sum and average\n5. No of Vowels\n6. Palindrome\n7. Greeting\n8. Exit the Program")
 choice=int(input("\nEnter your choice:"))

 if choice ==1:
  num=int(input("Enter a number:"))
  result=num_check(num)
  print(f"\nThe number {num} is {result}")

 elif choice ==2:
  num=int(input("Enter a number:"))
  print(f"\nMultiplication Table of {num} is:")
  for line in table(num):
   print (line)

 elif choice ==3:
  print("To check Max & Min")
  nums=get_number_list()
  max_val,min_val=max_min(nums)
  print(f"Maximum: {max_val}\nMinimum:{min_val}")

 elif choice ==4:
  nums= get_number_list()
  total,avg=sum_avg(nums)
  print(f"The sum is {total} and average of list is: {avg}")

 elif choice==5:
  print("To count number of vowels")
  my_word=input("Enter a word:")
  vowels(my_word)

 elif choice==6:
  my_word=input("Enter a word:")
  if is_palindrome(my_word) :
      print("The given word is palindrome!")
  else:
      print("The entered word is not a palindrome!")

 elif choice==7:
   name=input("\nEnter your name:")
   age=input("Enter your age:")
   for line in greeting(name,age):
     print(line)

 elif choice==8:
  print("Exiting program.....")
  print("Thank you for interacting..Goodbye...")
  break

 else:
  print("Invalid Choice,try again!")