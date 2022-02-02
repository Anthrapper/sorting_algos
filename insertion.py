from read import get_data

def insertionSort(data): 
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >=0 and key.frequency > data[j].frequency:
                data[j+1] = data[j]
                j -= 1
        data[j+1] = key

data=get_data() 
print("Before sorting: \n")
for e in data:
    print(e)

print("\nAfter sorting: \n")
insertionSort(data)
for e in data:
    print(e)