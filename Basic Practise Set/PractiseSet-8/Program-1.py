def greatestNumber():
  a = int(input("Enter Number1: "))
  b = int(input("Enter Number2: "))
  c = int(input("Enter Number3: "))

  if (a>b and a>c):
    print(f"{a} is greatest among three")
  elif (b>c and b>a):
    print(f"{b} is greatest among three")
  elif (c>b and c>a):
    print(f"{c} is greatest among three")

greatestNumber()