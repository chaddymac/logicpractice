import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reversed_s = s[::-1]
        return s == reversed_s

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
