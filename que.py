Question 1

n = int(input("enter your number"))

for i in range(1,n+1):
    print(i)

Question 2 

n= int(input("enter your number"))

for i in range(n,-1,-1):
    print(i)

Question 3

n= int(input("enter your number"))

for i in range(n,(n*10)+1,n):
    print(i)
         or

n= int(input("enter your number"))

for i in range(1,11):
    print(f"{n}* {i} = {n* i}")


Question 4

n= int(input("enter your number"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)

Question 5

n = int(input("enter your number"))
fact = 1

for i in range(1,n+1):
    fact= fact * i
print(fact)
    

Question 6

n = int(input("enter your number"))
print("all the factors are")
for i in range(1,n+1):
    if n % i ==0:
        print(i,end = " ") 

Question 7

n = int(input("enter your number"))
sum = 0

for i in range(1,n):
    if n%i==0:
        sum = sum+i
# print(sum)
if sum == n:
    print("yes this is a strong number")
else:
    print("not a strong number")   

Question 8

n= int(input("enter your number"))
count= 0 

for i in range(1,n+1):
    if n%1== 0 :
        count = count + 1
if count == 2:
    print(f"{n} is a prime number")
else:
    print(f"{n} is composite number")

Question 9

a= int(input("enter your number"))
while a > 0:
    print(a%10)
    a = a//10

Question 10

n = int(input("tell your number"))
copy = n
rev = 0
while n> 0 :
    a= n%10
    rev = rev * 10 + a
    n =n // 10
print(rev)

if copy == rev:
    print("PALLINDROM NUMBER")

else:
    print("NOT A PALLINDROM NUMBER")

question 11

num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:    print("both numbers are equal")

question 12
Q12 Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender)

gender = input("enter your gender (M/F): ")

if gender == "M " or gender == "Male" or gender == "m" :
    print("Good Morning Sir")
elif gender == "F" or gender == "Female" or gender == "f":
    print("Good Morning Ma'am")
else:
    print("Invalid gender")

Q13. Accept an integer and check whether it is an even number
or odd.

num = int(input("enter your number"))

if num%2 == 0:
    print(f"{num} is an even number")
else:    print(f"{num} is an odd number")

Q14. Accept name and age from the user. Check if the user is a
valid voter or not.
Ex- “hello shery you are a valid voter”

name = input("enter your name")
age = int(input("enter your age"))

if age>= 18:
    print(f"{name} is a valid voter")
else:    print(f"{name} is not a valid voter")

Q15. Accept a year and check if it a leap year or not (google to
find out what is a leap year)

