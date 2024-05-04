class Solution(object):
    def singleNumber(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        # At this point, the set should contain only the unique number
        return seen.pop()

        