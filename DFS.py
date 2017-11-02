stack[0]
vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0), (1,3), (2,0),
            (2,4), (2,5),(3,1), (4,2), (4,6), (5,2), (6,4)]
adjacencyList = [[] for vertex in vertexList]

for edge in edgeList:
    adjacencyList[edge[0].append(edge[1])]
    
while stack:
    current = stack.pop()
    for neighbor in adjacencyList[current]:
        if not neighbor in visitedVertex:
            stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex
            

##def DFSBinary(root, fcn):
##    stack =[root]
##    while len(stack)>0:
##        if fcn(stack[0]):
##            return True
##        else:
##            temp = stack.pop(0)
##            if temp.getRightBinary():
##                stack.insert(0, temp.getRightBranch())
##            if temp.getLeftBinary():
##                stack.insert(0, temp.getLeftBranch())
##        return False
##DFSBinary(5, find6)
