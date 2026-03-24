class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        # print(citations)

        h = 0

        for i in citations:
            if i > h:
                h += 1

            else:
                break

        return h