numbers = range(1, 11)

squares = {number: number * number for number in numbers}

even_squares = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print("Squares Dictionary:", squares)
print("Even Squares Dictionary:", even_squares)
