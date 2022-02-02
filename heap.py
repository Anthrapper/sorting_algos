from read import get_data


def heapify(arr, n, i):
   largest = i
   l = 2 * i + 1 
   r = 2 * i + 2
   if l < n and arr[i].frequency > arr[l].frequency:
      largest = l
   if r < n and arr[largest].frequency > arr[r].frequency:
      largest = r
   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] 
      heapify(arr, n, largest)

def heapSort(arr):
   n = len(arr)
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] 
      heapify(arr, i, 0)

if __name__ == '__main__':
	myList = get_data()

	south=[_ for _ in myList if _.dir=='South']
	north=[_ for _ in myList if _.dir=='North']
	west=[_ for _ in myList if _.dir=='West']
	east=[_ for _ in myList if _.dir=='East']


	print('\n Frequent Travellers in West Zone !! \n')
	heapSort(west)
	for i in west:
		print(i)

	print('\n Frequent Travellers in East Zone !! \n')
	heapSort(east)
	for i in east:
		print(i)

	print('\n Frequent Travellers in North Zone !! \n')
	heapSort(north)
	for i in north:
		print(i)

	print('\n Frequent Travellers in South Zone !! \n')
	heapSort(south)
	for i in south:
		print(i)