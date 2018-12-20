# # 1st Assignment - Network Connectivity - part B
# This assignment involves the importing and analysis of an internal email communication network amongst employees
# of a manufacturing company.
#
# Each node depicts and employee and each directed edge between two nodes depicts and individual mail. The node to the
# left represents the sender and the node to the right represents the recipient.

# ======================================================================================================================
# The reason that exists methods like load_answer_<number> is just for printing purposes
# ======================================================================================================================

import networkx as nx
import pandas as pd
file_path = "./data/mail_network.txt"

# ### Question 1
#
# Use NetworkX to load up the directed multigraph, located in `mail_network.txt` and make sure the node names are
# strings.
#
# [*Returns a directed multigraph networkx graph]


def answer_one():
    # Your Code Here
    multigraph_df = pd.read_csv(file_path, delim_whitespace=True, header=0, names=["Sender", "Recipient", "time"])
    multigraph_g = nx.from_pandas_edgelist(multigraph_df, "Sender", "Recipient", edge_attr="time", create_using=nx.MultiDiGraph)
    print("1B 1-------------------------------------------------------------------------------------------")
    print("G info: ")
    print(nx.info(multigraph_g))
    return multigraph_g  # Your Answer Here


def load_answer_one():
    # Your Code Here
    multigraph_df = pd.read_csv(file_path, delim_whitespace=True, header=0, names=["Sender", "Recipient", "time"])
    multigraph_g = nx.from_pandas_edgelist(multigraph_df, "Sender", "Recipient", edge_attr="time", create_using=nx.MultiDiGraph)
    return multigraph_g  # Your Answer Here


# ### Question 2
#
# Find the number of employees and mails in the graph from Question 1.
#
# [*Returns a tuple (<num_of_employees>, <num_of_mails>).*


def answer_two():
    # Your Code Here
    G = load_answer_one()
    num_of_employees = nx.number_of_nodes(G)
    num_of_mails = nx.number_of_edges(G)
    myTuple = (num_of_employees, num_of_mails)
    print("1B 2-------------------------------------------------------------------------------------------")
    print("<num_of_employees>, <num_of_mails>: ")
    print(myTuple)
    return myTuple  # Your Answer Here


# ### Question 3
#
# * Part 1. For this part, we assume that the information in this company can only be exchanged via mail.
#
#   Whenever an employee sends a mail to another employee, a one-way communication channel is created, which allows the
#   sender to provide info to the receiver, but not vice versa
#
#   Based on the mail transaction present in our dataset, detect whether it is possible for info to go from every employ
#   to every other employ (True, False)
#
# * Part 2. For this part, we assume that the communication channel that is established by a mail allows for vice-versa
#           communication (both ways)
#
#   Based on the mail transaction present in our dataset, detect whether it is possible for info to go from every employ
#   to every other employ (True, False)
#
# [*Returns a tuple of bools (<part1>, <part2>)]

def answer_three():
    # Your Code Here
    G = load_answer_one()
    strongly_connected_g_is = nx.is_strongly_connected(G)
    weakly_connected_g_is = nx.is_weakly_connected(G)
    myTuple = (strongly_connected_g_is, weakly_connected_g_is)
    print("1B 3-------------------------------------------------------------------------------------------")
    print("<is_strongly_connected>, <is_weakly_connected>: ")
    print(myTuple)
    return myTuple  # Your Answer Here


# ### Question 4
#
# What is the number of nodes in the largest (in terms of nodes) weakly connected component?
#
# [*Returns an int]


def answer_four():
    # Your Code Here
    G = load_answer_one()
    weakly_connected_sg_max = max(nx.weakly_connected_component_subgraphs(G), key=len)
    weakly_connected_sg_max_nodes = nx.number_of_nodes(weakly_connected_sg_max)
    print("1B 4-------------------------------------------------------------------------------------------")
    print("max_weakly_connected_nodes: ")
    print(weakly_connected_sg_max_nodes)
    return weakly_connected_sg_max_nodes  # Your Answer Here


# ### Question 5
#
# What is the number of nodes in the largest (in terms of nodes) strongly connected component?
#
# [*Returns an int]

def answer_five():
    # Your Code Here
    G = load_answer_one()
    strongly_connected_sg_max = max(nx.strongly_connected_component_subgraphs(G), key=len)
    strongly_connected_sg_max_nodes = nx.number_of_nodes(strongly_connected_sg_max)
    print("1B 5-------------------------------------------------------------------------------------------")
    print("max_strongly_connected_nodes: ")
    print(strongly_connected_sg_max_nodes)
    return strongly_connected_sg_max_nodes  # Your Answer Here


# ### Question 6
#
# Use the NetworkX function for strongly connected component subgraphs to find the subgraph of nodes in a largest
# strongly connected component. Assume that this graph is called G_sc.
#
# [*Returns a NetworkX MultiDiGraph named G_sc]


def answer_six():
    # Your Code Here
    G = load_answer_one()
    G_sc = max(nx.strongly_connected_component_subgraphs(G), key=len)
    print("1B 6-------------------------------------------------------------------------------------------")
    print("G info: ")
    print(nx.info(G_sc))
    return G_sc  # Your Answer Here


def load_answer_six():
    # Your Code Here
    G = load_answer_one()
    G_sc = max(nx.strongly_connected_component_subgraphs(G), key=len)
    return G_sc  # Your Answer Here

# ### Question 7
#
# Calculate the average distance between nodes in G_sc (from question 6)
#
# [*Returns a float]


def answer_seven():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        avg = nx.average_shortest_path_length(G_sc)
        print("1B 7-------------------------------------------------------------------------------------------")
        print("average distance between nodes: ")
        print(avg)
    except nx.NetworkXError:
        print("G is not connected")
        avg = 0
    return avg  # Your Answer Here


