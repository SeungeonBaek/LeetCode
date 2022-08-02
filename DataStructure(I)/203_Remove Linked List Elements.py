# Definition for singly-linked list.
'''
Remove Linked List Elements / Easy

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None 
        
        def helper(node):
            if not node: return 
            
            next_node = node.next
            while next_node and next_node.val == val:
                next_node = next_node.next 
            node.next = next_node
                        
            helper(node.next) 
            
        helper(head) 
        
        node = head
        
        while node and node.val == val:
            node = node.next 

        return node