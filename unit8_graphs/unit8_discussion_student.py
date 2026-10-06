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
    # 1. Edge Case: If the selected starting seat is missing from our seating chart configuration,
    # handle it safely by returning an empty list to prevent throwing a system KeyError.
    if start not in graph:
        return []

    # 2. Initialization: Set up the search pathways.
    visited_order = []          # Order in which seats are evaluated for distance proximity
    visited_set = set()         # Tracks unique seats checked to prevent geometric backtracking
    
    # Why a queue is used: 
    # A queue follows First-In, First-Out (FIFO) mechanics. This guarantees that seats 
    # immediately bordering the ideal seat (1 step away) are checked completely before the system 
    # moves to seats farther away (2 or more steps away). This ensures proximity-first searching.
    queue = deque([start])
    visited_set.add(start)

    while queue:
        # Pull the next closest seat out from the front of the queue to check its neighborhood
        current_node = queue.popleft()
        visited_order.append(current_node)

        # Look at every adjacent seat (up, down, left, right neighbors) of the current seat.
        # FIX: Using graph.get() protects the function from crashing if a neighbor node is omitted from the main keys.
        for neighbor in graph.get(current_node, []):
            # Why neighbors are added to the queue:
            # We append unvisited neighboring seats to the back of the queue. Because of FIFO processing, 
            # all seats within a closer tier radius are handled before we drift deeper into the theater, 
            # building an expanding visual ring of alternative choices.
            if neighbor not in visited_set:
                visited_set.add(neighbor)
                queue.append(neighbor)

    # How BFS differs from Depth-First Traversal (DFS):
    # BFS explores the seating arrangement organically in expanding concentric circles, making it perfect 
    # for finding seats with the absolute minimum distance from the target choice. DFS would instead plunge 
    # all the way down a single row to the side wall or back of the auditorium before checking seats sitting 
    # directly next to the user's initial selection.
    return visited_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # CREATE A GRAPH
    # ===============================
    print("\n=== GRAPH STRUCTURE ===")
    
    # Real-World Scenario: Movie Theater Booking System Seat Proximity Optimization.
    # Nodes represent physical seats in a coordinate cluster.
    # Edges represent immediate physical proximity links (directly adjacent spaces).
    
    # 1. & 2. & 3. Create a layout with all necessary nodes mapped cleanly to prevent lookup exceptions.
    seating_map = {
        "C3": ["C2", "C4", "B3"],
        "C2": ["C3", "D2"],
        "C4": ["C3", "D4"],
        "B3": ["C3", "B2", "B4"],
        "B2": ["B3"],
        "B4": ["B3"],
        "D2": ["C2"],  # FIX: Added entry node so graph["D2"] lookup functions safely
        "D4": ["C4"]   # FIX: Added entry node so graph["D4"] lookup functions safely
    }

    # 4. Display the graph structure cleanly
    print("Auditorium Seating Grid Cluster (Adjacency List):")
    for seat, adjacencies in seating_map.items():
        print(f"  Seat [{seat}] touches adjacent spaces --> {adjacencies}")
        
    print("\nExplanation: Nodes are seats; adjacency arrays track physically bordering seating positions.")

    # ===============================
    # BFS TRAVERSAL
    # ===============================
    print("\n=== BFS TRAVERSAL ===")
    
    # 1. & 2. & 3. Select preferred focal seat and execute nearby proximity sweep.
    ideal_seat = "C3"
    proximity_sweep = bfs(seating_map, ideal_seat)
    print(f"BFS Alternative Recommendation Priority starting from preferred seat [{ideal_seat}]:")
    print(f"  {proximity_sweep}")
    
    # 4. Explain how BFS visits nodes level by level
    print("\nExplanation of Distance Tiers (Proximity Steps):")
    print("  - Tier 0 (Perfect Match): C3")
    print("  - Tier 1 (Immediate Neighbors): C2, C4, and B3 are evaluated next as primary backups.")
    print("  - Tier 2 (Secondary Backups): D2, D4, B2, and B4 are swept outward on the next loop layer.")

    # 5. Add an additional node/edge and demonstrate updating the grid layout dynamically.
    print("\n--- Updating Chart: Installing a new VIP Companion seat 'B5' linked via 'B4' ---")
    seating_map["B4"].append("B5")
    seating_map["B5"] = ["B4"]  # Creating a bidirectional physical link
    
    updated_sweep = bfs(seating_map, ideal_seat)
    print(f"Updated Backup Seating Scan after provisioning Seat B5:")
    print(f"  {updated_sweep}")
    print("Notice how B5 correctly drops into the final position, mapping as a Tier 3 priority backup.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")
    
    # Edge Case 1: Safe handling of a booking request for a non-existent seat label
    invalid_seat = "Z99"
    print(f"1. Querying alternative recommendations for invalid seat code '{invalid_seat}':")
    missing_result = bfs(seating_map, invalid_seat)
    print(f"   Returned allocation recommendations: {missing_result}")
    print("   -> Explanation: System lookup boundaries confirm seat presence first, preventing crashes.")

    # Edge Case 2: Executing BFS across an isolated sub-graph (Air-Gapped Private VIP Box Balcony)
    print("\n2. Simulating an isolated VIP box configuration ('Box-A1' and 'Box-A2' share an isolated lounge):")
    seating_map["Box-A1"] = ["Box-A2"]
    seating_map["Box-A2"] = ["Box-A1"]
    
    isolated_result = bfs(seating_map, "Box-A1")
    print(f"   Recommendation loop initialized for isolated ticket zone 'Box-A1': {isolated_result}")
    print("   -> Explanation: BFS identifies the adjacent VIP seat but will never cross over to main rows")
    print("      because no geometric aisles or physical pathways bridge the balcony box to the lower level.")


if __name__ == "__main__":
    main()
