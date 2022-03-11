# Python Internals

### Truth Value Testing
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object.  Here are most of the built-in objects considered false:

* constants defined to be false: None and False.

* zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)

* empty sequences and collections: '', (), [], {}, set(), range(0)

## Built-in types
### Numbers
Value of an integer is not restricted by the number of bits and can expand to the limit of the available memory.

### Strings
Strings are immutable.

Unicode includes ASCII.
3.x - all strings are unicode.
2.x - strings are ASCII, to use unicode:
``` str = u"Unicode string"```


```python
s = "hello, I am a string s"
s = "hi, I am another string"  # legal
s[4] = "a"                     # illegal
```
len(str) is a function. 

### String formatting 
The %s is the format specifier, which tells Python to insert the text here. Python will insert a string if:
* the string with a % and another string.
* the string with a % and another string type variable.

%f is used to substitute floats within a string. 
%.xf - limit number after comma by x. 
```3.126456 -> %.2f -> 3.13```

### String slicing
str[start:end:step]


```python 
my_string = "Hello, I am a friendly string."
print(my_string[:7])  # All the characters before 'I'
print(my_string[7:])  # All the characters starting from 'I'
print(my_string[:])  # The whole string
print(my_string[::-1])  # The whole string in reverse (step is -1)
print(my_string[::-1]) # The string in reverse (step is -2)
```

### NoneType
It only has a single value, None. 

Can assign None to any variable.
Cannot create other NoneType variables.

* None is not a default value for the variable that has not yet been assigned a value.
* None is not the same as False.
* None is not an empty string.
* None is not 0.

## Operations

### Comparisons
The == and != operators compare the values of both operands. 
However, the identity operators, is and is not, check whether the two operands are the exact same object.
```python 
num1 = 5
num2 = 10
num3 = 10
list1 = [6,7,8]
list2 = [6,7,8]

print(num2 == num3)  # Both have the same value
print(num3 != num1)  # Both have different values

print(num2 is not num3)  # Both have the same object
print(list1 is list2)  # Both have the different objects
```

When two strings have different lengths, the string which comes first in the dictionary is said to have the smaller value.

### Ternary expression
```python
output_true if condition else output_false
```

### Bitwise Operations
Left Shift '<<' increases
Right Shift'>>' decreases
|
~ a tricky one: ~1 = -2

## Functions

### Strings funcitons
Functions that are properties of a particular entity are known as **methods**. 

`find(substring, start, end)` returns the first index at which a substring occurs in a string. 
If no instance of the substring is found, the method returns -1.

`replace(substring_to_be_replaced, new_string)` - replace string_to_be_replaced by the new_string.

`upper()`/`lower()` - changes uppercase to lower case and vice versa.

`'separator'.join(list)` - joins elements of the list with separators.

`"Learn Python {} at {}".format(3, "Educative")` - format string.

### Type conversions
`ord()` - This function can be used to convert a character to its Unicode value:
```python
print(ord('a'))  -> 97
print(ord('0'))  -> 48
```

## Lambdas
A lambda is an anonymous function that returns some form of data.

Lambdas are defined using the lambda keyword. Since they return data, it is a good practice to assign them to a variable.

A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.



