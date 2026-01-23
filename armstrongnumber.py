num = int(input("Enter number: "))
temp = num
sum = 0
digits = len(str(num))

while temp > 0:
    d = temp % 10
    sum += d ** digits
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")
