class MinStack(object):
    def __init__(self):
        self.stack=[]
        

    def push(self, value):
        if not self.stack:
            current_min=value
        else:
            current_min=min(value,self.stack[-1][1])
        self.stack.append((value,current_min))

        """
        :type value: int
        :rtype: None
        """
        

    def pop(self):
        if not self.stack:
            return None
        else:
            self.stack.pop()

        """
        :rtype: None
        """
        

    def top(self):
        return self.stack[-1][0]
        """
        :rtype: int
        """
        

    def getMin(self):
        return self.stack[-1][1]
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()