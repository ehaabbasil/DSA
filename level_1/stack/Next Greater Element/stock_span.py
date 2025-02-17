 # Stack 
# Stock Span - next greater element left

# Algo 
	# pop , answer, push 


def sol(arr=[2, 5, 9, 3, 1, 12, 6, 8, 7]):
    n = len(arr)
    span = [0] * n  # Initialize span list with zeros
    stack = []  # Stack to keep track of indices

    for i in range(n):
        # Pop elements from the stack while the current element is greater than or equal to the element at the top of the stack
        while stack and arr[i] > arr[stack[-1]]:
            stack.pop()

        # If the stack is empty, the current element is the greatest so far
        if not stack:
            span[i] = i + 1
        else:
            # Otherwise, the span is the difference between the current index and the index at the top of the stack
            span[i] = i - stack[-1]

        # Push the current index onto the stack
        stack.append(i)

    return span

print(sol())