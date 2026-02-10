# Write a user-defined function that returns the largest and smallest values from a list without using built-in functions


def mini_max(numbers):
    smallest = numbers[0]
    largest = numbers[0]
    
    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    
    return smallest, largest

lst = [12, 5, 8, 19, 3, 25, 7]
smallest, largest = mini_max(lst)
print("Smallest:", smallest)
print("Largest:", largest)