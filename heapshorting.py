import heapq

def heap_sort(elements):
    heapq.heapify(elements)
    sorted_list = []

    for i in range(len(elements)):
        x = heapq.heappop(elements)
        sorted_list.append(x)


    return sorted_list
    

elements = [20, 12, 32, -6, -7, 2, 0, 4]
sorted_list = heap_sort(elements)

print('Sorted List is:', sorted_list)