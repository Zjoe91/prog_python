
import csv
import networkx as nx
import matplotlib.pyplot as plt

#FIRST EXERCISE
def parse_csv_to_graph (file_csv):
    com_graph = {}
    try:
        with open (file_csv) as file:
            reader = csv.DictReader(file)

            # The code iterates over the rows of the CSV data, 
            # extracting the source and target nodes from each row.
            for row in reader:
                source = row['source']
                target = row['target']


                # For each edge, the code checks if the source node exists in the graph. 
                # If it does, the code appends the target node to its list of neighbors. 
                # If it doesn't, the code creates a new list of neighbors for the source node and adds the target node to it.
                # same for the target node to source node to account for all possible connections between the nodes to create a graph.
                if source not in com_graph:
                    com_graph[source] = []
                com_graph[source].append (target)
                if target not in com_graph:
                    com_graph[target] = []
                com_graph[target].append(source)
            return com_graph 

    except FileNotFoundError:
        print(f"File '{file_csv}' not found")


#SECOND EXERCISE

def influence_chains (start, end):
    com_graph1 = parse_csv_to_graph("comedians.csv")

    try:
        # i checked if the start and end nodes exist in the graph, if not i raise an exception
        if start not in com_graph1 or end not in com_graph1:
            raise KeyError("Key not found")

        # i create a list to keep track of visited nodes
        visited = []
        visited.append(start)

        # i created a queue to store the nodes to be explored
        com_queue = [(start,[start])] # i am assigning the start node and the path from it to the queue in a tupple

        while com_queue:
            node, path = com_queue.pop(0)

            if node == end: # If the end node is reached, i return the path
                return path

            for neighbor in com_graph1[node]:
                if neighbor not in visited: # If neighbor not explored, 
                    visited.append(neighbor) # i mark it as explored and add it to the visited list
                    com_queue.append((neighbor, path + [neighbor]))# i mark it as explored and add neighbor to the queue, ready for further exploration.

        return "OoOops No influence chain found"  # If no path exists, i return a message
    except Exception as e:
        print("error:", e)
        return None
    

#THIRD EXERCISE

def top_10_influencers ():
    com_graph2 = parse_csv_to_graph("comedians.csv")

    #dictionary to store the influence scores
    inf_scores = {}
    
    try:
        for node in com_graph2:
            inf_scores[node] = 0

            # traversing the graph using breadth-first search
            visited = []
            visited.append(node)
            com_queue1 = [(node,1)] #i am assigning the start node and the distance from it to the queue in a tupple

        while com_queue1: # i used queing again to traverse the graph using BFS to account direct and indirect influence
            
            current_node, current_score = com_queue1.pop(0)
            
            # calculating the influence score for each node
            for neighbor in com_graph2[current_node]: 
                    
                    if neighbor not in visited: # if neighbor not explored,
                        visited.append(neighbor) # i mark it as explored and add it to the visited list
                        com_queue1.append((neighbor, current_score + 1)) # and add neighbor to the queue with updated distance, ready for further exploration.
                    inf_scores[current_node] += current_score # and update its influence score.

        # sort the influencers based on their influence scores
        sorted_influencers = sorted(inf_scores.items(), key=lambda x: x[1], reverse=True) #Credit for: github.com/saulhappy/algoPractice
        top_10_influencers = sorted_influencers[:10]

        # here i am returning the top 10 influencers with their corresponding scores for better result validation
        top_10_with_scores = []
        for influencer, score in top_10_influencers:
            influencer_score_pair = (influencer, score)
            top_10_with_scores.append(influencer_score_pair)
        return top_10_with_scores
    
    except Exception as e:
        print("error:", e)
        return None


#FOURTH EXERCISE

def pretty_print ():
    com_graph3 = parse_csv_to_graph("comedians.csv")

    try:
        # i create a NetworkX graph from previously generated dictionary (com_graph3)
        G_represent = nx.Graph()
        for node, neighors in com_graph3.items():
            for neighbor in neighors:
                G_represent.add_edge(node, neighbor, length=20)

        # i drew the graph using Matplotlib & NetworkX 
        # i used spring_layout to have a better visual of the graph
        nx.draw(G_represent, 
                with_labels=True, # i set it to True, but to have a clear visual of the nodes and edges, its better to be False
                node_size=15, 
                node_color='red', 
                edge_color='blue', 
                font_size=5, 
                font_color='black',
                arrows = True,  # i set it to True, to incorporate the direction of the edges
                arrowstyle = '-|>', # i used '-|>' to see the direction of the edges
                pos = nx.spring_layout(G_represent, k=0.2) # i used k=0.2 to have a better visual of the graph
                )
        plt.show()
    
    except nx.NetworkXError as e:
        print("NetworkXError:", e)
        print("Error occurred during graph operations.")
