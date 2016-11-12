import random
def selectionSort(list):
	list = []
	temp = 0
	# populate empty list
	for n in range(100):
		list.append(random.randint(1,10000))
# 	# iterate thru our list, less the last value
	for i in range(len(list)-1):
		min = i
# 		# iterate thru our unsort list to find minimum value
		for j in range(i + 1, len(list)):
			if list[j] < list[min]:
				min = j
# 		# if the first value of our unsorted list is less than our newly set min..
		if i != min:
			temp = list[i]
			list[i] = list[min]
			list[min] = temp

selectionSort(list)