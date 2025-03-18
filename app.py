from flask import Flask, jsonify
import random

app = Flask(__name__)

graph_problems = [
    "DFS", "BFS", "Rotten Tomatoes", "Flood Fill", "Map of the Highest Peak",
    "Number of Provinces", "Number of Islands", "Detect Cycle in Graph",
    "Surrounded Regions", "Number of Enclaves", "Number of Distinct Islands",
    "Bipartite Graphs", "Cycle Detection in Directed Graph Using DFS",
    "Eventual Safe States", "Topological Sort", "Kahn's Algorithm",
    "Course Schedule I and II and IV", "Detect Cycle Using BFS",
    "Eventual Safe State Using Topological Sort", "Alien Dictionary",
    "Shortest Distance in DAG", "Shortest Distance in an Undirected Graph Using BFS",
    "Word Ladder", "Dijkstra's Algorithm Using Priority Queue",
    "Dijkstra's Algorithm Using Set", "Print Shortest Path Using Dijkstra's Algorithm",
    "Shortest Distance in Binary Maze", "Path with Minimum Effort",
    "Cheapest Flight with K Stops", "Number of Ways to Reach Destination",
    "Kruskal Algorithm", "Bellman Ford Algorithm", "City with Smallest Number",
    "Prim's Algorithm", "Kruskal + Disjoint Set", "Minimum Operations to Connect Graph",
    "Making a Large Island", "Word Search"
]

tree_problems = [
    "Inorder, Preorder, and Postorder Traversals", "Invert Binary Tree",
    "Symmetric Trees", "Breadth-First Search (BFS)", "Maximum Depth",
    "Diameter", "Subtree of a Tree", "Balanced Binary Tree",
    "Lowest Common Ancestor", "Vertical Traversal", "Left and Right View",
    "Top and Bottom View", "Validate Binary Search Tree (Using Range)",
    "Maximum Path Sum", "Kth Smallest Element in BST", "Count Good Nodes",
    "Max Width of BT", "Create a Height Balanced BST from Sorted Array",
    "Fix a BST", "Serialize and Deserialize a BT",
    "Construct BT from Inorder and Preorder Vectors"
]


@app.route('/')
def random_problems():
    graph_selected = random.sample(graph_problems, 2)
    tree_selected = random.sample(tree_problems, 2)
    
    return jsonify({
        "Graph Problems": graph_selected,
        "Tree Problems": tree_selected
    })

if __name__ == "__main__":
    app.run(debug=True)
