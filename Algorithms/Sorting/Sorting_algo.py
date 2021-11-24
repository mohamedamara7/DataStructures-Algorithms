def bubble_sort(list):
    n = len(list)
    for passnum in range(n - 1, 0, -1):
        exchaneges = False
        for j in range(passnum):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                exchaneges = True
        if not exchaneges:
            break


########################################################################################################################
def selection_sort(list):
    n = len(list)
    for i in range(n - 1):
        mn_idx = i
        for j in range(i + 1, n):
            if list[j] < list[mn_idx]:
                mn_idx = j
        list[i], list[mn_idx] = list[mn_idx], list[i]


########################################################################################################################
def merging(list, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list[k] = left[i]
            i = i + 1
        else:
            list[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        list[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        list[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        merging(list, left, right)


########################################################################################################################
def partitioning(list, first, last):
    pivot = list[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while rightmark >= leftmark and pivot >= list[leftmark]:
            leftmark = leftmark + 1
        while rightmark >= leftmark and pivot <= list[rightmark]:
            rightmark = rightmark - 1
        if leftmark > rightmark:
            done = True
        else:
            list[leftmark], list[rightmark] = list[rightmark], list[leftmark]
    list[first], list[rightmark] = list[rightmark], list[first]
    return rightmark


def quicksorthelper(list, first, last):
    if last > first:
        splitpoint = partitioning(list, first, last)
        quicksorthelper(list, first, splitpoint - 1)
        quicksorthelper(list, splitpoint + 1, last)


def quick_sort(list):
    quicksorthelper(list, 0, len(list) - 1)


def insertion_sort(list):
    for i in range(1, len(list)):
        currentvalue = list[i]
        j = i
        while j > 0 and currentvalue < list[j - 1]:
            list[j] = list[j - 1]
            j = j - 1
        list[j] = currentvalue
