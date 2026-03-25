import random

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.d = {}
        # Notice we dropped self.top entirely! 
        # The length of the list handles the index tracking for us.

    def insert(self, val: int) -> bool:
        # Check if the value is already in the dictionary
        if val in self.d:
            return False
            
        # Append the new value to the end of the list
        self.lst.append(val)
        
        # Record its index in the dictionary
        # The index of a newly appended item is always len(list) - 1
        self.d[val] = len(self.lst) - 1
        
        return True

    def remove(self, val: int) -> bool:
        # Check if the value actually exists
        if val not in self.d:
            return False
        
        # Step 1: Find the exact index of the item we want to remove
        idx_to_remove = self.d[val]
        
        # Step 2: Find the actual value of the very last item in the list
        last_val = self.lst[-1]
        
        # Step 3: Overwrite the target item with the last item
        self.lst[idx_to_remove] = last_val
        
        # Step 4: Update the dictionary so the last item knows its new index
        self.d[last_val] = idx_to_remove
        
        # Step 5: Pop the last item off the list (O(1)) and delete the target from the dictionary (O(1))
        self.lst.pop()
        del self.d[val] # 'del' is the standard O(1) way to remove a key from a dict
        
        return True

    def getRandom(self) -> int:
        # random.choice is O(1) because it randomly picks a valid index instantly
        return random.choice(self.lst)