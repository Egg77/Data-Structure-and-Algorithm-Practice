"""
Question:

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def isAnagram(s: str, t: str) -> bool:

    hash = {}

    for c in s: # Filling hash with s: O(n)
        if c in hash:
            hash[c] += 1 
        else:
            hash[c] = 1
    
    print(hash)

    for c in t: # Emptying hash againbased on t: O(n)
        if c in hash:
            hash[c] -=1
        else:
            return False
    
    for val in hash.values(): # Checking to make sure none of the are anything but 0: O(n)
        if val != 0:
            return False
    
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

"""
Explanation:

This hash implementation is among the fastest solutions to this problem. Basically, the first of the input strings fills is filled into a dictionary - this is done primarily so any subsequent searches of the dictionary proceed at O(1) speed. The total time complexity is O(n).

As the dictionary is filled, the character "c" is used as the key, while a value of 1 is assigned as the value. If a given character appears more than once, that original value of 1 is incremented. So, in the case of the word "anagram", you'd have the following key:value pairs by the end of the first loop: 
    'a':3 
    'n':1 
    'g':1 
    'r':1 
    'm':1

The second loop is responsible for basically iterating over the other input string, comparing each character, and decrementing the associated key:value pairs from the dictionary whenever a character is encountered.

To speed things along, if a character is encountered in the second string that doesn't exist in the first, False is immediately returned, since we already know the anagram isn't valid at this point. Should that second loop finish executing, the final loop checks to see that each key in the dictionary has an associated value of zero.

There's also a far sneakier, faster, and Python-ier way to do this:

def isAnagram(self, s: str, t: str) -> bool:

    return Counter(s) == Counter(t)

Yep, that's it. Python has a Counter function which counts all the occurrences of elements in whatever it's fed. So in this case, if we make two counters and feed them each of the strings, a valid anagram will have the same counts for each character, and an invalid one won't. This operation and the associated comparison apparently happens bonkers fast. While this isn't a hash map solution, I've included it here because this is super powerful and likely something I'll want to use frequently.

"""


