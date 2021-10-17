from typing import List

# Returns the index of the value, if found
def searchIterative (value, orderedArray : List):

    # Time complexity: 
    # Each iteration of the while loop, half the original dataset is eliminated => O(log n) :D
    # Compare that to just iterating through the entire array one index at a time until the desired value is found => O(n) :(

    left = int(0)
    right = int(len(orderedArray) - 1)

    while left <= right:
        # There are several ways to find a midpoint. Each seems to have its own issues, but this one is pretty good and probably worth remembering:
        # middleIndex = left + (right - left) // 2
        
        # Can also try this snazzy right-shift version, since we can do that in Python, and it's super efficient:
        middleIndex = (right + left) >> 1

        if orderedArray[middleIndex] == value:
            return middleIndex

        elif orderedArray[middleIndex] < value:
            left = middleIndex + 1
            # +1 b/c the middle index has already been eliminated
        
        else:
            right = middleIndex - 1
            # -1 b/c the middle index has already been eliminated
    
    return -1 #No match found


def main():
    orderedArray = [1, 3, 5, 6, 7, 10, 11, 13, 15, 16, 17, 19, 21, 22, 23, 24, 29, 
                                   30, 31, 38, 42, 43, 49, 50, 51, 52, 53, 56, 59, 60]
    print(searchIterative(16, orderedArray))


if __name__ == '__main__':
    main()



