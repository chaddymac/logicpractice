def makeArrayConsecutive2(statues):
    maxList = max(statues)
    minList = min(statues)
    sortedStats = sorted(statues)
    listVars= list(range(minList,(maxList + 1)))
    finalnum = len(listVars) - len(sortedStats) 
    print(finalnum)
    return 



newlist = [2,4,6,7]

prod = makeArrayConsecutive2(newlist) 
