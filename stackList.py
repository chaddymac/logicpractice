from collections import deque

# example of a stack created from a list O(n) complexity using deque
def removeOneItem(stack):
    final_stack =list(stack)
    final_stack.pop()
    final_stack.append("Steve")
    print(final_stack)
    final_stack.pop()
    return final_stack

def dequeStack(stack):
    stack = deque(stack)
    stack.pop()
    return stack 

list1 = ["Chad","Lam","Dax"]
print(removeOneItem(list1))
print(dequeStack(list1))