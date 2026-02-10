# Write a program that iterates through a list, skips negative numbers, stops execution at zero, and handles non-integer values using exception handling.
def process_list(values):
    for item in values:
        try:
            num = int(item)
            
            if num < 0:
                continue
            
            if num == 0:
                print("Encountered zero. Stopping execution.")
                break
            
            print("Processing:", num)
        
        except ValueError:
            print(f"Skipping non-integer value: {item}")
            
data = [10, -5, "hello", 3.5, 0, 7, 12]
process_list(data)