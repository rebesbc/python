def merge_sort(list):
    # ordenar una lista dada de manera ascendente
    # devuelve una nueva lista, ahora ordenada
    #
    # instrucciones
    # dividir: hallar el punto medio de la lista y partirlo en dos sublistas
    # determinar: recursivamente clasificar las listas
    # combinar: fusionar las sublistas en una sola

    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    # divide la lista desordenada por la mitad, en dos sublistas
    # devuelve dos sublistas, left y right

    mid = len(list) // 2
    left = list[:mid] # no incluye el midpoint
    right = list[mid:]

    return left, right