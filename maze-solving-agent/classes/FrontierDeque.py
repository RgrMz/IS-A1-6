from collections import deque

class FrontierDeque():
    
    """
        Class Description:
            This class is used to manage the frontier. It is stored in a deque and there are methods to pop, push and to know if the structure is empty.
    """

    def __init__(self):

        self.dequeFrontier = deque()

    def pop(self):
        
        return self.dequeFrontier.popleft()

    def push(self, node):
        
        self.dequeFrontier.append(node)
        self.dequeFrontier = deque(sorted(self.dequeFrontier))
    
    def isEmpty(self):
        
        return len(self.dequeFrontier) == 0
