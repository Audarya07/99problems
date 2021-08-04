# Generate the combinations of K distinct objects chosen from the N elements of a list.

def generate_combination(arr, n, r):
    ''' A function to generate combination of size r.
    
    Parameters:
        arr (List): Input array.
        n (int): Size of input array.
        r (int): Size of combination to be generated.
    '''

	# Temporary array to store all combination
    data = [0] * r

    helper(arr, n, r, 0, data, 0)


def helper(arr, n, r, index, data, i):
    ''' A helper function to generate combination of size r.
    
    Parameters:
        arr (List): Input array.
        n (int): Size of input array.
        r (int): Size of combination to be generated.
        index (int): Current index in data array.
        data (List): Temporary array to store current combination.
        i (int):Index of current element in arr
    '''

    if (index == r):
        for j in range(r):
            print(data[j], end = " ")
        print()
        return
    
    if (i >= n):
        return

    data[index] = arr[i]
    helper(arr, n, r, index + 1, data, i + 1)
    helper(arr, n, r, index, data, i + 1)

if __name__ == "__main__":
    arr = ['a','b','c','d','e','f']
    r = int(input("Enter size of combination: "))
    n = len(arr)
    generate_combination(arr, n, r)
