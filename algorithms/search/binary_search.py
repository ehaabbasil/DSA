"""
Binary Search Algorithm 

Runs in log n Time 

"""

def binary_search(data, target, low, high):

	""" Return tue if target is found in indicated portion of a list """


	print(f"binary search:{data}")

	if low > high:

		return False

	else:
		mid = (low+high)//2

	if target == data[mid]:
		print(mid)

		return True

	elif target < data[mid]:

		# recur the portion left of the middle 

		return binary_search(data, target, low, mid - 1)


	else: 
		# recur the portion right of the middle 

		return binary_search(data, target, mid + 1, high)




binary_search([2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37],22,0,15)