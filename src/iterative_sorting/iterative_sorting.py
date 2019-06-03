# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # Store the current index. But why?
        cur_index = i
        print("cur_index:", cur_index, "\n")

        # Assign the smallest index as the current index
        smallest_index = cur_index
        print("smallest_index before for:", smallest_index, "\n")

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Loop through all indices in list after index 0 and compare them to the smallest_index
        for j in range(1, len(arr)):
            print("arr[j]:", arr[j], "\n")
            
            # If arr[1] < arr[0] (if 10 < 29 [TRUE], update smallest_index with the index that equals j. After looping through all the indices, swap arr[smallest_index] with )
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            arr[cur_index] = arr[smallest_index]
            arr[j] = arr[i]
        print(arr, "\n")

    return arr

selection_sort([29,10,14,37,13])




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