class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        li1 = list(map(int, num1))
        li2 = list(map(int, num2))

        carry = 0
        res = []

        while li1 or li2:
            a = li1.pop() if li1 else 0
            b = li2.pop() if li2 else 0

            s = a + b + carry
            res.append(str(s % 10))
            carry = s // 10

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])
