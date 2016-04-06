# coding: utf-8

# This script reads the .csv file generated by tropes1.csv,
# and "does stuff" with it in Python code.

from pattern.db import Datasheet, pd

# The Datasheet object is a like an Excel-sheet in Python.
# It provides an easy-to-use reader/writer for .csv files.
# Basically, it reads a .csv file as a list of rows,
# in which each item is a list of column values.
# For example:
# [["trope1", "movie1, movie2, ...", "description"],
#  ["trope2", "movie3, movie3, ...", "description"]
# ]

# The pd() function means "parent directory".
# It points to the folder that contains the script you are looking at.
# So, if you have a "data.csv" file in the same folder as this script,
# you can reference it from this script with pd("data.csv").

tropes = {} # {trope1: [movie1, movie2, ...], ...}
movies = {} # {movie1: [trope1, trope2, ...], ...}

# Read each row in the .csv file.
for trope, examples, description in Datasheet.load(pd("tropes.csv")):
    # The examples of movies that use this trope are separated by a newline (\n).
    # Split the string into a list:
    examples = examples.split("\n")
    # Add each new trope to the tropes dictionary.
    if not trope in tropes:
        tropes[trope] = set() # set() is like a list, but never contains duplicates.
    # Add each new movie to the movies dictionary.
    for movie in examples:
        if not movie in movies:
            movies[movie] = set()
        movies[movie].add(trope)
        tropes[trope].add(movie)

print len(tropes), "tropes"
print len(movies), "movies"
print

print movies["Star Wars Episode III"] 
print
# - Fire and Brimstone Hell
# - Teach Him Anger

print tropes["Teach Him Anger"]
print
# - Star Wars Episode III
# - Ben Hur
# - Star Trek: The Original Series
# - Cool Runnings
# - Doctor Who
# - Buffy the Vampire Slayer

# So, given a movie, we can look for similar movies,
# where "similar" means movies that use the same tropes (naive approach):

def similar(movie1, top=10):
    """ Returns a list of similar movies.
        Each item in the list is a (number of shared tropes, movie)-tuple.
    """
    similarity = {} # {movie2: similarity score}
    for movie2, tropes in movies.items():
        similarity[movie2] = 0
        for t in tropes:
            if t in movies[movie1]:
                similarity[movie2] += 1
            # Note: the similarity score is the number of shared tropes.
            # We could make it better by also taking into account
            # the number of tropes that differ between two movies.
    scores = [(score, movie) for movie, score in similarity.items()]
    scores = sorted(scores, reverse=True)
    scores = scores[1:top+1]
    return scores
    
print similar("Sherlock Holmes")
print
# - 43, Doctor Who (seems to be linked to almost every trope?)
# - 34, Buffy the Vampire Slayer
# - 20, The X-Files
# - ...

# ------------------------------------------------------------------------------------

# Another approach is to create a network of movies linked by tropes (or vice versa).
# A network can be represented as a graph with nodes (= things) 
# and edges (connections between things).
# http://www.clips.ua.ac.be/pages/pattern-graph

from pattern.graph import Graph

g = Graph()
for movie, tropes in movies.items():
    g.add_node(movie)
    for trope in tropes:
        g.add_node(trope)
        g.add_edge(movie, trope) # connection between movie <=> trope

# What nodes directly connect to a given trope?
for node in g["Teach Him Anger"].links:
    print node

# What is the shortest path between two nodes in the network?
print
print g.shortest_path("Cinderella", "Alien")

# Cinderella => Race Against the Clock => The X-Files => Absurdly Spacious Sewer => Alien

# Could we transform this into a tweet? For example:
# "I just watched Alien vs. Cinderella...
#  a mind-blowing race against the clock in an absurdly spacious sewer!"

# The network is too large visualize as a whole 
# (using only Pattern tools).
# But we can visualize sub-networks:
# http://www.clips.ua.ac.be/pages/pattern-graph#canvas

node = g["Lassie"]
halo = node.flatten(depth=2) 

# The node "halo" is the node itself (depth 0),
# nodes connected to it (depth 1),
# nodes connected to those nodes (depth 2),
# and so on.

# Graph.copy() returns a new copy of a graph,
# optionally only including a subset of nodes.
g2 = g.copy(nodes=halo)

# Add some coloring to discern between movies and tropes.
# Each edge has movie (node1) <=> trope (node2).
for e in g2.edges:
    e.node1.stroke = (0,0,1,1) # R,G,B,A blue
    e.node2.stroke = (1,0,0,1) # R,B,B,A red

g2.export("lassie-halo")

# This should generate a "lassie-halo" folder,
# containing an "index.html". Open it in a browser...