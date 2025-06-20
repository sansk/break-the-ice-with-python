from functools import reduce

num = int(input("Enter the Number to find the Factorial: "))

# Solution - 1
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i += 1
print(fact)

# Solution - 2
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print(fact)

# Solution - 3
factorial_num = lambda n: 1 if n == 0 else n * factorial_num(n - 1)
print(factorial_num(num))

# Solution - 4
red_fun = lambda acc, i: acc * i
fact = reduce(red_fun, range(1, num + 1), 1)
print(fact)

#=========================================================================================
# Complexity Analysis:
# --------------------
# Solution - 1, 2, 4
# Time complexity: O(n)
# Space complexity: O(1).
#
# Solution - 3
# Time complexity: O(n)
# Space complexity: O(n).
#==================================================================================================
