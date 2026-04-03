class Solution:
    def intToRoman(self, num: int) -> str:
        # d = {
        #     1: "I",
        #     5: "V",
        #     10: "X",
        #     50: "L",
        #     100: "C",
        #     500: "D",
        #     1000: "M",
        # }
        d = {
            "M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
        }

        res = ""
        
        # Go through every bill in the register
        for symbol, val in d.items():
            # While the remaining number is big enough to use this bill
            while num >= val:
                res += symbol
                num -= val
                
        return res