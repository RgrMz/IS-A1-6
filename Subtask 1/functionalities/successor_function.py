def successor_function (state):
    
    successors = []
    if state.take_neighbours()[0]:
        successors.append(('N',(state.neighbours[0]),1))
    if state.take_neighbours()[1]:
        successors.append(('E',(state.neighbours[1]),1))
    if state.take_neighbours()[2]:
        successors.append(('S',(state.neighbours[2]),1))
    if state.take_neighbours()[3]:
        successors.append(('O',(state.neighbours[3]),1))

    return successors
# Crear toString maybe