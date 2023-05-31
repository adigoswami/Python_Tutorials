#There are couple of ways to initialize lists.

# Method 1: sqaure brackets
lis = [5,6,8,9]
print(lis)

# Method 2: List() function to create an empty list only
arr = list()
print(arr)

# Method 3: List comprehension 
seq = [i for i in range(5)]
print(seq)

# Method 4: Using * operator this is the fastest method but creates shallow lists for 2D arrays
seque = [0]*6
print(seque)

#Therefore list comprehension is the better method to initialize the lists in python
# We will further look at some more examples to understand list comprehension 