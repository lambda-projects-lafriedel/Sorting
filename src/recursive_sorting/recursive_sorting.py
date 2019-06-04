# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # These 2 lines are creating a new list that has the length of 'elements' and is being instantiated with 0s as placeholders
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Loop through arrA's indices, compare them to the indices of arrB.
    # If i of arrA is smaller than i of arrB, set arrA[i] to the next index of merged_arr. Else, set arrB[i] as the next index
    i = 0
    for i in range(len(arrA)):
        print(i, arrA, arrB)
        if arrA[i] < arrB[i]:
            merged_arr[i] = arrA[i]
            arrA.remove(arrA[i])
        else:
            merged_arr[i] = arrB[i]
            merged_arr[i+1] = arrA[i]
            arrB.remove(arrB[i])
        i += 1
    print(merged_arr)
    #return merged_arr

merge([2,4], [1,5])


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # If arr is 0 or 1 in length, return arr.
    if len(arr) <= 1:
        return arr

    # Split arr into two equal arrays
    split_index = len(arr) // 2

    left = arr[split_index-1:]
    right = arr[:split_index+1]

    # Recurse through the new arrays
    return merge_sort(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
