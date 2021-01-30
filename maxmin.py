
adet = int(input("enter length of the list: "))

list = []

for s in range(adet):
    number = int(input(f'{s+1}. number:'))
    list.append(number)
    numberTuple = tuple(list)

# The function and algorithm that can find the max and min values of a list of numbers is defined below.
def maxminFinder(tuple):
    print(type(tuple),tuple) #To show that the received parameter is a tuple.

    max = tuple[0]
    for num in tuple[1:]:
        if (max < num):
            max = num


    min = tuple[0]
    for num1 in tuple[1:]:
        if (min > num1):
            min = num1

    tupleResult = (max,min)

    return print('Max and Min values: ',tupleResult)

maxminFinder(numberTuple)