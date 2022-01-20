# goal is to merge 2 given arrarys and make sure they're ordered.

def merge_sort(list1, list2):
    #check inputs
    if type(list1) and type(list2) == type([]):
        ret_statement = sorted(list1 + list2)
    else:
        ret_statement = "Please pass in two arrays"
    return print(ret_statement)


list1 = ["car", "bike", "gym", "soccer"]
list2 = ["green","red","blue","yellow"]
merge_sort(list1,list2)
    


