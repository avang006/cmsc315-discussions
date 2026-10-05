"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # 1. Edge Case: If the start node is completely missing from the graph definition, 
    # handle it safely by returning an empty list to avoid throwing a KeyError.
    if start not in graph:
        return []

    # 2. Initialization: Set up the track paths.
    visited_order = []          # Keeps track of the exact sequence nodes are fully processed
    visited_set = set()         # Tracks unique visited keys for O(1) membership lookups
    
    # Why a queue is used: 
    # A queue follows First-In, First-Out (FIFO) behavior. This guarantees that elements 
    # entered into the system first (closer layers) are dequeued and processed before elements 
    # discovered later (deeper layers). This naturally enforces a uniform, radial expansion.
    queue = deque([start])
    visited_set.add(start)

    while queue:
        # Pull the next person out from the front of the queue to process them
        current_node = queue.popleft()
        visited_order.append(current_node)

        # Look at every direct connection (neighbor) of the current person
        for neighbor in graph[current_node]:
            # Why neighbors are added to the queue:
            # We append unvisited neighbors to the back of the queue. Because of FIFO ordering, 
            # all current-tier neighbors will finish processing before *their* respective 
            # downstream neighbors are ever touched. This builds our level-by-level ripple effect.
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)

    # How BFS differs from Depth-First Traversal (DFS):
    # BFS explores the graph horizontally layer by layer using a FIFO Queue, making it ideal for 
    # finding the absolute shortest path to an element. Conversely, DFS uses a LIFO Stack to plunge 
    # as deep as possible down a single structural branch before backtracking, prioritizing path 
    # exhaustion over structural proximity.
    return visited_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    print("\n=== GRAPH STRUCTURE ===")
    
    # Real-World Scenario: A professional social network (like LinkedIn).
    # Nodes represent individuals.
    # Edges represent mutual 1st-degree professional connections.
    
    # 1. & 2. & 3. Create graph with 6 initial nodes and multiple cross-connections.
    social_graph = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "David", "Eve"],
        "Charlie": ["Alice", "Eve"],
        "David": ["Bob", "Frank"],
        "Eve": ["Bob", "Charlie", "Frank"],
        "Frank": ["David", "Eve"]
    }

    # 4. Display the graph structure cleanly
    print("Professional Network Layout (Adjacency List):")
    for person, connections in social_graph.items():
        print(f"  {person} is connected to --> {connections}")
        
    print("\nExplanation: Nodes represent people; the adjacency arrays show direct 1st-degree links.")

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    print("\n=== BFS TRAVERSAL ===")
    
    # 1. & 2. & 3. Select start node and execute BFS.
    start_person = "Alice"
    initial_traversal = bfs(social_graph, start_person)
    print(f"BFS Exploration Order starting from {start_person}:")
    print(f"  {initial_traversal}")
    
    # 4. Explain how BFS visits nodes level by level
    # Level 0: Alice (Starting node)
    # Level 1 (Direct connections): Bob, Charlie
    # Level 2 (Friends-of-friends): David, Eve
    # Level 3 (3rd-degree links): Frank
    print("\nExplanation of Levels:")
    print("  - Level 0 (Origin): Alice")
    print("  - Level 1 (1st Degree): Bob and Charlie are visited first.")
    print("  - Level 2 (2nd Degree): David and Eve are pulled in via Bob and Charlie.")
    print("  - Level 3 (3rd Degree): Frank is reached last through David and Eve.")

    # 5. Add an additional node/edge and demonstrate updating the network layout dynamically.
    print("\n--- Updating Network: Adding 'Grace' connected to 'Frank' ---")
    social_graph["Frank"].append("Grace")
    social_graph["Grace"] = ["Frank"]  # Bidirectional edge declaration
    
    updated_traversal = bfs(social_graph, start_person)
    print(f"Updated BFS Order after Grace joins network:")
    print(f"  {updated_traversal}")
    print("Notice how Grace automatically surfaces at the absolute end, mapping accurately as a 4th-degree link.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")
    
    # Edge Case 1: Safe handling of a completely missing search key request
    missing_target = "Zane"
    print(f"1. Attempting BFS with a missing start node '{missing_target}':")
    missing_result = bfs(social_graph, missing_target)
    print(f"   Result list: {missing_result}")
    print("   -> Explanation: Safe guard intercept prevents 'KeyError' exceptions by verifying lookup bounds first.")

    # Edge Case 2: Executing BFS across a completely disconnected sub-network (Island Isolation)
    print("\n2. Simulating a disconnected network entry ('Ian' and 'Jill' are stranded on their own island):")
    social_graph["Ian"] = ["Jill"]
    social_graph["Jill"] = ["Ian"]
    
    isolated_result = bfs(social_graph, "Ian")
    print(f"   BFS tracking starting from isolated user 'Ian': {isolated_result}")
    print("   -> Explanation: BFS processes the isolated island entirely but will never cross over to Alice's")
    print("      component because there are no edge pathways connecting the two sub-graphs together.")


if __name__ == "__main__":
    main()
