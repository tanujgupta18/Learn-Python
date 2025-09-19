# Program 1
s = {
  "madad":"Help",
  "kutta":"Dog",
  "Thapad":"Slap"
}
word = input("Enter word to search that word: ")
print(s[word])

# Program 2
s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)

# Program 3
s = set()
s.add(18)
s.add("18")

print(s)

# Program 4
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s))


# Program 5
dict = {}
name = input("Enter your Name: ")
lang = input("Enter your Language: ")
dict.update({name:lang})

name = input("Enter your Name: ")
lang = input("Enter your Language: ")
dict.update({name:lang})

name = input("Enter your Name: ")
lang = input("Enter your Language: ")
dict.update({name:lang})

name = input("Enter your Name: ")
lang = input("Enter your Language: ")
dict.update({name:lang})

print(dict)


# Program 6
s = {8, 7, 12, "Harry", [1,2]}
s[4][0] = 9