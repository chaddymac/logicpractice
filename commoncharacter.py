def commonCharacterCount(s1, s2):
    #TODO: find the number of common characters
    s3 = []
    if len(s1) > len(s2):
        for i in s2:
            if i in s1:
                s3.append(i)
                s1 = s1.replace(i,"",1)

    else:
        for i in s1:
            if i in s2:
                s3.append(i)
                s2 = s2.replace(i,"",1)
    return len(s3)
list1 = "aabcc"
list2 = "adcaa"
print(commonCharacterCount(list1,list2))