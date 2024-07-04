
class Solution(object):
    def mergeNodes(self, head):
        modify = head.next  
        next_sum = modify

        while next_sum:
            total = 0
            while next_sum.val != 0:
                total += next_sum.val
                next_sum = next_sum.next

            modify.val = total
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next

        return head.next  
        