# ### Question 8
#
# Calculate the largest possible distance between two employees in the G_sc graph (from question 6)
#
# [*Returns an int]


def answer_eight():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        d = nx.diameter(G_sc)
        print("1B 8-------------------------------------------------------------------------------------------")
        print("largest possible distance between nodes: ")
        print(d)
    except nx.exception.NetworkXError:
        print("Found infinity path length because the graph is not connected")
        d = 0
    return d  # Your Answer Here


# ### Question 9
#
# Find the set of nodes in G_sc with eccentricity equal to the diameter
#
# [*Returns the set of the node(s)]


def answer_nine():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        # d = nx.diameter(G_sc)
        # e = nx.eccentricity(G_sc)
        # eccentricity_equal_d = [i for i in e if (e[i] == d)]
        eccentricity_equal_d = set(nx.periphery(G_sc))
        print("1B 9-------------------------------------------------------------------------------------------")
        print("set of nodes with eccentricity equal to the diameter: ")
        print(eccentricity_equal_d)
    except nx.exception.NetworkXError:
        print("Found infinity path length because the graph is not connected")
        eccentricity_equal_d = 0
    return eccentricity_equal_d  # Your Answer Here


# ### Question 10
#
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
#
# [*Returns the set of the node(s)]


def answer_ten():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        # rad = nx.radius(G_sc)
        # e = nx.eccentricity(G_sc)
        # eccentricity_equal_rad = [i for i in e if (e[i] == rad)]
        eccentricity_equal_rad = set(nx.center(G_sc))
        print("1B 10------------------------------------------------------------------------------------------")
        print("set of nodes with eccentricity equal to the radius: ")
        print(eccentricity_equal_rad)
    except nx.NetworkXError:
        print("G is not connected")
        eccentricity_equal_rad = 0
    return eccentricity_equal_rad  # Your Answer Here


# ### Question 11
#
# Find which node in G_sc is connected to the most other nodes by a shortest path of length equal to the diameter
# of G_sc
#
# Find the number of nodes that are connected to this node
#
# [*Returns a tuple (<name of node>, <number of satisfied connected nodes>)]


def answer_eleven():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        d = nx.diameter(G_sc)
        peripheries = nx.periphery(G_sc)
        max_count = -1
        result_node = None
        for node in peripheries:
            sp = nx.shortest_path_length(G_sc, node)
            count = list(sp.values()).count(d)
            if count > max_count:
                result_node = node
                max_count = count
        myTuple = (result_node, max_count)
        print("1B 11------------------------------------------------------------------------------------------")
        print("<name of node>, <number of satisfied connected nodes>: ")
        print(myTuple)
    except nx.exception.NetworkXError:
        print("Found infinity path length because the graph is not connected")
        myTuple = ()
    return myTuple  # Your Answer Here


def load_answer_eleven():
    # Your Code Here
    try:
        G_sc = load_answer_six()
        d = nx.diameter(G_sc)
        peripheries = nx.periphery(G_sc)
        max_count = -1
        result_node = None
        for node in peripheries:
            sp = nx.shortest_path_length(G_sc, node)
            count = list(sp.values()).count(d)
            if count > max_count:
                result_node = node
                max_count = count
        myTuple = (result_node, max_count)
    except nx.exception.NetworkXError:
        print("Found infinity path length because the graph is not connected")
        myTuple = ()
    return myTuple  # Your Answer Here

# ### Question 12
#
# Assuming that we want to prevent the communication from flowing from the node that we found in question 11 from any
# node in the center of G_sc, detect the smallest number of nodes you would need to remove from the graph (you are not
# allowed to remove the node from the previous question or the center nodes).
#
# [*Returns an integer]

def answer_twelve():
    # Your Code Here
    G_sc = load_answer_six()
    center = nx.center(G_sc)[0]
    node = load_answer_eleven()[0]
    minimum_node_cut = len(nx.minimum_node_cut(G_sc, center, node))
    print("1B 12------------------------------------------------------------------------------------------")
    print("G minimum_node_cut: ")
    print(minimum_node_cut)
    return minimum_node_cut  # Your Answer Here


# ### Question 13
#
#
# Create an undirected graph named G_un using G_sc (it is possible to ignore the attributes).
#
# [*Returns a NetworkX Graph (G_un)]

# In[ ]:

def answer_thirteen():
    # Your Code Here
    G_sc = load_answer_six()
    G_un_sb = G_sc.to_undirected()
    G_un = nx.Graph(G_un_sb)
    print("1B 13------------------------------------------------------------------------------------------")
    print("G info: ")
    print(nx.info(G_un))
    return G_un  # Your Answer Here


def load_answer_thirteen():
    # Your Code Here
    G_sc = load_answer_six()
    G_un_sb = G_sc.to_undirected()
    G_un = nx.Graph(G_un_sb)
    return G_un  # Your Answer Here

# ### Question 14
#
# Find the transitivity and the average clustering coefficient of graph G_un.
#
# [*Returns a tuple (<transitivity>, <avg_clustering_coefficient>]

# In[ ]:

def answer_fourteen():
    # Your Code Here
    G_un = load_answer_thirteen()
    transitivity = nx.transitivity(G_un)
    avg_clustering_coefficient = nx.average_clustering(G_un)
    myTuple = (transitivity, avg_clustering_coefficient)
    print("1B 14------------------------------------------------------------------------------------------")
    print("<transitivity>, <avg_clustering_coefficient>: ")
    print(myTuple)
    return myTuple  # Your Answer Here
