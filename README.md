# Python Dictionary Comprehension

## Explanation

Dictionary comprehension is a concise way to create dictionaries using an expression and an iterable. It can also include conditions to filter data.

## Problem Statement

Write a Python program using dictionary comprehension to create a dictionary containing numbers and their squares, and another dictionary containing only even numbers and their squares.

## Features

* Demonstrates dictionary comprehension
* Creates key-value pairs
* Calculates squares
* Filters even numbers
* Uses concise Python syntax

## How It Works

1. A range of numbers from 1 to 10 is created.
2. Dictionary comprehension creates a dictionary where each number is a key and its square is the value.
3. A condition is used to create another dictionary containing only even numbers.
4. Both dictionaries are displayed.

## Technologies Used

* Python 3
* Dictionary Comprehension

## Program Flow

Start → Create Number Range → Create Square Dictionary → Filter Even Numbers → Create Second Dictionary → Display Results → End

## Sample Input

```text
No user input required.
```

## Sample Output

```text
Squares Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
Even Squares Dictionary: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

## Key Learning

* Dictionary comprehension provides a concise way to create dictionaries.
* It creates key-value pairs from an iterable.
* Conditions can be used to filter elements.
* The basic syntax is:
  `new_dict = {key: value for item in iterable if condition}`

## File Location

```text
Python-Dictionary-Comprehension/dictionary_comprehension.py
```

## Repository Structure

```text
Python-Dictionary-Comprehension/
│
├── dictionary_comprehension.py
└── README.md
```

## Author

V.Harini
