import streamlit as st
import random

# Questions dictionary
questions = {
    "Graphs": [
        "DFS", "BFS", "Rotten Tomatoes", "Flood Fill", "Map of the Highest Peak (Simple BFS)",
        "Number of Provinces", "Number of Islands", "Detect Cycle in Graph", "Surrounded Regions",
        "Number of Enclaves", "Number of Distinct Islands", "Bipartite Graphs",
        "Cycle Detection in Directed Graph Using DFS", "Eventual Safe States", "Topological Sort",
        "Khan's Algorithm (Topological Sort Using DFS)", "Course Schedule I and II",
        "Detect Cycle Using BFS (Topological Sort)", "Eventual Safe State Using Topological Sort (Reverse Graph)",
        "Alien Dictionary", "Shortest Distance in DAG", "Shortest Distance in an Undirected Graph Using BFS",
        "Word Ladder", "Dijkstra's Algorithm Using Priority Queue", "Dijkstra Using Set",
        "Print Shortest Path Using Dijkstra", "Shortest Distance in Binary Maze (Easy)",
        "Path with Minimum Effort (Bit Tricky)", "Cheapest Flight with K Stops",
        "Number of Ways to Reach Destination (New Intuition)", "Kruskal's Algorithm",
        "Bellman-Ford Algorithm", "City with Smallest Number", "Prim's Algorithm (Minimum Spanning Tree)",
        "Disjoint Set", "Number of Provinces Using Disjoint Set", "Minimum Number of Operations to Connect Graph",
        "Redundant Connection"
    ],
    "Trees": [
        "Inorder, Preorder, and Postorder Traversals (Recursive and Iterative)", "Invert Binary Tree",
        "Symmetric Trees", "Breadth-First Search (BFS)", "Maximum Depth", "Diameter",
        "Subtree of a Tree", "Balanced Binary Tree", "Lowest Common Ancestor", "Vertical Traversal",
        "Left and Right View", "Top and Bottom View (DFS and BFS)", "Validate Binary Search Tree (Using Range)",
        "Maximum Path Sum", "Kth Smallest Element in BST", "Count Good Nodes",
        "Maximum Width of Binary Tree", "Create a Height Balanced BST from Sorted Array"
    ],
    "Linked Lists": [
        "Reverse a Linked List", "LRU CACHE", "Find the Middle of a Linked List",
        "Detect a Loop in a Linked List", "Remove a Loop from Linked List", "Merge Two Sorted Linked Lists",
        "Intersection Point of Two Linked Lists", "Delete Node Without Head Pointer",
        "Add Two Numbers Represented by Linked Lists", "Clone a Linked List with Random Pointers",
        "Sort a Linked List", "Flatten a Multilevel Doubly Linked List", "Reverse Nodes in k-Group",
        "Rotate a Linked List", "Remove Duplicates from Sorted Linked List",
        "Remove Duplicates from Unsorted Linked List", "Check If Linked List Is a Palindrome",
        "Partition List", "Reorder List", "Merge K Sorted Lists", "Add Two Numbers II",
        "Convert Binary Number in a Linked List to Integer", "Swap Nodes in Pairs", "Odd Even Linked List",
        "Split Linked List in Parts", "Sort List Using Merge Sort", "Linked List Cycle II (Find Starting Point)",
        "Convert Sorted List to BST", "Flatten Binary Tree to Linked List", "Remove Nth Node From End of List"
    ],
    "Others": [
        "Sort an Array Using Merge Sort", "Find All Permutations of a String"
    ]
}

# Title
st.title("Random DSA Question Generator")

# Button to generate
if st.button("Generate Questions"):
    for topic, qlist in questions.items():
        st.subheader(topic)
        for idx, q in enumerate(random.sample(qlist, 2 if len(qlist) >= 2 else len(qlist)), 1):
            st.markdown(f"{idx}. {q}")
