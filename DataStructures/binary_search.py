# binary search
# def: función o bloque de código

def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        # // es una división con resultado de un número entero
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
            
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


# pruebas
numbers = range(1, 10)

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)