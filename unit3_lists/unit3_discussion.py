"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

      Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Use the built-in insert operation to mutate the dynamic array
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Guard check: Validate that the index exists (handles positive and negative bounds)
    if index < -len(lst) or index >= len(lst):
        return None  # Return None safely if the index is invalid
        
    # Memory Shift: All items to the right of 'index' shift one slot left to fill the gap
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Sequentially scan the list using its indices
    for i in range(len(lst)):
        if lst[i] == value:
            return i  # Return the index immediately if found
            
    return -1  # Return -1 if the value is not found after a complete scan


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")
    
    # 1. Create a playlist containing several track values
    playlist = ["Midnight City", "Starlight", "Blinding Lights"]
    
    # 2. Display the original list
    print(f"Original Playlist Queue: {playlist}")

    # 3 & 4. Test insertions and display results after each step:
    
    # - At the beginning: Worst-case O(n) performance due to shifting the whole list right
    insert_at(playlist, 0, "Bohemian Rhapsody")
    print(f"Inserted at Beginning (Play Next - Index 0) : {playlist}")

    # - In the middle: Average-case O(n) performance due to shifting trailing elements
    insert_at(playlist, 2, "Hotel California")
    print(f"Inserted in Middle    (Custom Drop - Index 2): {playlist}")

    # - At the end: Best-case O(1) performance as no items need to shift memory spaces
    insert_at(playlist, len(playlist), "Stayin' Alive")
    print(f"Inserted at End       (Queue Track - Index {len(playlist)-1}): {playlist}")


    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")
    print(f"Current Playlist State: {playlist}")

    # 1, 2 & 3. Delete items, display values, and print updated states:
    
    # - From the beginning: O(n) cost. The current song finishes, all remaining tracks slide left.
    track_front = delete_at(playlist, 0)
    print(f"Removed from Beginning : '{track_front}'")
    print(f"Updated Playlist State : {playlist}")

    # - From the middle: O(n) cost. A track is removed from the queue, items behind it slide left.
    track_mid = delete_at(playlist, 1)
    print(f"\nRemoved from Middle    : '{track_mid}'")
    print(f"Updated Playlist State : {playlist}")

    # - From the end: O(1) cost. The last track is removed with zero data relocation.
    track_end = delete_at(playlist, len(playlist) - 1)
    print(f"\nRemoved from End       : '{track_end}'")
    print(f"Updated Playlist State : {playlist}")


    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")
    print(f"Current Target Catalog: {playlist}")

    # 1 & 3. Search for a value that exists and display results
    search_target_1 = "Blinding Lights"
    idx_1 = search_value(playlist, search_target_1)
    print(f"Searching for '{search_target_1}': Found at index position {idx_1}")

    # 2 & 3. Search for a value that does not exist and display results
    search_target_2 = "Beat It"
    idx_2 = search_value(playlist, search_target_2)
    print(f"Searching for '{search_target_2}': Not found, system returned {idx_2}")


    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using an invalid index out of bounds
    invalid_index = 99
    print(f"Attempting track deletion at out-of-bounds index {invalid_index}...")
    edge_del_result = delete_at(playlist, invalid_index)
    print(f"Result: {edge_del_result} (System safely returned None instead of throwing a fatal exception)")

    # Edge Case 2: Insert into a completely empty collection
    empty_playlist = []
    print(f"\nInitial Empty Playlist Queue: {empty_playlist}")
    insert_at(empty_playlist, 0, "First Track Initializer")
    print(f"Result after insertion into index 0: {empty_playlist}")


if __name__ == "__main__":
    main()
