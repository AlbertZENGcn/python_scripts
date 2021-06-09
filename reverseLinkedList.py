class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next=None
        curr=head
        prev=None
        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

    def quick_sort(lists, i, j):
        if i >= j: return lists
        left = i
        rigjt = j
        pivot = lists[i]
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            lists[i] = lists[j]
            while i < j and lists[i] <= pivot:
                i += 1
            lists[j] = lists[i]

        lists[i] = pivot
        quick_sort(lists, left, i - 1)
        quick_sort(lists, i + 1, rigjt)
        return lists