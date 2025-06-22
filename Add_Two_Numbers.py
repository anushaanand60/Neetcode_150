class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1+val2+carry
            digit = total%10
            carry = total//10

            current.next = ListNode(digit)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next

def build_ll(lst):
    head = ListNode()
    current = head
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return head.next

def print_ll(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

if __name__ == "__main__":
    l1_input = input("Enter list 1: ")
    l1_list = list(map(int, l1_input.strip().split()))
    l1 = build_ll(l1_list)

    l2_input = input("Enter list 2: ")
    l2_list = list(map(int, l2_input.strip().split()))
    l2 = build_ll(l2_list)

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Result linked list:")
    print_ll(result)

        