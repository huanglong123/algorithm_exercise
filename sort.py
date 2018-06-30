# -*- coding: utf-8 -*-

"""
选择排序 时间复杂度O(n^2)
首先在未排序序列中找到最小元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""
def FindSmallest(arr):
    print("排序的列表 %s" %arr)
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

print(FindSmallest([1,3,5,2]))

def selectionSore(arr):
    newarr = []
    for i in range(len(arr)):
    #关键点:arr重建,删掉上次得出的,在运行下次取新的arr里面最小的
        newarr.append(arr.pop(FindSmallest(arr)))

    print(newarr)

selectionSore([1,3,5,2,4])

## 另一种选择排序的写法，上面的是新建列表，这个是交换元素位置
def swap(lyst,i,j):
    temp = lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp

def selectsort(lyst):
    i=0
    while i<len(lyst)-1:
        minindex = i
        j = i+1
        while j<len(lyst):
            if lyst[j]<lyst[minindex]:
                minindex = j
            j+=1
        if minindex != i:
            swap(lyst,i,minindex)
        i+=1
    print(lyst)

selectsort([1,3,5,2,4])

"""
冒泡排序 时间复杂度O(n^2)
1，比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2，对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3，针对所有的元素重复以上的步骤，除了最后一个。
4，持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def bubble_sorted(iterable):
    new_list = list(iterable)
    list_len = len(new_list)
    for i in range(list_len - 1):
        for j in range(list_len - 1, i, -1):
            if new_list[j] < new_list[j - 1]:
                new_list[j], new_list[j - 1] = new_list[j - 1], new_list[j]
    return new_list

testlist = [27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
print('sorted:', bubble_sorted(testlist))