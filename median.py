def find_median(list_nums):
    if len(list_nums) % 2 == 0:
        med1 = (len(list_nums)) // 2
        med2 = med1 - 1
        return (list_nums[med1] + list_nums[med2]) / 2

    else:
        med = (len(list_nums)) // 2
        return list_nums[med]


print(find_median([0, -1, 1, 1]))
