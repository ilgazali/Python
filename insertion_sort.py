
size = int(input("Enter size of the number list: "))

theList = []

for i in range(size):
    num = int(input("Enter a number: "))
    theList.append(num)
print("scrambled list of numbers-->",theList)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSort(theList)

print("sorted list of numbers-->",theList)

