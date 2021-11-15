#creates a pivot where all numbers to the left are smaller and numbers to the right
#are larger, then the process is repeated for left and right subtrees
def quick_sort(sort_list, low, high):
    if low < high:
        pivot = partition(sort_list, low, high)
        quick_sort(sort_list, low, pivot - 1)
        quick_sort(sort_list, pivot + 1, high)

#list searches for and moves left all values less than pivot, with the pivot being placed after
#all smaller numbers when the loop is finished. Returns the pivot point
def partition(sort_list, low, high):
    i = low - 1
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= sort_list[high]:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i + 1], sort_list[high] = sort_list[high], sort_list[i + 1]
    return i + 1

#sample list with unsorted and sorted versions printed
sample = [8, 4, 3, -1, 7, 2, 0]

print(sample)
quick_sort(sample, 0, len(sample) - 1)
print(sample)
