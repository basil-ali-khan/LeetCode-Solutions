class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = [], []
        # print(left_max, right_max)

        n = len(height)
        i = 0
        left_tallest = 0
        right_tallest = 0

        while i < n:
            left_tallest = max(height[i], left_tallest)
            left_max.append(left_tallest)

            i += 1

        print(left_max)
        i -= 1
        while i >= 0:
            right_tallest = max(height[i], right_tallest)
            right_max.append(right_tallest)

            i -= 1

        right_max.reverse()
        print(right_max)
        lst = []
        for i in range(n):
            trapped_water = min(left_max[i], right_max[i]) - height[i]
            print(trapped_water)
            lst.append(trapped_water)

        print(lst)
        return sum(lst)