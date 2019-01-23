# # 3rd Assignment
#
# This assignment will enable you to explore measure of centrality on two networks, a friendship network and a blog
# network.

# ## Part 1
#
# This part of the assignment (questions 1-4) can be answered by using the network `G1` (a network of friendships at a
# university department). Every node corresponds to a person, and every edge represents a friendship.
#
# *The network is loaded as a networkx graph object `G1`.*

import networkx as nx
import operator

G1 = nx.read_gml("data/university_friendships.gml")


# ### Question 1
#
# Calculate the degree centrality, closeness centrality and normalized betweeness centrality (excluding endpoints) of
# the node #100.
#
# [*Return a tuple of floats (<degree_centrality>, <closeness_centrality>, <betweenness_centrality>)]


def answer_one():
    # Your Code Here
    degree_centrality = nx.degree_centrality(G1)[100]
    closeness_centrality = nx.closeness_centrality(G1)[100]
    betweenness_centrality = nx.betweenness_centrality(G1, normalized=True, endpoints=False)[100]
    myTuple = (degree_centrality, closeness_centrality, betweenness_centrality)
    print(myTuple)
    return myTuple # Your Answer Here


# #### For Questions 2, 3, and 4, we will assume that we don't know anything about the network structure, except for
#all the centrality values of the nodes. Based on this, use one of the covered centrality measures in order to
# rank the nodes and find the most appropriate candidate.

# ### Question 2
#
# Supposedly you are hired by an online e-commerce website and you are tasked with selecting one user in network G1 to
# whom you will send an online shopping voucher. Let's suppose that the user that will receive the voucher will promote and send
# it to their friends in the network. We want the voucher to reach as many nodes as possible. While the voucher can be
# forwarded to multiple users at the same time, the travel distance of the voucher is limited to one step, which means
# that if the voucher travels more than one step in the network, it is no longer valid. Use your knowledge in network
# centrality to select the best candidate for the voucher.
#
# [*Returns an integer, the name of the node.]


def answer_two():
    # Your Code Here
    degree_centrality = nx.degree_centrality(G1)
    voucher_node_degree_centrality = max(degree_centrality, key=degree_centrality.get)
    print(voucher_node_degree_centrality)
    return voucher_node_degree_centrality # Your Answer Here


# ### Question 3
#
# For this question, the limit for the voucher's travel distance is removed. Due to the fact that the network is
# connected, regardless of who you pick, all nodes in the network will eventually receive the voucher. However, the
# point of this question is to ensure that the voucher reaches the nodes in the lowest possible average number of hops.
#
# Change your voucher selection strategy accordingly and write the code to find the best candidate in the network.
#
#
# [*Returns an integer, the name of the node]


def answer_three():
    # Your Code Here
    closeness_centrality = nx.closeness_centrality(G1)
    voucher_node_closeness_centrality = max(closeness_centrality, key=closeness_centrality.get)
    print(voucher_node_closeness_centrality)
    return voucher_node_closeness_centrality # Your Answer Here


# ### Question 4
#
# Assuming that the restriction on the voucher's travel distance is still removed, similarly to the previous question,
# but now a competitor company has developed a strategy to remove a person from the network in order to disrupt the
# distribution of your voucher. More specifically, your competitor is targeting people (nodes) who are often information
# flow bridges between other groups of people.
#
# Find the one, riskiest person that the competitor company can remove from your network.
#
# [*Returns an integer, the name of the node]

def answer_four():
    # Your Code Here
    betweenness_centrality = nx.betweenness_centrality(G1, normalized=True, endpoints=False)
    voucher_node_betweenness_centrality = max(betweenness_centrality, key=betweenness_centrality.get)
    print(voucher_node_betweenness_centrality)
    return voucher_node_betweenness_centrality # Your Answer Here


# ## Part 2
#
# Graph `G2` is a directed graph network of political blogs, in which nodes correspond to a single blog and edges
# correspond to links between blogs. Utilize your knowledge of PageRank and HITS to answer the following questions (5-9)

G2 = nx.read_gml("data/blogs.gml")

# ### Question 5
#
# Use the Scaled Page Rank Algorithm on this network. Find the Page Rank of node 'realclearpolitics.com' with a damping
# value of 0.85
#
# [*Returns a float]


def answer_five():
    # Your Code Here
    page_rank = nx.pagerank(G2, alpha=0.85)
    realclearpolitics = page_rank["realclearpolitics.com"]
    print(realclearpolitics)
    return realclearpolitics # Your Answer Here


# ### Question 6
#
# Use the Scaled Page Rank Algorithm on this network with a damping value of 0.85 in order to find the 5 nodes with the
# highest Page Rqank.
#
# [*Returns a list of the top 5 blogs in desending order of Page Rank]


def answer_six():
    # Your Code Here
    page_rank = nx.pagerank(G2, alpha=0.85)
    page_rank_list = sorted(page_rank.items(), key=operator.itemgetter(1), reverse=True)[0:5]
    top_5_blogs_list = []
    for i in page_rank_list:
        top_5_blogs_list.append(i[0])
    print(top_5_blogs_list)
    return top_5_blogs_list # Your Answer Here


# ### Question 7
#
# Use the HITS Algorithm on the network to find the authority and hub scores of node 'realclearpolitics.com'
#
# [*Return tuple of floats (<authority_score>, <hub_score>)]


def answer_seven():
    # Your Code Here
    hits = nx.hits(G2)
    authority_score = hits[0]["realclearpolitics.com"]
    hub_score = hits[1]["realclearpolitics.com"]
    myTuple = (authority_score, hub_score)
    print(myTuple)
    return myTuple # Your Answer Here


# ### Question 8
#
# Use the HITS Algorithm on this network to find the top 5 nodes with the highest hub scores.
#
# [*Returns a list of the top 5 blogs (nodes) in descending order according to the hub score]


def answer_eight():
    # Your Code Here
    hits = nx.hits(G2)
    hubs = hits[0]
    top_5_blogs_list = sorted(hubs.keys(), key=lambda key: hubs[key], reverse=True)[:5]
    return top_5_blogs_list # Your Answer Here


# ### Question 9
#
# Use the HITS Algorithm on this network to find the top 5 nodes with the highest authority scores.
#
# [*Returns a list of the top 5 blogs (nodes) in descending order according to the authority score]


def answer_nine():
    # Your Code Here
    hits = nx.hits(G2)
    authorities = hits[1]
    top_5_blogs_list = sorted(authorities.keys(), key=lambda key: authorities[key], reverse=True)[:5]
    return top_5_blogs_list # Your Answer Here
