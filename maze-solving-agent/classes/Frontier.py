import heapq

class Frontier():
    
    """
        Class Description:
            This class is used to manage the frontier. It is stored in a heapq and there are methods 
            to pop, push and to know if the structure is empty.
    """
    
    def __init__(self):

        self.heap = []

    def pop(self):
        
        return heapq.heappop(self.heap)
    
    def push(self, node):
        
        heapq.heappush(self.heap, node)

    def isEmpty(self):
        return len(self.heap) == 0
