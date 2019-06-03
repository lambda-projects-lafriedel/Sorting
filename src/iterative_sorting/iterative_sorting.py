# TO-DO: Complete the selection_sort() function below 
#def selection_sort(arr):
    # loop through n-1 elements
    #for i in range(0, len(arr) - 1):
     #   cur_index = i
      #  smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    #return arr


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

bubble_sort([29,10,14,37,14])
# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

    # return arr