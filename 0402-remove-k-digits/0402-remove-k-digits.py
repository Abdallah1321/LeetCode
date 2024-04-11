class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for i in num: 
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
        while k > 0:
            stack.pop()
            k-=1

        return "".join(stack).lstrip("0") or "0"