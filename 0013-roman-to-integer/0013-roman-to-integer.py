class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        print(d)

        i = 0
        n = len(s)
        total = 0

        while i < (n - 2):
            
            if s[i:i+2] in d.keys():
                print("current char(s):", s[i:i+2])
                total += d[s[i:i+2]]
                i += 2
            else:
                print("current char(s):", s[i])
                total += d[s[i]]
                i += 1

        if s[i:i+2] in d.keys():
            total += d[s[i:i+2]]
        else:
            total += d[s[i]] + d[s[i+1]]
        print(total)

        return total
        