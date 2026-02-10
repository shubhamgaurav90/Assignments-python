# list comprehension: squares of numbers (1-20) divisible by 2 and 5
# for a number divisible by 2 and 5 both it should end with 0 that is also divisible by 10 also

squares = [n**2 for n in range(1, 22) if (n**2) % 10 == 0]
print(squares)
