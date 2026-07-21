class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for x in operations:
            if x == 'C':
                stack.pop()
            elif x == 'D':
                stack.append(stack[-1] * 2)
            elif x == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(x))
        total = 0
        for i in stack:
            total += i

        return total