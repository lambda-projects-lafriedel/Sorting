# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    for i in range(0, len(arr) - 1):

        cur_index = i
        smallest_index = cur_index

        for j in range(cur_index+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Store length of array to know how many times to iterate
    iterations = len(arr) - 1

    # Loop through array as long as iterations is 1 or more
    while iterations > 0:

        # Loop through all indicies in array
        for i in range(1, len(arr)):
            left = arr[i-1]
            right = arr[i]

            # If left index is greater than right index, swap places
            if arr[i-1] > arr[i]:

                arr[i-1] = right
                arr[i] = left

        # Decrease iterations by 1
        iterations -= 1

    return arr

    # *********TO-DO: Need to jump out of loop after array is already sorted. No need to keep going if it's already in its final state.

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

    # return arr