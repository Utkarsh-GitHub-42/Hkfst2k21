import time

def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list
    mid_point = list_length // 2
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])


    return merge(left_partition, right_partition)
def merge(left, right):

    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_merge_sort():
    alist = input('Enter the list of numbers: ').split()
    c=time.time()
    print(alist)
    sorted_list = merge_sort(alist)
    print(time.time()-c)
    print(sorted_list)


run_merge_sort()
