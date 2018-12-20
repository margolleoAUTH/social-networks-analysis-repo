# # 1st Assignment - Creation and manipulation of Graphs - part A
#
# A small company asked eight of its employees to choose 3 movies that they would prefer to watch at an upcoming
# scheduled movie night. The choices of the employees are store in the file `employee_movies_preferences.txt`
#  The file # `employee_relationships.txt` contains data about the relationships between different coworkers.
#
# Relationship scores range from `-100` (Enemies) to `+100` (Best friends). Zero values mean that the employees have
# never interacted with one another or are indifferent.
#
# The files are delimited using tabs.

# ======================================================================================================================
# The reason that exists methods like load_answer_<number> is just for printing purposes
# ======================================================================================================================

import networkx as nx
import pandas as pd
import numpy as np
from networkx.algorithms import bipartite

# This is the set of employees
employees = {"Pablo", "Lee", "Georgia", "Vincent", "Andy", "Frida", "Joan", "Claude"}

# This is the set of movies
movies = {"The Shawshank Redemption", "Forrest Gump", "The Matrix", "Anaconda", "The Social Network", "The Godfather",
          "Monty Python and the Holy Grail", "Snakes on a Plane", "Kung Fu Panda", "The Dark Knight", "Mean Girls"}


file_path = "./data/employee_movies_preferences.txt"
file_path_relationships = "./data/employee_relationships.txt"

# The following method can be used to plot your graphs
# It would preferably be commented out upon submission
def plot_graph(G, weight_name=None):
    """
    G: a networkx G
    weight_name: name of the attribute for plotting edge weights (if G is weighted)
    """
    import matplotlib.pyplot as plt

    plt.figure()
    pos = nx.spring_layout(G)
    edges = G.edges()
    weights = None

    if weight_name:
        weights = [int(G[u][v][weight_name]) for u, v in edges]
        labels = nx.get_edge_attributes(G, weight_name)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        nx.draw_networkx(G, pos, edges=edges, width=weights)
    else:
        nx.draw_networkx(G, pos, edges=edges)
    plt.show()


# ### Question 1
#
# Load the bipartite graph contained in `employee_movies_preferences.txt` by using NetworkX and return the graph
#

# [*Returns* a networkx graph with 19 nodes and 24 edges*]

def answer_one():
    # Your Code Here
    G = nx.read_adjlist(file_path, delimiter="\t")
    print("1A 1a------------------------------------------------------------------------------------------")
    print("Is bipartice: ")
    print(bipartite.is_bipartite(G))
    print("1A 1b------------------------------------------------------------------------------------------")
    print("G info: ")
    print(nx.info(G))
    # plot_graph(G)
    return G  # Your Answer Here


def load_answer_one():
    # Your Code Here
    G = nx.read_adjlist(file_path, delimiter="\t")
    # plot_graph(G)
    return G  # Your Answer Here

# ### Question 2
#
# Utilizing the graph from the previous question, add node attributes named `"type"` in which movies have the value
# `"movie"`, while employees have the value `"employee"`. Then, return the graph.
#
# *This function should return


# [*Returns* a networkx graph with node attributes `{"type": "movie"}` or `{"type": "employee"}`]

def answer_two():
    # Your Code Here
    G = load_answer_one()
    nx.set_node_attributes(G, dict.fromkeys(employees, "employee"), "type")
    nx.set_node_attributes(G, dict.fromkeys(movies, "movie"), "type")
    return G  # Your Answer Here


# ### Question 3
#
# Detect a weighted projection of the graph from the previous answer (`answer_two`) which shows us how many movies are
# common for different pairs of employees.

# [*Returns* a weighted projected graph]

def answer_three():
    # Your Code Here
    G = answer_two()
    M = bipartite.weighted_projected_graph(G, movies)
    print("1A 3-------------------------------------------------------------------------------------------")
    print("G info: ")
    print(nx.info(M))
    # plot_graph(M)
    return M  # Your Answer Here


# ### Question 4
#
# Let"s suppose that we would like to find out if people who have a high relationship score to one another, also like
# the same types of movies
#
# To achieve this, find the the Pearson Correlation (using `DataFrame.corr()`) between the employee relationships scores
# and the number of movies that are common between them. If two employees have no common movies, it should be treated
# as a 0 value rather than a missing value, and should be accounted for in the correlation calculation.
#
# [*Returns a float]

def answer_four():
    # Your Code Here
    G = answer_two()
    E = bipartite.weighted_projected_graph(G, employees)

    relationship_df = pd.read_csv(file_path_relationships, delim_whitespace=True, header=None, names=["E1", "E2", "Relationship"])
    relationship_g = nx.from_pandas_edgelist(relationship_df, "E1", "E2", edge_attr="Relationship")

    weight_attr = {(i[0], i[1]): i[2] for i in E.edges(data="weight")}
    nx.set_edge_attributes(relationship_g, 0, "Shared_Movies")
    nx.set_edge_attributes(relationship_g, weight_attr, "Shared_Movies")

    idx = [(i[0], i[1]) for i in relationship_g.edges(data=True)]
    relationship = [i[2] for i in relationship_g.edges(data="Relationship")]
    movies = [i[2] for i in relationship_g.edges(data="Shared_Movies")]

    # correlation_df = pd.DataFrame({"Relationship": relationship, "Shared_Movies": movies}, index=idx)
    # correlation_pearson = correlation_df.corr("pearson")
    correlation_pearson_np = np.corrcoef(relationship, movies)
    print("1A 4-------------------------------------------------------------------------------------------")
    print("Pearson Correlation: ")
    print(correlation_pearson_np[0][1])
    return correlation_pearson_np[0][1]  # Your Answer Here
