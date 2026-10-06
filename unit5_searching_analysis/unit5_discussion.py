"""
===================================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (E-COMMERCE SYSTEM SCENARIO)
===================================================================

SCENARIO OVERVIEW:
This program simulates an e-commerce product search system.
Products are indexed and strictly sorted by their unique Product ID (SKU).
- Linear Search mimics scanning a chaotic, unsorted checkout cart.
- Binary Search mimics searching a highly optimized, indexed warehouse database.
"""

import time


def linear_search(catalog, target_sku):
    """
    Implements a linear search algorithm to find a product SKU.

    Requirements:
    - Scans the catalog from the first item to the last item.
    - Returns the index if found, or -1 if the product doesn't exist.
    
    TIME COMPLEXITY ANALYSIS: O(n)
    Linear search checks every single index sequentially. If a customer is looking
    for a rare item at the very bottom of the page, or an item that is entirely 
    out of stock, the algorithm must perform 'n' comparisons. Because execution time
    grows in direct, 1-to-1 proportion with catalog size, its complexity is O(n).
    """
    for i in range(len(catalog)):
        if catalog[i] == target_sku:
            return i
    return -1


def binary_search(catalog, target_sku):
    """
    Implements a binary search algorithm to pinpoint a product SKU.

    Requirements:
    - Assumes the catalog array is already sorted numerically by SKU.
    - Continuously cuts the active database search space in half.
    
    HOW EACH ITERATION REDUCES SEARCH SPACE: O(log n)
    Each loop iteration looks at the middle element of the current inventory segment.
    If the target SKU is smaller than the middle SKU, the entire upper half of the 
    catalog is discarded. If it is larger, the lower half is discarded. By eliminating 
    50% of the remaining products on every single step, the algorithm operates on a 
    logarithmic time scale, making it incredibly scalable for massive marketplaces.
    """
    low = 0
    high = len(catalog) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if catalog[mid] == target_sku:
            return mid  # Product found!
        elif catalog[mid] > target_sku:
            high = mid - 1  # Target is in the lower-numbered SKU half
        else:
            low = mid + 1   # Target is in the higher-numbered SKU half
            
    return -1  # Product is not in stock


def main():
    print("=== E-COMMERCE PRODUCT DATABASE SYSTEM ===")

    # ==========================================
    # 1. SMALL DATASET TEST (A Customer Cart)
    # ==========================================
    print("\n=== 1. SMALL DATASET TEST (Active Shopping Cart) ===")
    # A small shopping cart containing 6 items sorted by ID
    cart_skus = [1002, 1005, 1012, 1022, 1045, 1099]
    print(f"Current Cart Items (SKUs): {cart_skus}")

    # Case A: Search for an item a customer knows is in their cart
    target_item = 1022
    print(f"\nSearching for existing item SKU ({target_item}):")
    print(f"  Linear Search Cart Index: {linear_search(cart_skus, target_item)}")
    print(f"  Binary Search Cart Index: {binary_search(cart_skus, target_item)}")

    # Case B: Search for a promo item not in the cart
    missing_item = 1050
    print(f"\nSearching for missing item SKU ({missing_item}):")
    print(f"  Linear Search Cart Index: {linear_search(cart_skus, missing_item)}")
    print(f"  Binary Search Cart Index: {binary_search(cart_skus, missing_item)}")
    
    # PERFORMANCE ANALYSIS (Small Scale):
    # For a small cart of 6 items, both algorithms finish instantly. The architectural 
    # overhead of setting up low, high, and middle pointers in Binary Search provides 
    # no practical advantage over simply checking all 6 items one-by-one.


    # ==========================================
    # 2. LARGE DATASET TEST (Global Inventory)
    # ==========================================
    print("\n=== 2. LARGE DATASET TEST (Warehouse Central Catalog) ===")
    # Simulating a massive online warehouse catalog containing 500,000 items
    warehouse_catalog = list(range(100000, 600000)) 
    
    # Looking for a rare item placed right at the end of the inventory database
    rare_product_sku = 599998 
    
    print(f"Total Warehouse Catalog Size: {len(warehouse_catalog)} items")
    print(f"Looking up SKU: {rare_product_sku}")

    # Testing Linear Search on Marketplace Database
    start_time = time.perf_counter()
    lin_res = linear_search(warehouse_catalog, rare_product_sku)
    end_time = time.perf_counter()
    linear_duration = end_time - start_time
    print(f"  Linear Search processed catalog in: {linear_duration:.6f} seconds (Index: {lin_res})")

    # Testing Binary Search on Marketplace Database
    start_time = time.perf_counter()
    bin_res = binary_search(warehouse_catalog, rare_product_sku)
    end_time = time.perf_counter()
    binary_duration = end_time - start_time
    print(f"  Binary Search processed catalog in: {binary_duration:.6f} seconds (Index: {bin_res})")

    # PERFORMANCE ANALYSIS (Large Scale):
    # As our inventory scales up to half a million products, Linear Search chokes because
    # it performs nearly 500,000 comparisons step-by-step. Binary Search finishes in a 
    # fraction of a millisecond. While Linear Search scales linearly, Binary Search cuts 
    # 500,000 items down to 1 in roughly 19 steps (2^19 = 524,288).


    # ==========================================
    # 3. EDGE CASE TESTS
    # ==========================================
    print("\n=== 3. EDGE CASE TESTS ===")

    # Edge Case 1: Empty Shopping Cart (No items added yet)
    empty_cart = []
    print(f"Edge Case 1 - Empty Cart Lookup: Result Index = {binary_search(empty_cart, 1002)}")
    # Why it works: The loop boundary condition 'low <= high' (0 <= -1) safely fails 
    # immediately, avoiding a crash and correctly returning -1 (Item Not Found).

    # Edge Case 2: Only 1 Single Item in Clearance Section
    clearance_item = [7777]
    print(f"Edge Case 2a - Single Item (In Stock Match): Result Index = {binary_search(clearance_item, 7777)}")
    print(f"Edge Case 2b - Single Item (Out of Stock):  Result Index = {binary_search(clearance_item, 1111)}")
    # Why it works: If the SKU matches, mid calculation (0+0)//2 equals 0, returning instantly.
    # If it fails, high or low shifts out of bounds, naturally terminating the loop safely.

    # Edge Case 3: Items at Absolute First and Last Positions of the Catalog Display
    boundary_catalog = [1001, 2002, 3003, 4004, 5005]
    print(f"Edge Case 3a - First Item in Catalog (1001): Result Index = {binary_search(boundary_catalog, 1001)}")
    print(f"Edge Case 3b - Last Item in Catalog (5005):  Result Index = {binary_search(boundary_catalog, 5005)}")
    # Why it works: Linear search finds the first item on step #1, but performs worst-case 
    # bounds for the last. Binary search easily shifts its boundary index pointers step-by-step 
    # until high/low close in perfectly on the exact outer index positions without bleeding over.


if __name__ == "__main__":
    main()
