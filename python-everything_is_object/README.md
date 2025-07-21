# Python – Objects, References, and Mutability

## Introduction

When learning Python, it’s essential to understand how the language manages **objects**, their **identity**, and their **mutability**. These concepts govern how variables reference data in memory, how data changes (or doesn’t), and how function arguments behave under the hood. Misunderstanding these can lead to confusing bugs, especially with mutable objects like lists and dictionaries. In this post, I’ll walk you through Python’s object model, the difference between mutable and immutable types, and what this means for passing variables to functions.

---

## `id()` and `type()`: Understanding Object Identity and Type

Every object in Python has a **type** (like `int`, `list`, or `str`) and a unique **identity**. The `type()` function tells you what kind of object you have:

```python
a = 42
print(type(a))  # <class 'int'>

b = [1, 2, 3]
print(type(b))  # <class 'list'>
```

The identity of an object is its address in memory, which you can see using id():

```python
print(id(a))  # e.g. 140320842982512
print(id(b))  # e.g. 140320875095040
```

Two variables may have the same value but different identities:

```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True (same content)
print(x is y)  # False (different objects)
```

---

## Mutable Objects

Mutable objects can be changed after creation. Common built-in mutable types include:

- `list`
- `dict`
- `set`
- `bytearray`

Example :

```python
lst = [1, 2, 3]
print(id(lst))  # e.g. 140320875095040
lst.append(4)
print(lst)      # [1, 2, 3, 4]
print(id(lst))  # Same id! The list was modified in place
```

Since the object is modified in place, any other variable referencing the same object will see the change:

```python
a = lst
a.append(5)
print(lst)  # [1, 2, 3, 4, 5]
```

---

## Immutable Objects

Immutable objects cannot be changed after creation :

- `int`
- `float`
- `str`
- `tuple`
- `frozenset`
- `bytes`

Example with integers:

```python
a = 100
b = 100
print(a is b)  # True (small integers are cached)
a = a + 1
print(a)       # 101
print(b)       # 100
```

The operation `a = a + 1` creates a new integer object and reassigns `a`. The original integer 100 remains unchanged, so b still references 100.

---

## Why Does It Matter? How Python Treats Mutable and Immutable Objects Differently

The difference between mutable and immutable objects affects how Python manages variables and memory.

- Immutable objects can be safely shared because their content cannot change.

- Mutable objects can cause unintended side effects if shared references are modified unexpectedly.

This has implications for aliasing:

```python
x = [1, 2]
y = x       # y references the same list as x
y.append(3)
print(x)    # [1, 2, 3]
```

Here, modifying `y` modifies `x` as well, because both refer to the same list.

---

## How Arguments Are Passed to Functions and What That Implies

Python passes references to objects to functions (sometimes called “pass-by-object-reference” or “pass-by-assignment”).

- If the object is mutable, the function can modify the object and changes persist outside the function.

- If the object is immutable, attempts to modify it create new objects and do not affect the caller’s variable.

Example with mutable:

```python
def append_item(lst):
    lst.append(4)

my_list = [1, 2, 3]
append_item(my_list)
print(my_list)  # [1, 2, 3, 4]
```

Example with immutable:

```python
def add_one(n):
    n = n + 1
    print(n)  # prints 43

num = 42
add_one(num)
print(num)    # still 42
```

---

## Advanced Learnings: Interning and Object Caching

In Python, small integers (usually from -5 to 256) and some strings are interned, meaning the same object is reused to optimize memory.

```python
a = 256
b = 256
print(a is b)  # True

a = 257
b = 257
print(a is b)  # False (usually)
```

Similarly for strings:

```python
s1 = "hello"
s2 = "hello"
print(s1 is s2)  # True

s3 = "".join(["he", "llo"])
print(s1 == s3)  # True
print(s1 is s3)  # False
```

This knowledge is useful to understand subtle behaviors when comparing with is vs ==.

---

## Conclusion

Understanding Python’s object model identity, mutability, and how arguments are passed is crucial for writing bug-free, efficient programs. Knowing when objects are shared, when copies are made, and how Python handles values in memory can save hours of debugging. Experiment with these concepts yourself by printing `id()`, comparing with `is` and `==`, and observing how mutations propagate.
