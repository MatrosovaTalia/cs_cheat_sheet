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
print("Not num1 ", ~num1) 
print("Not num1 bug fix", ~num1 | 255) 
print("Not num2 ", ~num2)
print("Shift left num1 3 ", num1 << 3)     
print("Shift left num2 3 ", num2 << 3) 
print("Shift right num1 3 ", num1 >> 3)     
print("Shift right num2 3 ", num2 >> 3) 
print(~1) 

## Conditional expressions
num = 60

output = "The number is less than or equal to 50" \
    if num <= 50 else "The number is greater than 50"

print(output)

## Functions
# String.find()
random_string = "This is a string"
print(random_string.find("is"))  # First instance of 'is' occurs at index 2
print(random_string.find("is", 9, 13))  # No instance of 'is' in this range

llist = ['a', 'b', 'c']
print('>>'.join(llist)) # joining strings with >>
print('<<'.join(llist)) # joining strings with <<
print(', '.join(llist)) # joining strings with comma and space


# Lambdas
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))

my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))

def calculator(operation, n1, n2):
    return operation(n1, n2)

print(calculator(lambda n1, n2: n1 - n2, 30, 20))


nums = [-5, 0, 47, -10, 8, 2345]

positive = list(filter(lambda n : n > 0, nums))
print(positive)