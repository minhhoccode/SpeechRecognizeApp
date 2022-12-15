
import time
import sys
start_time = time.time()
INT_MAX = sys.maxsize
NO_PARENT = -1


def getPath(currentVertex: int, parents: list)->str:
    if currentVertex == NO_PARENT:
        return ""
    return getPath(parents[currentVertex], parents) + str(currentVertex) + " "

def getSolution(startVertex: int, endVertex: int, distances: list, parents: list)-> str:
    nVertices = len(distances)
    solution = ""
    solution += getPath(endVertex, parents)
    return solution

def dijkstra(adjacencyMatrix: list, startVertex: int, endVertex: int):
    nVertices = len(adjacencyMatrix[0])
    shortestDistances = [INT_MAX] * nVertices
    added = [False] * nVertices
    shortestDistances[startVertex] = 0
    parents = [NO_PARENT] * nVertices
    for i in range(1, nVertices):
        nearestVertex = -1
        shortestDistance = INT_MAX
        for vertexIndex in range(nVertices):
            if not added[vertexIndex] and shortestDistances[vertexIndex] is not None and shortestDistances[vertexIndex] < shortestDistance:
                nearestVertex = vertexIndex
                shortestDistance = shortestDistances[vertexIndex]
        added[nearestVertex] = True
        for vertexIndex in range(nVertices):
            vertexDistance = adjacencyMatrix[nearestVertex][vertexIndex]
            if vertexDistance > 0 and ((shortestDistance + vertexDistance) < shortestDistances[vertexIndex] or shortestDistances[vertexIndex] is None):
                shortestDistances[vertexIndex] = shortestDistance + \
                    vertexDistance
                parents[vertexIndex] = nearestVertex
    return getSolution(startVertex, endVertex, shortestDistances, parents)

def ReturnPath(first: int, second: int, language: str):
    with open('matrix.txt', 'r') as f:
        adjacencyMatrix = [[int(num) for num in line.split(' ')] for line in f]
    try :
        path = dijkstra(adjacencyMatrix, first, second)
    except:
        if language=="vi-VN":
            path = "Không có đường đi"
        else:
            path = "There is no path"
    # Trả về kết quả là 1 xâu 
    return path