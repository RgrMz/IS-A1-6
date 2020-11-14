from collections import deque

class FrontierDeque():
    
    def __init__(self):
        
        self.dequeFrontier = deque()

    def pop(self):
        
        return self.dequeFrontier.popleft()

    def push(self, node):
        
        self.dequeFrontier.append(node)
        self.dequeFrontier = deque(sorted(self.dequeFrontier))
    
    def isEmpty(self):
        
        return len(self.dequeFrontier) == 0
