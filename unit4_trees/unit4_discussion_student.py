"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value (assigned altitude in feet) and 
        # initialize references to the left and right child nodes as None.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree with its root set to None.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion depends strictly on whether a value is smaller or larger 
        # than the current node because a BST maintains a strict order: 
        # lower flight altitudes go to the left subtree, and higher flight altitudes 
        # go to the right subtree. This maintains a structured, vertical flight stack
        # allowing Air Traffic Control to search or organize the airspace instantly.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base Case: If we reach an unassigned altitude level, clear to assign here.
        if node is None:
            return Node(value)

        # Handle duplicates: In aviation, two aircraft cannot hold the exact same altitude.
        if value == node.value:
            print(f"⚠️ ATC COLLISION WARNING: Flight level {value} ft is already occupied!")
            return node

        # Recursive step: Move down the flight stack based on altitude comparison.
        if value < node.value:
            # If the new altitude is lower, branch into the lower altitude subtree.
            node.left = self._insert_recursive(node.left, value)
        else:
            # If the new altitude is higher, branch into the higher altitude subtree.
            node.right = self._insert_recursive(node.right, value)

        # Return the unchanged node pointer to rebuild tree links.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST search is significantly more efficient than linear search for radar lookups. 
        # Instead of scanning through a flat list of every plane in the sky one by one, 
        # a BST allows the system to look at a node and instantly eliminate entire 
        # bands of airspace. If we are looking for a plane at 12,000 ft and the current 
        # node is 30,000 ft, we can completely ignore everything above 30,000 ft.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        # Base Cases: If the node is None, no aircraft is tracking at this altitude. 
        if node is None:
            return False
        
        # If the flight level matches, we have localized the target aircraft.
        if node.value == value:
            return True

        # Recursive Steps: Navigate up or down the airspace column.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # 1. Visit the left subtree (all lower altitude aircraft)
            self._inorder_recursive(node.left, values)
            
            # 2. Visit the current aircraft altitude
            values.append(node.value)
            
            # 3. Visit the right subtree (all higher altitude aircraft)
            self._inorder_recursive(node.right, values)

        # Why this produces sorted output:
        # An in-order traversal processes the leftmost (lowest altitude) nodes first, 
        # travels up through intermediate heights, and finishes with the rightmost 
        # (highest altitude) nodes. This natural path output gives the radar operator 
        # a perfectly sorted vertical stack of flights from closest to the ground to highest.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")
    
    # 1. Create a BST object.
    atc_radar = BST()
    
    # Real-world scenario: Active assigned flight altitudes (in feet) under radar control.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left and right subtrees.
    flight_altitudes = [30000, 15000, 37000, 10000, 22000, 34000, 41000]
    
    print(f"Logging active flight altitudes into ATC radar matrix: {flight_altitudes}")
    for altitude in flight_altitudes:
        atc_radar.insert(altitude)
        
    # 5. Explaining why a BST is efficient at reducing search space:
    # When initializing the airspace at 30,000 ft, it maps as our root.
    # Inserting a low-altitude regional flight at 15,000 ft eliminates the right side of the tree.
    # Inserting a high-altitude cruise liner at 37,000 ft eliminates the left side of the tree.
    # Branching decision rules automatically drop irrelevant airspace paths from calculation loops.
    print("Airspace monitoring system built! The data layout avoids brute-force linear table scans.")

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")
    
    # 1. & 2. Perform and display in-order traversal results
    vertical_flight_stack = atc_radar.inorder()
    print(f"Radar Vertical Altitude Stack (Lowest to Highest): {vertical_flight_stack}")
    print("Explanation: The traversal lists altitudes in sorted sequence because it completely processes")
    print("lower altitude branches before reporting the parent height, followed by higher levels.")

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    
    # 1. Search for at least two values that exist.
    exists_1 = 22000
    exists_2 = 34000
    print(f"Pinging active altitude {exists_1} ft: Aircraft detected? -> {atc_radar.search(exists_1)}")
    print(f"Pinging active altitude {exists_2} ft: Aircraft detected? -> {atc_radar.search(exists_2)}")
    
    # 2. Search for at least two values that do not exist.
    missing_1 = 12000
    missing_2 = 45000
    print(f"Pinging unassigned altitude {missing_1} ft: Aircraft detected? -> {atc_radar.search(missing_1)}")
    print(f"Pinging unassigned altitude {missing_2} ft: Aircraft detected? -> {atc_radar.search(missing_2)}")
    
    # 3. Use comments to clearly explain the results.
    # When looking for 22,000 ft, the tree checks 30k (goes left), checks 15k (goes right), and highlights it.
    # When looking for a non-existent flight layer at 45,000 ft, it tracks right past 30k, 37k, and 41k,
    # hits a clear corridor boundary (None), and returns False safely in exactly 4 targeted checks.

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")
    
    # Demonstrating Edge Case: Inserting a duplicate altitude slot assignment
    duplicate_altitude = 22000
    print(f"Attempting to route a new flight into an occupied level ({duplicate_altitude} ft)...")
    atc_radar.insert(duplicate_altitude)
    print("Radar inventory following duplicate verification:", atc_radar.inorder())
    print("-> Explanation: Our safety exception checks duplicate conditions and blocks entry processing,")
    print("   preventing corrupt tree splits and ensuring flight separation standards remain intact.")


if __name__ == "__main__":
    main()
