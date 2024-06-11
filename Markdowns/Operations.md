# Python Operations Overview

## Table of Contents
- [Loops](#loops)
- [Dictionaries](#dictionaries)
- [Functions](#functions)
- [Methods](#methods)
- [Classes](#classes)

---

## Loops

Loop operations enable consistent modification of an iterable, continual behavior until a condition is met, and more. When possible, it is best to avoid redundant code and loops are one way to do this. 

### For Loop
The `for` loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).

```python
# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### While Loop
The `while` loop continues as long as a specified condition is `True`.

```python
# Example: Using a while loop
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control Statements
- `break`: Terminates the loop statement and transfers execution to the statement immediately following the loop.
- `continue`: Causes the loop to skip the remainder of its body and immediately retest its condition before reiterating.

```python
# Example: Using break and continue
for number in range(10):
    if number == 5:
        break  # Exit loop when number is 5
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
```


## Dictionaries

A dictionary in Python is a mutable, unordered collection of items. Each item is a key-value pair. Dictionaries are indexed by keys, which can be any immutable type such as strings, numbers, or tuples.

#### Creating a Dictionary

```python
# Creating an empty dictionary
my_dict = {}

# Creating a dictionary with initial key-value pairs
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
```

#### Accessing Values

```python
# Accessing values by key
name = my_dict['name']  # Output: 'Alice'
age = my_dict.get('age')  # Output: 25

# Using get() to avoid KeyError if the key doesn't exist
country = my_dict.get('country', 'Not Found')  # Output: 'Not Found'
```

#### Modifying a Dictionary

```python
# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'

# Updating an existing key-value pair
my_dict['age'] = 26
```

#### Removing Items

```python
# Using pop() to remove a key-value pair by key
age = my_dict.pop('age')  # Removes 'age' and returns its value

# Using del to remove a key-value pair by key
del my_dict['city']
```

#### Iterating Over a Dictionary

```python
# Iterating over keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

## Functions

Functions are blocks of code that only run when they are called. You can pass data, known as parameters, into a function.

### Defining a Function
Use the `def` keyword to define a function.

```python
# Example: Defining and calling a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

### Parameters and Arguments
Functions can take arguments, which are specified after the function name inside the parentheses.

```python
# Example: Function with parameters
def add(a, b):
    return a + b

result = add(2, 3)
print(result)  # Output: 5
```

### Default Parameters
You can define default parameter values.

```python
# Example: Function with default parameter
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())       # Output: Hello, World!
print(greet("Bob"))  # Output: Hello, Bob!
```

### Parameter Variable Names
When passing arguments to a function, the variable name can be explicitly passed with the parameter. This can help detail what parameters mean and is especially helpful for functions with many arguments.

```python
# Example: Function with parameters
def add(a, b):
    return a + b

result = add(a=2, b=3)
print(result)  # Output: 5
```

## Classes

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object.

### Defining a Class
Use the `class` keyword to define a class.

```python
# Example: Defining a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Creating an instance of Person
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hi, I'm Alice and I'm 30 years old.
```

## Methods

Methods are functions that are defined inside the body of a class. They are used to perform operations with the attributes of the class.

### Example of Methods
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy")
print(my_dog.bark())  # Output: Buddy says woof!
```

---
