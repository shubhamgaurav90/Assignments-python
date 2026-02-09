# write a python script that accepts a number from the command line and checks whether the number it is prime. Explain how command-line arguements are accessed.
import sys
n=int(sys.argv[1])
prime=True
for i in range(2,n): #range is from 2 to n-1 because it checks the divisibility
    if n%i==0:
        prime=False
        break
if prime:
     print(f"{n} is prime")
else:
     print(f"{n} is not prime")