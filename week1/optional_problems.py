"""
1. You are given as input an unsorted array of n distinct numbers, where n is a power of 2.
Give an algorithm that identifies the second-largest number in the array, and that uses at
most n+log2⁡n−2 comparisons.
"""


"""
2. You are a given a unimodal array of n distinct elements, meaning that its entries are
in increasing order up until its maximum element, after which its elements are in
decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.
"""

def get_max(arr):
	if len(arr) < 2:
		return arr
	mid = len(arr)//2
	a = arr[:mid]
	b = arr[mid:]
	return get_max(a if a[-1] > b[0] else b)

"""
3. You are given a sorted (from smallest to largest) array A of n distinct integers which can be
positive, negative, or zero. You want to decide whether or not there is an index i such that
A[i] = i. Design the fastest algorithm that you can for solving this problem.
"""
def index_match(arr):
    for item in array:
        if array[item] == item:
            return True
    return False

