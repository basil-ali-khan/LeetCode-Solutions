class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            # print(strs[0][i])
            cur = strs[0][i]

            for j in range(1, len(strs)):
                print("j", j, "i", i)
                if i == len(strs[j]) or strs[j][i] != cur:
                    return prefix

            prefix += cur

        return prefix
        