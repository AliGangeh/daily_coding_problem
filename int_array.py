# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array except
# the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
# [2, 3, 6].
#
# Follow-up: what if you can't use division?

# with division
def int_array (array):
    p = 1
    f_array = []
    for i in array:
        p *= i
    for i in array:
        f_array.append(int(p/i))
    print(f_array)
    return f_array

int_array([7,2,3,4,5])

# without division
def int_array (array):
    f_array = []
    for i in array:
        product = 1
        f_list = array[i:len(array)]+array[:i-1]
        for j in f_list:
            product *= j
        f_array.append(product)
    print(f_array)
    return f_array

int_array([1,2,3,4,5])
