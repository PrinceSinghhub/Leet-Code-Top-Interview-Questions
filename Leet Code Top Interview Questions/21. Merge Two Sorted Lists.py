class Solution:
    def mergeTwoLists(self, l1, l2):
        ans = second = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                second.next = l1
                l1 = l1.next
            else:
                second.next = l2
                l2 = l2.next
            second = second.next
        second.next = l1 or l2
        return ans.next
