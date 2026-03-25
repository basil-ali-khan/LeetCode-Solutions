class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        right_prod = 1
        left_products = []
        right_products = []

        i = 0

        while i < len(nums):
            
            left_products.append(left_prod)
            left_prod = left_prod * nums[i]
            i += 1
            # print(left_products)

        i -= 1

        while i >= 0:
            
            right_products.append(right_prod)
            right_prod = right_prod * nums[i]
            i -= 1
            # print(right_products)
        right_products.reverse()
        # print(right_products)

        final = []

        for i in range(len(nums)):
            final.append(left_products[i] * right_products[i])

        return final
        