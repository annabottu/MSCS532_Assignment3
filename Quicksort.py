import random

# This function is implementing the randomized quicksort algorithm
def random_quicksort(array):
    # Check if the array is empty or has one element
    if array is None or len(array) <= 1:
        # If the array is empty or has one element, it is already sorted
        return array  

    # Recursive function to perform quicksort
    # using a randomized partitioning scheme
    def quicksort_recursive(low, high):
        # if the low index is less than the high index then continue sorting
        if low < high:
            # Call the random_quicksort function to get the pivot index
            # and partition the array around the pivot
            # The pivot index is the index where the pivot element is placed
            # after partitioning, and it is used to recursively sort the subarrays
            pivot_index = random_quicksort(low, high)
            quicksort_recursive(low, pivot_index - 1)
            quicksort_recursive(pivot_index + 1, high)

    # Randomized partitioning function
    # This function selects a random pivot and partitions the array
    def random_quicksort(low, high):
        # Select a random pivot index and swap it with the last element
        if low >= high:
            return low
        pivotIndex = random.randint(low, high)
        # Swap the pivot with the last element
        array[pivotIndex], array[high] = array[high], array[pivotIndex]

        # Partitioning the array around the pivot
        pivot = array[high]
        i = low - 1
        # Move elements smaller than or equal to the pivot to the left
        # and elements greater than the pivot to the right
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # Puts the pivot in the right position
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    # Call the recursive quicksort function
    quicksort_recursive(0, len(array) - 1)
    return array 
