class Solution(object):

	def quick_sort(self, arr, left, right):
		# sort arr if len is > 1
		if len(arr) > 1:
			if left is None:
				left = 0
				right = len(arr) - 1
			index = self.partition(arr, left, right)
			if left < index - 1:
				self.quick_sort(arr, left, index-1)
			if index < right:
				self.quick_sort(arr, index, right)
		return arr

	def partition(self, arr, left, right):
		pivot = arr[(right + left) // 2]
		i = left
		j = right
		while i <= j:
			while arr[i] < pivot:
				i +=1
			while arr[j] > pivot:
				j -=1
			if i <= j:
				self.swap(arr, i, j)
				j -=1
				i +=1
		return i

	def swap(self, arr, i, j):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp

s1 = Solution()
test = [2,5,1,6,3,4]
print s1.quick_sort(test, None, None)

		