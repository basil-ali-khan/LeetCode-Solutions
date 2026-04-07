import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        print(s)
        s.reverse()
        print(s)
        return " ".join(s)
        
        