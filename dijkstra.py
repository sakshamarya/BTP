import pandas as pd
import networkx as nx
import math

df = pd.read_csv('dataset.csv')

print(df)

adjMatrix = df.to_numpy()

shortestPathColumn=[]

for i in range(0,len(adjMatrix)):
    size = math.sqrt(len(adjMatrix[i]))
    A = adjMatrix[i].reshape(int(size),int(size))

    G = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

    # length gives shortest path, path gives shortest length path
    length, path = nx.bidirectional_dijkstra(G, 0, size-1) 

    shortestPathColumn.append(length)

    print(length,path)

# inserting dijkstra min cost column to csv
df.insert(16, column = "minCost", value = shortestPathColumn)  
df.head()

print(df)

# updating csv with new dataframe
df.to_csv("dataset.csv")