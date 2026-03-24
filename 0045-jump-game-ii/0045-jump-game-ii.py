class Solution:
    def jump(self, nums: list[int]) -> int:
        # If the array has only 1 element, we are already at the end!
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We loop up to the second-to-last element (len(nums) - 1)
        # because if we are already at the last element, we don't need to jump again.
        for i in range(len(nums) - 1):
            
            # Constantly update the farthest we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we reach the end of our current jump's range...
            if i == current_end:
                jumps += 1             # We are forced to make a jump
                current_end = farthest # Our new jump range extends to the farthest point we found
                
                # Optimization: If our new range reaches or passes the end, we can stop!
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps