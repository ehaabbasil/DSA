
# Brute Force 
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

# Optimal 
def max_pairwise_product_optimized(numbers):
    n = len(numbers)
    max_product = 0

    first, second = 0,0 

    for num in numbers:
        
        if num > first:
            first , second = num, first

        elif num > second:
            second = num

    return (first)*(second)

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))




