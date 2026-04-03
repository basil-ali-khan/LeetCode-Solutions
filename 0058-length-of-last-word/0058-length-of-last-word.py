class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words = s.strip().split(" ")
        print(words[-1])

        return len(words[-1])
        