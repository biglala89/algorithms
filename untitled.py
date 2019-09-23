class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import operator as op
        operator_map = {'+':op.add, '-':op.sub}
        operands, operators = [], []
        for i in s:
            if i != ' ':
                if i == '(' or i in operator_map:
                    operators.append(i)
                    print operators
                elif i == ')':
                    while operators[-1] != '(':
                        elm = int(operands.pop())
                        tmp = operator_map[operators.pop()](int(operands.pop()), elm)
                        operands.append(tmp)
                        print operands
                    operators.pop()
                else:
                    operands.append(i)
                    print operands
        if operands and operators:
            elm = int(operands.pop())
            tmp = operator_map[operators.pop()](int(operands.pop()), elm)
            operands.append(tmp)
        return operands.pop()

test = "(1+(4+5+2)-3)+(6+8)"
s = Solution()
print s.calculate(test)
