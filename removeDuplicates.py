# thought I could change nums to set but pass by ref vs pass by value 
#       def removeDuplicates(self, nums):
#         nums=list(set(nums))
#         nums = len(nums)
#         return nums


def removeDuplicates(nums):
    set_nums = list(set(nums))
    holder_nums = nums.copy()
    for i in holder_nums:
        if nums != set_nums:
            if nums.count(i) > 1:
                nums.remove(i)
    return len(nums)

list1 = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(list1))