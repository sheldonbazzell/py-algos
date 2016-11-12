import random

def bubbleSort(list):
	list = []
	#populate empty list
	for n in range(100):
		list.append(random.randint(1, 10000))
	#iterate thru list
	for i in range(0, len(list)-1):
		#iterate thru sorted list, stopping after swapping the list's final 2 values
		for j in range(0, len(list)-1-i):
			#if next value in list is greater than j
			if list[j] > list[j+1]:
				#swap the values
				list[j], list[j+1] = list[j+1], list[j]

bubbleSort(list)