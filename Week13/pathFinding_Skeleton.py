import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph
G = nx.Graph()

# Add nodes (representing locations in the city)
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Add weighted edges (representing roads with distances)
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 1),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
]
G.add_weighted_edges_from(edges)

# Draw the graph
# layout where nodes are evenly distributed 
 #and edges are of similar length.
pos = nx.spring_layout(G) 

#draw nodes   
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')

#retrieves the weights of all edges in the graph G and returns them as a dict
    #keys are tuples representing the edges and the values are the weights.
labels = nx.get_edge_attributes(G, 'weight')

#draw edges
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


# Finding Path - Example usage

        
plt.show()


#print(f"Dijkstra's shortest path from {start_node} to {goal_node}: {dijkstra_result}")
#print(f"A* shortest path from {start_node} to {goal_node}: {astar_result}")
