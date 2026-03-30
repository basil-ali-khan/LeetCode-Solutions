from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_tank += diff
            current_tank += diff

            # If we can't reach station i+1 from current start
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        # If total gas is enough, return start
        if total_tank >= 0:
            return start_index
        else:
            return -1