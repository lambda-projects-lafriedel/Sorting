# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through all indicies in array
    for i in range(1, len(arr)):
        # Create variables for indicies being compared
        a = arr[i-1]
        b = arr[i]
        # If left index is greater than right index, swap places
        if a > b:
            a = arr[i]
            b = arr[i-1]
        else:
            pass

    return arr


# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

    # return arr