def multiplicationTable():
  n = int(input("Enter Number: "))
  for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
  
multiplicationTable()