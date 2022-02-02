import itertools
from read import get_data


def heapify(arr, n, i,frq):

   largest = i
   l = 2 * i + 1 
   r = 2 * i + 2
   
   if l < n and arr[i].get(frq) > arr[l].get(frq):
	  
      largest = l
   if r < n and arr[largest].get(frq) > arr[r].get(frq):
      largest = r
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] 
      heapify(arr, n, largest,frq)

def heapSort(arr,frq):
   n = len(arr)
   for i in range(n, -1, -1):
      heapify(arr, n, i,frq)
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] 
      heapify(arr, i, 0,frq)

if __name__ == '__main__':
	myList = get_data()
	limit=3

	print('\n Frequent Travellers in 1st Quarter !! \n')
	heapSort(myList,'q1')
	for item in itertools.islice(myList, 0, limit):
		print(item)

	print('\n Frequent Travellers in 2nd Quarter !! \n')
	heapSort(myList,'q2')
	for item in itertools.islice(myList, 0, limit):
		print(item)

	print('\n Frequent Travellers in 3rd Quarter !! \n')
	heapSort(myList,'q3')
	for item in itertools.islice(myList, 0, limit):
		print(item)

	print('\n Frequent Travellers in 4th Quarter !! \n')
	heapSort(myList,'q4')
	for item in itertools.islice(myList, 0, limit):
		print(item)

	print('\n Frequent Travellers in the year !! \n')
	heapSort(myList,'frequency')
	for item in itertools.islice(myList, 0, limit):
		print(item)