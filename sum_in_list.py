# coding interview problem by Google

# given a list of num and a number k, return whether
# any two numbers from the list add up to k.

# for example given 10,15,3,7 and k of 17. return true since 10+7 is 17
# bonus can you do this in one pass?

def  sum_in_list (list, k):
    flag = False
    list.sort()
    p1 = 0
    p2 = len(list)-1
    for i in range (len(list)-1):
        sum = list[p1] + list[p2]
        if sum == k:
            flag = True
            break
        elif sum > k:
            p2 -= 1
        elif sum < k:
            p1 += 1
    return flag

sum_in_list([1,3,2,4,5,13], 7)
