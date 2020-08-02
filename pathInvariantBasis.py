import copy

#Computes and returns path-invariant basis. A path is represented by a list of vertices with the source as the first element of that list
#A path pair is represented by a list containing 2 paths
#Input: A list of vertices from 0 to n - 1, as well as their corresponding adjacency lists. Adjacency lists should contain a vertices' inbound edges
#The list of vertices should be arranged in DAG order
#Output: A list of path pairs
def computeDAGBasis(vertices, adjListIn):
    maxLength = pow(2, 64) - 1
    paths = [[[-1 for x in range(len(vertices))] for y in range(len(vertices))] for z in range(len(vertices))]  #represents shortest path pairs
                                                                                                                #index 1 = target
                                                                                                                #index 2 = source
                                                                                                                #list pointed to by indexes 1,2 represents path from source to target
    pathLengths = [[maxLength for x in range(len(vertices))] for y in range(len(vertices))]     #path length of maxLength means unreachable
                                                                                                #index 1 = target
                                                                                                #index 2 = source 
                                                                                                #Note that path length denotes the number of vertices in the path 
                                                                                                 
    basis = []
    for i in range(len(vertices)):
        pathLengths[i][i] = 1

    for i in range(len(vertices)):
        paths[i][i][0] = i

    #Iterate over all edges
    for i in range(len(vertices)):
        for j in range(len(adjListIn[i])):
            u = adjListIn[i][j]
            v = vertices[i]
            P = set()
            PBar = set()

            #Construct the set P
            for k in range(len(vertices)):
                if(pathLengths[u][k] < maxLength and pathLengths[v][k] < maxLength):
                    P.add(k)

            #Construct the set P-bar
            for k in P:
                remove = 0
                for l in P:
                    if(k != l and pathLengths[l][k] < maxLength):
                        remove = 1
                if(remove == 0):
                    PBar.add(k)

            #Add new path pairs to the basis
            for w in PBar:
                lengthP = pathLengths[u][w]
                lengthPPrime = pathLengths[v][w]
                pathPair =[]
                copyP = copy.deepcopy(paths[u][w][0:lengthP])
                copyP.append(v)
                copyPPrime = copy.deepcopy(paths[v][w][0:lengthPPrime])
                pathPair.append(copyP)
                pathPair.append(copyPPrime) 
                basis.append(pathPair)

            #Update the graph
            for k in range(len(vertices)):
                if(pathLengths[u][k] < maxLength):
                    curr = pathLengths[v][k]
                    alt = pathLengths[u][k]
                    if(alt + 1 < curr):
                        pathLengths[v][k] = alt + 1
                        paths[v][k] = copy.deepcopy(paths[u][k])
                        paths[v][k][alt] = v

    return basis

#Sample run
vert = [0, 1, 2]
adjList = [[], [0], [0, 1]]    
out = computeDAGBasis(vert, adjList)
print(out)

    
    

