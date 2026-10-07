"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:
This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

SCENARIO: Live Gaming Leaderboard Tracker
We are tracking player match scores. To rank players correctly, 
we need to sort the data numerically.
"""

import time


def bubble_sort(lst):
    """
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list to preserve original data.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    """
    # Create a copy so we don't destroy the user's original raw list data
    arr = list(lst)
    n = len(arr)
    
    # Outer loop visits each element to ensure complete passes
    for i in range(n):
        # Tracking variable to optimize: if no swaps happen, it's already sorted
        swapped = False
        
        # Inner loop checks adjacent pairs; elements past (n-i-1) are already sorted bubbles
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap them if they are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Optimization: Early exit if a full pass required zero changes
        if not swapped:
            break
            
    # TIME COMPLEXITY ANALYSIS: O(n^2)
    # Bubble Sort uses nested loops. In the worst-case scenario (like a reverse list),
    # it must perform comparisons for every pair, scaling quadratically.
    return arr


def merge_sort(lst):
    """
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    """
    # Base Case: A list of 0 or 1 elements is already sorted by default
    if len(lst) <= 1:
        return lst

    # Find the midpoint index of the list
    mid = len(lst) // 2
    
    # DIVIDE: Split the list into left and right sub-arrays and sort them recursively
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    
    # CONQUER & MERGE: Stitch the two sorted halves back together seamlessly
    return merge(left_half, right_half)


def merge(left, right):
    """
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    """
    result = []
    i = 0  # Pointer for left list
    j = 0  # Pointer for right list
    
    # Loop runs while there are items remaining in both sections
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Append any leftover stray items that remain in either array
    result.extend(left[i:])
    result.extend(right[j:])
    
    # TIME COMPLEXITY ANALYSIS: O(n log n)
    # The dividing step breaks data down logarithmically (log n). The merge step 
    # weaves everything back together linearly (n). Combined, this gives Merge Sort
    # a highly efficient, reliable runtime speed of O(n log n) even on massive lists.
    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ==========================================
    # DATASET #1: Standard Daily Match Scores
    # ==========================================
    print("\n=== DATASET #1 (Daily Leaderboard Scores) ===")
    # 1. Create an unsorted list containing at least 7 values.
    leaderboard_v1 = [450, 120, 890, 310, 550, 200, 760, 105]
    
    # 2. Display the original list.
    print(f"Original Unsorted Leaderboard: {leaderboard_v1}")
    
    # 3 & 4. Sort the list using both approaches
    bubble_res_1 = bubble_sort(leaderboard_v1)
    merge_res_1 = merge_sort(leaderboard_v1)
    
    # 5. Clearly label and display all results.
    print(f"  Bubble Sort Result: {bubble_res_1}")
    print(f"  Merge Sort Result:  {merge_res_1}")


    # ==========================================
    # DATASET #2: High Scale Performance Test
    # ==========================================
    print("\n=== DATASET #2 (Large Global Leaderboard Scalability) ===")
    # 1 & 2. Create a larger dataset with different values (5,000 players countdown)
    large_leaderboard = list(range(5000, 0, -1))
    print(f"Total Scaled Tournament Records: {len(large_leaderboard)} entries (Worst Case: Reverse Order)")

    # 3. Benchmark Bubble Sort
    start_time = time.perf_counter()
    bubble_res_2 = bubble_sort(large_leaderboard)
    end_time = time.perf_counter()
    bubble_duration = end_time - start_time
    print(f"  Bubble Sort process duration: {bubble_duration:.5f} seconds.")

    # 3. Benchmark Merge Sort
    start_time = time.perf_counter()
    merge_res_2 = merge_sort(large_leaderboard)
    end_time = time.perf_counter()
    merge_duration = end_time - start_time
    print(f"  Merge Sort process duration:  {merge_duration:.5f} seconds.")
    
    # 4. Performance Comparison Explanation:
    # On small scales (like Dataset 1), both algorithms complete almost instantly. 
    # However, when running a tournament ledger of 5,000 items in worst-case reverse order,
    # Bubble Sort experiences an exponential slowdown due to its O(n^2) nested loop architecture. 
    # Meanwhile, Merge Sort's divide-and-conquer strategy handles the 5,000 items seamlessly, 
    # finishing in a microscopic fraction of the time.


    # ==========================================
    # EDGE CASE TESTS
    # ==========================================
    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Players with identical game scores (Duplicates)
    duplicate_scores = [350, 120, 350, 990, 120, 500]
    print(f"1. Duplicate Player Scores Test:\n   Input:  {duplicate_scores}\n   Output: {merge_sort(duplicate_scores)}")
    # Why it works: The conditional rule `left[i] <= right[j]` ensures that when two values 
    # match, the item from the left slice retains priority placement. This preserves duplicate positions 
    # safely without dropping values or spinning into error states.

    # Edge Case 2: Empty Lobby Leaderboard (Empty List)
    empty_lobby = []
    print(f"\n2. Empty Lobby Tracking Test:\n   Input:  {empty_lobby}\n   Output: {merge_sort(empty_lobby)}")
    # Why it works: The recursion base check condition `len(lst) <= 1` flags true immediately. 
    # The functions safely return the blank structure without executing further loops, bypassing 
    # any accidental OutOfBounds indexing exceptions.


if __name__ == "__main__":
    main()
