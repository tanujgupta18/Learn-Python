# Program 1
num1 = int(input("Enter Num 1: "))
num2 = int(input("Enter Num 2: "))
num3 = int(input("Enter Num 3: "))
num4 = int(input("Enter Num 4: "))

if (num1>num2 and num1>num3 and num1>num4):
  print("Number 1 is greatest")
elif (num2>num1 and num2>num3 and num2>num4):
  print("Number 2 is greatest")
elif (num3>num1 and num3>num2 and num3>num4):
  print("Number 3 is greatest")
elif (num4>num1 and num4>num2 and num4>num3):
  print("Number 4 is greatest")
else:
  print("Invalid Input")

# Program 2
m1 = int(input("Enter marks of sub1: "))
m2 = int(input("Enter marks of sub2: "))
m3 = int(input("Enter marks of sub3: "))

total_marks = m1+m2+m3
avg = total_marks/3

if (m1>33 and m2>33 and m3>33 and avg>=40):
  print("You are passed")
else:
  print("You are Failed")

# Program 3
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
  print("Spam Comment")
else:
  print("Not spam comment")

# Program 4
username = input("Enter your username: ")
if (len(username)<10):
  print("Too short username")
else:
  print("All is well")


# Program 5
list = ["Himanshu","Tanmay","Rohan"]

name = input("Enter name: ")
if(name in list):
  print("Your name is in list")
else:
  print("Your name is not in list")

# Program 6
marks = int(input("Enter your marks: "))
if (marks>90 and marks<=100):
  print("Your Grade is O")
elif (marks>80 and marks<=90):
  print("Your Grade is A")
elif (marks>70 and marks<=80):
  print("Your Grade is B")
elif (marks>60 and marks<=70):
  print("Your Grade is C")
elif (marks>=50 and marks<=60):
  print("Your Grade is D")
elif (marks<50):
  print("Your Grade is F")
else:
  print("Invalid Input")

# Program 7
post = input("Enter you post: ")
if ("Developer" in post):
  print("This post is talking about developer")