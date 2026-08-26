class MinStack(object):

    def __init__(self):
        self.items = []
        self.min_stack = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """

        self.items.append(value)
        value = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if not self.items:
            raise IndexError("Cannot perform this operation")
        self.min_stack.pop()
        return self.items.pop()
        

    def top(self):
        """
        :rtype: int
        """
        
        if not self.items:
            raise IndexError("Cannot perform this operation")


        return self.items[-1]
        
    def getMin(self):
        """
        :rtype: int
        """

        if not self.items:
            raise IndexError("Cannot perform this operation")

        return self.min_stack[-1] 


