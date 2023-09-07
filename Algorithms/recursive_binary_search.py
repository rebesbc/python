# recursive binary search
# def: función o bloque de código

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # utilizar [num:] hace que python considere :] como todo lo que hay en el arreglo después de num
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                # utilizar [num:] hace que python considere :] como todo lo que hay al inicio, hasta topar con midpoint
                return recursive_binary_search(list[:midpoint], target)
            
def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)