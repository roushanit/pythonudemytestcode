import bisect

def insertion_sort(ele):
    sorted_list = []
    for e in ele:
        bisect.insort(sorted_list,e)

    return sorted_list


ele = [2,34,57,10,-2,0,37,58]
s_list = insertion_sort(ele)
print('Sorted list is:', s_list)


