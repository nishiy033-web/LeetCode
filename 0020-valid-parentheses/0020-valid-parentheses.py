class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={')':'(','}':'{',']':'['}
        for i in s:
            if i in '({[':
                stack.append(i)
            elif i in pairs:
                if not stack or stack.pop() !=pairs[i]:
                    return False
            else:
                return False
        return not stack

        """
        :type s: str
        :rtype: bool
        """
        