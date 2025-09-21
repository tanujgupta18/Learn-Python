# Program 1
num = int(input("Enter a number: "))
for i in range(1,11):
  print(f"{num} x {i} = {num*i}")

# Program 2
l = ["Jacky", "Soham", "Sachin", "Rahul"]

for item in l:
  if item.startswith("S"):
    print(item)


# Program 3
num = int(input("Enter a number: "))

i = 1
while(i<11):
  print(f"{num} x {i} = {num*i}")
  i += 1

# Program 4
num = int(input("Enter number: "))

for i in range(2,num):
  if (num%i)==0:
    print("Number is not prime")
    break
else:
    print("Number is prime")

# Program 5
num = int(input("Enter number: "))
i = 1
sum = 0
while(i<=num):
  sum += i
  i += 1

print(sum)

# Program 6
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
  fact = fact * i
else:
  print(f"Factorial of {num} is {fact}")

# Program 7
'''
Star Pattern Question

for n = 3

  *
 ***
*****

'''

num = int(input("Enter the number: "))

for i in range(1,num+1):
  print(" " * (num-i), end="")
  print("*"* (2*i-1), end="")
  print("")

# Program 8
'''
Star Pattern Question

for n = 3

*
***
*****

'''

num = int(input("Enter the number: "))

for i in range(1,num+1):
  print("*" * i,end="")
  print("")

# Program 9
'''
Star Pattern Question

for n = 3

***
* *
***

'''

num = int(input("Enter the number: "))
for i in range(1,num+1):
  if (i==1 or i==num):
    print("*"*num,end="")
  else:
    print("*",end="")
    print(" "*(num-2),end="")
    print("*",end="")
  print("")

# Program 10
n = int(input("Enter number: "))

for i in range(10,0,-1):
  print(f"{n} x {i} = {n*i}")