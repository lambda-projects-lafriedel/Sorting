# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # These 2 lines are creating a new list that has the length of 'elements' and is being instantiated with 0s as placeholders
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # Need to keep track of indices! This is what I was missing.
    arrA_index = 0
    arrB_index = 0

    # Loop through merged_arr's indices and compare the values of .
    for i in range(0, elements):

        # If index of arrA is smaller than index of arrB, set that arrA's index to merged_arr[i]. Else, set arrB's index to merged_arr[i]
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1
        
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
    merge_sort(merge(left, right))

    



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
