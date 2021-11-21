from typing import List

def quicksort(arr, len):
    quicksort_rec (arr, 0, len-1)

def quicksort_rec (arr : list, first, last):
    # first and last are used for recursion

    # Base Case (recursion stops here)
    if last <= first:
        return

    # Partitioning:
    pivot = arr[first]
    pos = last # As the array is iterated through, this represents the middle of the partition. After the array has been fully partitioned once, all elements to the right of pos are greater than the pivot, while all elements to the left of (and including) pos are smaller than the pivot.

    i = last
    while (i > first):
        # If the element is larger than the pivot, we move that element to the right by swapping it with pos, otherwise it's just left alone and pos stays where it is
        if arr[i] > pivot: 
            temp = arr[pos]
            arr[pos] = arr[i]
            arr[i] = temp
            pos -= 1
        i -= 1
    
    print(arr)

    # Place the pivot where pos ended up, so the partitioning is complete
    temp = arr[first]
    arr[first] = arr[pos]
    arr[pos] = temp



    # After this while loop has run once, the array will be partitioned around the pivot. At this point, each partition is sorted again using recursion until the base case case is encountered, at which point it will be fully sorted.

    quicksort_rec (arr, first, pos-1)
    quicksort_rec (arr, pos+1, last)


# Testing:

myArray = [9, 10, 11, 4, 15, 6, 3, 5, 21, 2, 3, 18]
print(str(myArray) + "\nSorting Started...\n")
quicksort(myArray, len(myArray))
print("\nSorting Completed:\n" + str(myArray))