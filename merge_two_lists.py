from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    real_list = []
    while (self != None):
      real_list.append(self.val)
      self = self.next
    return f"[{','.join(str(item) for item in real_list)}]"
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       # these if statements are for cases when either list is none or both lists = None  
      if list1 == None:
        return list2
      
      if list2 == None:
        return list1

      if list2 == None and list1 == None:
        return None

       # need the list with the smallest first to avoid an infinite loop. or else the function will get stuck as the numbers in the lists are not changing list1.next and list2.next stays the same
       # getting the list with the smaller first val since they're both sorted to make easier
      if list1 != None and list2 != None:
       if list1.val >list2.val:
        temp = list1
        list1 = list2
        list2 = temp
## while the bigger list's next item is not none loop through values.
# set final outside the while loop because it shouldn't be touched
       final = list1
       while list2 != None:
        if list1.next == None or list1.next.val >= list2.val:
          temp = list1.next
          temp2 = list2.next
          list1.next = list2
          list2 = temp2
          list1.next.next=temp
        else:
          list1 = list1.next
       return final

l1= ListNode(5,ListNode(7,ListNode(8)))
l2= ListNode(2,ListNode(4,ListNode(6)))
l3= None
l4 = ListNode(0) 
solution = Solution()
print(solution.mergeTwoLists(l3,l3))
