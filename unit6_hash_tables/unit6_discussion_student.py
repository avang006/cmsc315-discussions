"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================================
    # CREATE A HASH TABLE (Authenticator Sessions)
    # ===============================================
    print("\n=== INSERT OPERATIONS ===")
    
    # 1. Create an empty dictionary.
    session_tokens = {}
    
    # 2. Add at least 5 key-value pairs (Username -> Active Session Token)
    session_tokens["alex_dev"] = "tok_8f3a1b"
    session_tokens["clara_p"] = "tok_4c9e2d"
    session_tokens["marcus_k"] = "tok_7a1b9e"
    session_tokens["sarah_w"] = "tok_3d8f2c"
    session_tokens["tech_lead"] = "tok_9e5b6a"

    # 3. Add comments explaining how a dictionary behaves like a hash table.
    # UNDERSTANDING HASHING CONCEPTS:
    # A Python dictionary maps keys to values behind the scenes using a Hash Table. 
    # When we write `session_tokens["alex_dev"] = "tok_8f3a1b"`, Python runs the string key 
    # through an internal "hash function" to generate a unique integer index. 
    # That index tells the computer exactly where to store the token value in memory. 
    # This design allows for almost instant retrieval, insertion, and deletion.

    # 4. Display the contents of the dictionary.
    print(f"Active Session Database:\n{session_tokens}")


    # ===============================================
    # LOOKUP OPERATIONS
    # ===============================================
    print("\n=== LOOKUP OPERATIONS ===")
    
    # 1 & 2. Retrieve at least two existing keys and display results.
    user_1 = "clara_p"
    user_2 = "tech_lead"
    
    token_1 = session_tokens[user_1]
    token_2 = session_tokens[user_2]
    
    print(f"Verifying access for '{user_1}': Found Session Token -> {token_1}")
    print(f"Verifying access for '{user_2}': Found Session Token -> {token_2}")

    # 3. Add meaningful comments to explain how the lookup works.
    # RETRIEVING VALUES EFFICIENTLY:
    # Unlike a linear array or list, Python doesn't scan the entire dictionary 
    # row-by-row to find a key. It instantly hashes the key (e.g., 'clara_p') to figure out 
    # its exact index location. This gives lookups an ultra-fast constant time complexity 
    # of O(1), making it perfect for high-speed security verification systems.


    # ===============================================
    # UPDATE OPERATIONS
    # ===============================================
    print("\n=== UPDATE OPERATIONS ===")
    
    update_user = "marcus_k"
    
    # 2. Display the dictionary before the update.
    print(f"Before token refresh for '{update_user}': {session_tokens[update_user]}")
    
    # 1. Update the value associated with an existing key.
    session_tokens[update_user] = "tok_NEW_999"
    
    # 2. Display the dictionary after the update.
    print(f"After token refresh for  '{update_user}': {session_tokens[update_user]}")

    # 3. Use comments to explain what happens when an existing key is assigned a new value.
    # UPDATING EXISTING VALUES:
    # Dictionary keys must always be unique. If you assign a new value to a key that 
    # already exists in the dictionary, Python hashes the key, goes to its existing 
    # memory address, and overwrites the old value. It updates in place without 
    # spawning a duplicate entry.


    # ===============================================
    # DELETE OPERATIONS
    # ===============================================
    print("\n=== DELETE OPERATIONS ===")
    
    delete_user = "sarah_w"
    
    # 2. Display the dictionary before deletion.
    print(f"Database before log out ({delete_user}):\n  {session_tokens}")
    
    # 1. Delete at least one key-value pair.
    del session_tokens[delete_user]
    
    # 2. Display the dictionary after deletion.
    print(f"Database after log out ({delete_user}):\n  {session_tokens}")

    # 3. Use comments to explain what happens when a key is removed.
    # REMOVING ENTRIES:
    # The `del` statement finds the memory bucket corresponding to the hashed key 
    # and completely clears out both the key and its value block. The memory space 
    # is freed up, and subsequent lookups for that key will no longer succeed.


    # ===============================================
    # EDGE CASES
    # ===============================================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Looking up a missing key (Unauthorized/Expired User)
    missing_user = "hacker_99"
    print(f"Attempting lookup for unverified user: '{missing_user}'")
    
    # Using the standard approach `session_tokens[missing_user]` would throw a fatal KeyError.
    # Instead, we use the safe `.get()` method to handle missing data gracefully.
    safe_lookup = session_tokens.get(missing_user, "ACCESS_DENIED: Token Expired or Invalid")
    print(f"  System Response: {safe_lookup}")

    # Edge Case 2: Safely deleting a missing key
    print(f"\nAttempting to safely delete non-existent user: '{missing_user}'")
    
    # Running `del session_tokens['hacker_99']` would crash our app with a KeyError.
    # To delete safely, we use the `.pop()` method with a default fallback parameter.
    removed_token = session_tokens.pop(missing_user, None)
    
    if removed_token is None:
        print(f"  Clean Exit: User '{missing_user}' wasn't in the system. Nothing to delete.")
    else:
        print(f"  Removed token: {removed_token}")


if __name__ == "__main__":
    main()
