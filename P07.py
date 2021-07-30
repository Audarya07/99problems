# Flatten a nested list structure.

def flat(element, flat_list):
    if not isinstance(element, list):
        flat_list.append(element)
    else:
        for i in range(len(element)):
            flat(element[i], flat_list)


def flatten(arr, flat_list):
    flat(arr, flat_list)
    return flat_list

if __name__ == "__main__":
    array = [1, 2, [4, 3], 6, [3, [4,5]]]
    print("Nested List = ", array)
    
    flat_list = []
    flatten(array, flat_list)
    print("Flattened list = ", flat_list)