def solution(n):
    n = str(n)
    n1 = n[:len(n)//2]
    n2 = n[len(n)//2:]
    total = 0
    total2 = 0 

    for i in n1:
        total = total + int(i)
    for j in n2:
            total2  = total2 + int(j)  
    if total == total2:
        return True 
    else:
        return False 

print(solution(156915))