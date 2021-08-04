# Sorting a list of lists according to length of sublists

def sort_on_length(arr):
    '''Sort given multi-dimensional list according to length of it's sublist.
    
    Parameters :
        arr (List) : Array which is to be sorted.
    
    Returns :
        arr (List) : Sorted array according to length of the sublist.
    '''
    
    return sorted(arr, key=len)


if __name__ == "__main__":
    arr = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]

    print(f'Array before sorting: {arr}')

    new_arr = sort_on_length(arr)
    print(f'Array after sorting: {new_arr}')