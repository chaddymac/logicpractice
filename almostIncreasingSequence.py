def checkIncreasing(sequence):
    return sequence == sorted(sequence)


def almostIncreasingSequence(sequence):
    result = False
    new_seq = sequence.copy()
    # max_ele = 0

    # for i in range(len(sequence)):
    #     cur_ele = sequence[i]
    #     next_ele = sequence[i+1]
    #     if cur_ele >= next_ele:
    #         # Try removing first ele and checking if that fixes
    #         new_seq1 = sequence.copy()
    #         new_seq1.pop(i)
    #         res1 = new_seq1 == sorted(new_seq1)
    #         # Try removing second ele and see ifo that fixes
    #         new_seq2 = sequence.copy()
    #         new_seq2.pop(i+1)
    #         res2 = new_seq2 == sorted(new_seq2)
    #         # If one of those worked
    #         if res1 

            


    for i in range(len(sequence)-1):
        cur_ele = sequence[i]
        next_ele = sequence[i+1]
        # 1st mistake, remove it form the other lsit
        if cur_ele >= next_ele:
            sequence.pop(i+1)
            break
    
    for i in range(len(new_seq)-1):
        cur_ele = new_seq[i]
        next_ele = new_seq[i+1]
        # 1st mistake, remove it form the other lsit
        if cur_ele >= next_ele:
            new_seq.pop(i)
            break

    if sequence == sorted(list(set(sequence))) or new_seq == sorted(list(set(new_seq))):
        result = True
        
    # for i in range(len(new_seq)):
    #     cur_ele = new_seq[i]
    #     next_ele = new_seq[i+1]
    #     # 2nd mistake set result to false
    #     if cur_ele >= next_ele:
    #         result = False
            
    return result

    
# test = [1,2,3,4,5] # True
# test = [1,3,2,5]   # True, can remove 2
# test = [2,1,6,5]   # False
test = [1, 2, 5, 3, 5]
test = [1, 2, 1, 2]  # False
test = [1,3,2]
test = [123, -17, -5, 1, 2, 3, 12, 43, 45]
almostIncreasingSequence(test)