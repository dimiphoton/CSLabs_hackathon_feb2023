from py2neo import Graph, Node, Relationship

# Create a new graph database
graph = Graph()

# Create nodes for activities, problems, and solutions
a1 = Node("Activity", name="Activity 1")
a2 = Node("Activity", name="Activity 2")
b1 = Node("Problem", name="Problem 1")
b2 = Node("Problem", name="Problem 2")
s1 = Node("Solution", name="Solution 1")
s2 = Node("Solution", name="Solution 2")
s3 = Node("Solution", name="Solution 3")

# Create relationships between the nodes
r1 = Relationship(a1, "HAS_PROBLEM", b1)
r2 = Relationship(a1, "HAS_SOLUTION", s1)
r3 = Relationship(a1, "HAS_SOLUTION", s2)
r4 = Relationship(a2, "HAS_PROBLEM", b2)
r5 = Relationship(a2, "HAS_SOLUTION", s2)
r6 = Relationship(a2, "HAS_SOLUTION", s3)

# Add the nodes and relationships to the graph
graph.create(a1, a2, b1, b2, s1, s2, s3, r1, r2, r3, r4, r5, r6)