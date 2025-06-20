# Solution-1
# Using the classic for loop and range()
def normal_solution(start, end):
    for i in range(start, end + 1):
        if i % 7 == 0 and not i % 5 == 0:
            print(i, end=",")

normal_solution(2000, 3200)

# Solution-2
# Using List Comprehension and Unpacking List in print using *()
def comprehension_solution(start, end):
    print(*(i for i in range(start, end + 1) if i % 7 == 0 and not i % 5 == 0), sep = ',')

comprehension_solution(2000, 3200)
#=========================================================================================
# Complexity Analysis: (For both solutions, same Time & Space)
# --------------------
# Time complexity: O(n)
# Space complexity: O(1).
#
# The given code iterates through a range of integers from 2000 to 3200 (inclusive) and
# checks for two conditions: whether the number is divisible by 7 and not divisible by 5.
#
# ** Time Complexity: **
# The time complexity of this code can be analyzed based on the loop and the operations within it.
# The loop runs for a total of 3201 - 2000 = 1201 iterations.
# For each iteration, it performs a constant amount of work: two modulus operations and
# a conditional check. Therefore, the overall time complexity is O(n), where n is
# the number of integers in the range, which is 1201 in this case.
# Thus, we can say the time complexity is O(1) in terms of the specific range,
# but generally, it is O(n) for any range of size n.
#
# ** Space Complexity: **
# The space complexity of the code is O(1) because it uses a fixed amount of space
# regardless of the input size. The only variables used are the loop index `i` and the
# output, which is printed directly to the console. There are no data structures that
# grow with the input size, so the space complexity remains constant.
#==================================================================================================
