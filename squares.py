# list comprehension: squares of numbers (1-20) divisible by 2 and 5
# for a number divisible by 2 and 5 both it should end with 0 that is also divisible by 10 also

for i in range(1,21):
    if i%10==0:
        square=i**2
        print(list([square]))
        
