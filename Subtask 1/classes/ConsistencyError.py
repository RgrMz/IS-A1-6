class ConsistencyError(Exception):
    
    def __init__(self, message, filename,cell_position):
        self.message = message
        self.filename = filename
        self.cell_position = cell_position