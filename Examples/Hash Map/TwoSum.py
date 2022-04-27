"""
Question: 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from collections import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    hash = {} # Using a dictionary (ie. hash map) for O(1) lookups - much faster than a list implementation
     
    for i, val in enumerate(nums): # O(n)
        complement = target - val # Calculating a complement and checking the dictionary to see if it's already in there
        
        if complement in hash: # O(1) lookup
            return [i, hash[complement]]

        else:
            hash[val] = i # O(1) - Filling the complement dictionary. The key is the value in nums, value is the index at which it was encountered

""" 
Explanation:

The general idea is to iterate through the "nums" list, checking to see if the complement (target - val) exists elsewhere in the list. 

In order to speed things up and only require a single pass through the the "nums" list, every time a complement is calculated, the result and it's associated index is stored in a hash map containing key:value pairs of complements:indeces. 

During the first iteration, the hash map is filled with the first calculated complement and index pair. Thereafter, the hash map is checked to see if the currently calculated complement exists in the hash map. If it does, the index (stored in the hash map's value) associated with the calculated complement, as well as the current index are returned.

The above solution executes in O(n) time complexity. The input list need only be traversed once, and all dictionary operations performed occur in O(1) time complexity. This solution requires O(n) space complexity.

A less efficient solution would involve a for loop nested within a main for loop, essentially beginning at one index, then checking to see if every other item (in conjunction with the current value) meets the target value provided. While you could get lucky if the first and second indices contain the solution, this will generally require O(n^2) time complexity. The singular advantage to this method, is that it requires O(1) space complexity.
"""