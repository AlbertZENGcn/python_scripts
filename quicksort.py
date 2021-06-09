def quick_sort(lists, i, j):
    if i>=j:return lists
    left=i
    right=j
    pivot=lists[i]
    while i<j:
        while i<j and lists[j]>=pivot:
            j-=1
        lists[i]=lists[j]
        while i<j and lists[i]<=pivot:
            i+=1
        lists[j]=lists[i]
    lists[i]=pivot
    quick_sort(lists,left,i-1)
    quick_sort(lists,i+1,right)
    return lists


if __name__ == "__main__":
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：")
    for i in lists:
        print(i, end=" ")
    print("\n排序后的序列为：")
    for i in quick_sort(lists, 0, len(lists) - 1):
        print(i, end=" ")
