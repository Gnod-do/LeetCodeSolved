import random


class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False

        self.pos[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.pos[last] = idx
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()