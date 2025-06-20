n = int(input('Enter the Number: '))

# Solution - 1
# Using for loop and range()
res = dict()
for i in range(1, n + 1):
    res[i] = i * i
print(res)

# Complexity Analysis
# -------------------
# The given code snippet creates a dictionary `res` that maps integers from 1 to `n`
# to their squares.
#
# ** Time Complexity: **
# The time complexity of this code is O(n). This is because the loop iterates `n`
# times, and each iteration involves a constant-time operation: calculating the square
# of `i` and inserting it into the dictionary. Therefore, the overall time complexity
# is linear with respect to `n`.
#
# ** Space Complexity: **
# The space complexity of this code is also O(n). This is due to the storage of `n`
# key-value pairs in the dictionary `res`. Each integer from 1 to `n` is stored as
# a key, and its square is stored as the corresponding value.
# Thus, the space required grows linearly with `n`.
#
# In summary, both the time and space complexity of the code are O(n).
#============================================================================================

# Solution - 2
# Using dictionary Comprehension
print({i : i * i for i in range(1, n + 1)})

# Complexity Analysis
# -------------------
# The given code snippet creates a dictionary using a dictionary comprehension
# that maps each integer `i` from 1 to `n` (inclusive) to its square `i * i`.
#
# Time Complexity:
# The time complexity of this operation is O(n). This is because the comprehension
# iterates through each integer from 1 to `n`, performing a constant-time operation
# (multiplication and assignment) for each integer. Therefore, the total time taken
# grows linearly with the size of `n`.
#
# Space Complexity:
# The space complexity is also O(n). This is due to the fact that a new dictionary
# is created that contains `n` key-value pairs. Each pair consists of an integer
# and its square, which requires space proportional to the number of elements
# stored in the dictionary. Thus, the space required increases linearly with `n`.
#
# In summary, both the time and space complexity of the code are O(n).