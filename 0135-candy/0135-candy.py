class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        dp_arr = [1] * n
        
        # Left-to-right pass
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                dp_arr[i] = dp_arr[i-1] + 1
                
        # Right-to-left pass
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j+1]:
                # We need one more candy than the RIGHT neighbor (dp_arr[j+1] + 1)
                # We use max() so we don't accidentally take away candies they earned from the left pass!
                dp_arr[j] = max(dp_arr[j], dp_arr[j+1] + 1)
                
        return sum(dp_arr)