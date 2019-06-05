# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # These 2 lines are creating a new list that has the length of 'elements' and is being instantiated with 0s as placeholders
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # Need to keep track of indices! This is what I was missing.
    arrA_index = 0
    arrB_index = 0

    # Loop through merged_arr's indices and compare the values of arrA and arrB.
    for i in range(0, elements):
        # If the stored index equals the length of the arr (meaning all values have been added to the sorted list), set merged_arr[i] as the last value in the opposite arr.
        if arrA_index == len(arrA):
            merged_arr[i] = arrB[arrB_index]
        elif arrB_index == len(arrB):
            merged_arr[i] = arrA[arrA_index]
        # If index of arrA is smaller than index of arrB, set that arrA's index to merged_arr[i]. Else, set arrB's index to merged_arr[i]
        elif arrA[arrA_index] < arrB[arrB_index]:
            merged_arr[i] = arrA[arrA_index]
            arrA_index += 1
        else:
            merged_arr[i] = arrB[arrB_index]
            arrB_index += 1
        
    # print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # If arr is 0 or 1 in length, return arr.
    if len(arr) <= 1:
        return arr

    # Split arr into two equal arrays
    split_index = len(arr) // 2
    # split_index == 3 when len == 6

    left = arr[:split_index]
    right = arr[split_index:]

    # Recurse through the new arrays
    merge_sort(left)
    merge_sort(right)

    return arr

    



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
