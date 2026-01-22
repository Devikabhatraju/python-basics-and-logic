num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
