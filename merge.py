from read import get_data

def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i].frequency >= right[j].frequency:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

if __name__ == '__main__':
    myList = get_data()

    south=[_ for _ in myList if _.dir=='South']
    north=[_ for _ in myList if _.dir=='North']
    west=[_ for _ in myList if _.dir=='West']
    east=[_ for _ in myList if _.dir=='East']

    
    print('\n Frequent Travellers in West Zone !! \n')
    mergeSort(west)
    for i in west:
        print(i)

    print('\n Frequent Travellers in East Zone !! \n')
    mergeSort(east)
    for i in east:
        print(i)

    print('\n Frequent Travellers in North Zone !! \n')
    mergeSort(north)
    for i in north:
        print(i)

    print('\n Frequent Travellers in South Zone !! \n')
    mergeSort(south)
    for i in south:
        print(i)