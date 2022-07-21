class Solution:
    def isValid(self, s: str) -> bool: 
        match = {"}":"{","]":"[",")":"("}
        list1 = []
        if len(s) % 2 != 0:
            return False

        for i, letter in enumerate(s):
            if letter in match.keys() and len(list1) > 0:
                a= list1.pop()
                if match.get(letter) != a:
                    return False
            elif letter in match.values():
                list1.append(letter) 
            else:
                return False

        return len(list1) == 0