class Solution(object):

	def merge_sort(self, arr):
		if len(arr) <= 1:
			return arr
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		# break left and right subarrays
		# into arrays of length 1
		left = self.merge_sort(left)
		right =	self.merge_sort(right)
		return self.merge(left, right)


	def merge(self, left, right):
		# save from invoking unecessary recursive calls
	    if not left:
	        return right
	    if not right:
	        return left
	    if left[0] < right[0]:
	        return [left[0]] + self.merge(left[1:], right)
	    return [right[0]] + self.merge(left, right[1:])