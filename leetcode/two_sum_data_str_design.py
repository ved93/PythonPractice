from collections import defaultdict


class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.lookup[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
obj = TwoSum()
# number = int(input())
# print(number)
# obj.add(number)
# param_2 = obj.find(value)

for i in (1, 3, 5):
    obj.add(i)

for i in (4, 7):
    print(obj.find(i))
