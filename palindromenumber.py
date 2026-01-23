num = int(input("Enter number: "))
rev = int(str(num)[::-1])

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
