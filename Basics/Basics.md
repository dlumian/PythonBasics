# Basic Python

Python is a general purpose programming language with considerable and growing resources for data science. 

This README.md and [associated notebook](./Basics.ipynb) introduce Python data types, variable assignment, and common built-in functionality.

See [README.md in parent folder](../README.md) for general overview.

See [Jupyter Notebooks](./../Markdowns/JupyterNotebooks.md) for guidance on using notebooks.

Comments are indicated by the `#` symbol. These lines are not executued when running code cells.

Notebook Topics:
- [Data Types](#data-types)
- Math
- String Manipulation
- Lists
- Dictionaries
- Booleans
- [Assignment, Comparison, and Evaluations](#variable-setting-vs-evaluationcomparison)
- [Built-in Functions](#built-in-functions)

## Data Types
Information is stored in a vareity of data types. This may be for computational efficiency, functional differences between the types, or a number of other factors. It is important to know that data types vary in how they operate, so ensuring proper data types can help minimize issues. 

#### Data Types Covered
- **Integers:** represent whole numbers, such as 1, 2, and 3. Integers can be positive or negative.
- **Floats:** represent floating-point numbers, such as 3.14 and 2.718. Floats can be positive or negative.
- **Strings:** represent text, such as "Hello, world!" and "This is a string." Strings can be any length and can contain any characters.
- **Booleans:** represent `True` or `False` values. Booleans are often used to control the flow of a program.
- **Lists:** represent a mutable set of objects for iteration and flow
- **Dictionaries:** A set of key:value pairs where keys are unique and values may represent single values, strings, lists or more.

**NOTE:** See [Operations readme](../Markdowns/Operations.md) for more details on lists and dictionaries. 

## Variable Setting vs Evaluation/Comparison

#### Variable Setting

Variable setting (or assignment) is the process of assigning a value to a variable. This is done using the `=` operator.

```python
# Variable setting
x = 10  # x is now assigned the value 10
y = 'Hello'  # y is now assigned the value 'Hello'
```

#### Variables

Python uses variables to create complex workflows in an intelligible manner. Variable assignment helps simplify complex or abstract designs. Defining a dataframe as `df` faciliates manipulations and analysis by providing a single reference to that object. Variable naming can become confusing, so it is best to [find a naming convention](https://peps.python.org/pep-0008/) that works for you and to stick to it.

#### Evaluation/Comparison

Evaluation (or comparison) involves checking the value of a variable against another value. This is typically done using comparison operators such as `==`, `!=`, `<`, `>`, `<=`, `>=`.

```python
# Evaluation/Comparison
is_equal = (x == 10)  # True, because x is equal to 10
is_not_equal = (y != 'Hello')  # False, because y is 'Hello'

# Other comparisons
is_greater = (x > 5)  # True, because 10 is greater than 5
is_less_or_equal = (x <= 10)  # True, because 10 is equal to 10
```

### Key Points

- **Assignment**: Uses the `=` operator to assign a value to a variable.
- **Comparison**: Uses operators like `==`, `!=`, `<`, `>`, `<=`, `>=` to compare values.

**NOTE:** This is a basic introduction, many more methods of comparison exist. Strings for example offer methods such as `in`, `startswith`, and `endswith` for additioanl types of comparisons. 

## [Built-in functions](https://docs.python.org/3/library/functions.html)
- Python has many functions by default, known as `built-in` 
- Functions expect a certain type of input and often a certain number of inputs, and will return either a value or `None` 
- Functions can have both required and optional inputs
- Check the documentation of the code being used to understand required inputs and expected outputs
- If a value is returned, it can be assigned to a new variable.
- If `None` is returned, the function may modify an existing object or generate an output that is not code (e.g., writing a file).

#### Example Functions in this Notebook:
- **print:** returns value or description of object
- **type:** returns the datatype of the object
- **any:** checks if any passed objects evaluate to `True`
- **all:** checks if all passed objects evaluate to `True`
- **help:** returns documentation of passed object
- **isinstance:** returns `True` if type of arg1 matches arg2
- **len:** returns the length of an object