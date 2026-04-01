# class Solution:
#     def trap(self, height: List[int]) -> int:
#         left_max, right_max = [], []
#         # print(left_max, right_max)

#         n = len(height)
#         i = 0
#         left_tallest = 0
#         right_tallest = 0

#         while i < n:
#             left_tallest = max(height[i], left_tallest)
#             left_max.append(left_tallest)

#             i += 1

#         print(left_max)
#         i -= 1
#         while i >= 0:
#             right_tallest = max(height[i], right_tallest)
#             right_max.append(right_tallest)

#             i -= 1

#         right_max.reverse()
#         print(right_max)
#         lst = []
#         for i in range(n):
#             trapped_water = min(left_max[i], right_max[i]) - height[i]
#             print(trapped_water)
#             lst.append(trapped_water)

#         print(lst)
#         return sum(lst)

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        # 1. Setup our two pointers at the far edges
        l = 0
        r = len(height) - 1
        
        # 2. Track the tallest walls seen so far from both sides
        left_max = height[l]
        right_max = height[r]
        
        total_water = 0
        
        # 3. Walk the pointers inward until they meet
        while l < r:
            # If the left wall is the bottleneck, process the left side
            if left_max < right_max:
                l += 1 # Step inward first
                # Update the tallest left wall seen so far
                left_max = max(left_max, height[l]) 
                # Calculate trapped water (Surface level - ground level)
                total_water += left_max - height[l]
                
            # If the right wall is the bottleneck (or they are equal), process the right side
            else:
                r -= 1 # Step inward first
                # Update the tallest right wall seen so far
                right_max = max(right_max, height[r]) 
                # Calculate trapped water (Surface level - ground level)
                total_water += right_max - height[r]
                
        return total_water