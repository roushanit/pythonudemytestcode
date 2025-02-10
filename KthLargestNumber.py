import heapq

def kth_largest(ele, k):
    
    sorted_list = []

    for e in ele:
        heapq.heappush(sorted_list, -e)

    for i in range(k-1):
        heapq.heappop(sorted_list)

    return -heapq.heappop(sorted_list)

element = [10,24,71,19,101,96]
print('kth Largest element is', kth_largest(element,6))