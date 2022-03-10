s = "mama myla ramy"
# s[3] = "s"
s = "hello?"
print(s)


x = 3
# print(len(x))

x = 3.126345
print("%.2f" % x)

# Comparison '==' vs 'is'

num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects

# Bitwise Operations
num1 = 10    # = 
num2 = 20
print(num1 & num2)   # 0   -> Binary value = 00000
print(num1 | num2)   # 30  -> Binary value = 11110
print(num1 ^ num2)   # 30  -> Binary value = 11110
print("Not num1 ",  ~num1) 
print("Not num2 ", ~num2)
print("Shift left num1 3 ", num1 << 3)     
print("Shift left num2 3 ", num2 << 3) 
print("Shift right num1 3 ", num1 >> 3)     
print("Shift right num2 3 ", num2 >> 3)  

