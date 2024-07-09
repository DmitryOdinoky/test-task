def sum_of_digits_upto_n(n):
    # Initialize result
    result = 0
    
    # Go through every digit position
    i = 1
    while i <= n:
        # Compute the values for the current digit position
        current = (n // i) % 10
        higher = n // (i * 10)
        lower = n - (n // i) * i
        
        # Add the contribution of the current digit position
        result += higher * i
        if current > 0:
            result += (current * (current - 1) // 2) * i
            result += (current * (lower + 1))
        else:
            result += (current * (current - 1) // 2) * i
        
        i *= 10
    
    return result

def main():
    # Define the range
    n = 10**12
    
    # Calculate the sum of all digits from 0 to n
    total_sum = sum_of_digits_upto_n(n)
    
    # Print the result
    print('=== Task 4 ===')
    print(f"The sum of all digits of all natural numbers from 0 to {n} is: {total_sum}")
    print(" ")

if __name__ == "__main__":
    main()
