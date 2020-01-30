# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        (carry, num) = divmod(l1.val + l2.val, 10)
        headNode = ListNode(num)
        adder = headNode
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            num = l1.val + l2.val + carry
            (carry, sum) = divmod(num, 10)
            node = ListNode(sum)
            adder.next = node
            adder = adder.next
            l1 = l1.next
            l2 = l2.next
        else:
            if l1:
                adder.next = l1
            else:
                adder.next = l2
            while adder.next and carry != 0:
                (carry, sum) = divmod(adder.next.val + carry, 10)
                adder.next.val = sum
                adder = adder.next
        if carry != 0:
            adder.next = ListNode(carry)
        return headNode

            
