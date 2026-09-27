"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Internal data structure for the stack using a standard Python list.
        self.items = []

    def push(self, value):
        # LIFO Support: Items are appended to the *end* of the list.
        # This places them at the top of the stack, making the last added item 
        # the first one to be removed.
        self.items.append(value)

    def pop(self):
        # Empty-stack handling: Return None to avoid causing an IndexError.
        if self.is_empty():
            return None
        # Removes and returns the most recently added item (the top of the stack).
        return self.items.pop()

    def peek(self):
        # Returns the top value without removing it from the stack.
        # Useful for checking what is at the top of the pile.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack has no items inside it.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # Internal data structure for the queue using collections.deque.
        # Deque is highly optimized for O(1) appends and pops from both ends.
        self.items = deque()

    def enqueue(self, value):
        # FIFO Support: Items are added to the back (right end) of the queue.
        # They must wait for all items in front of them to be processed first.
        self.items.append(value)

    def dequeue(self):
        # Empty-queue handling: Return None to prevent crashing with an IndexError.
        if self.is_empty():
            return None
        # Removes and returns the value from the front (left end) of the queue.
        return self.items.popleft()

    def front(self):
        # Returns the value at the very front of the queue without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # Return True if the queue contains no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO (LIFO: Last-In, First-Out) ===")
    
    # 1. Create a Stack object.
    my_stack = Stack()
    
    # 6. Edge Case: peek() on an empty stack
    print(f"Edge Case - Peeking at an empty stack: {my_stack.peek()}")
    # 5. Edge Case: pop() on an empty stack
    print(f"Edge Case - Popping from an empty stack: {my_stack.pop()}")

    # 2. Add at least 4 values to the stack.
    print("\nPushing 4 values onto the stack...")
    for item in ["Item A", "Item B", "Item C", "Item D"]:
        my_stack.push(item)
        print(f" -> Pushed: {item} | Current Top: {my_stack.peek()}")

    # 4. Demonstrate LIFO behavior.
    print("\nPopping elements off the stack (LIFO verification):")
    while not my_stack.is_empty():
        popped_item = my_stack.pop()
        print(f" <- Popped: {popped_item}")

    # 7. Edge Case: Single item behavior verification
    print("\nEdge Case - Testing a single item stack:")
    single_stack = Stack()
    single_stack.push("Lone Item")
    print(f" Is stack empty after push? {single_stack.is_empty()}")
    print(f" Removing item: {single_stack.pop()}")
    print(f" Is stack empty after removal? {single_stack.is_empty()}")


    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO (FIFO: First-In, First-Out) ===")
    
    # 1. Create a Queue object.
    my_queue = Queue()
    
    # 6. Edge Case: front() on an empty queue
    print(f"Edge Case - Checking front of an empty queue: {my_queue.front()}")
    # 5. Edge Case: dequeue() on an empty queue
    print(f"Edge Case - Dequeuing from an empty queue: {my_queue.dequeue()}")

    # 2. Add at least 4 values to the queue.
    print("\nEnqueuing 4 values into the queue...")
    for person in ["Client 1", "Client 2", "Client 3", "Client 4"]:
        my_queue.enqueue(person)
        print(f" -> Enqueued: {person} | Next up (Front): {my_queue.front()}")

    # 4. Demonstrate FIFO behavior.
    print("\nDequeuing elements from the queue (FIFO verification):")
    while not my_queue.is_empty():
        dequeued_item = my_queue.dequeue()
        print(f" <- Dequeued: {dequeued_item}")

    # 7. Edge Case: Single item behavior verification
    print("\nEdge Case - Testing a single item queue:")
    single_queue = Queue()
    single_queue.enqueue("Sole Client")
    print(f" Is queue empty after enqueue? {single_queue.is_empty()}")
    print(f" Removing item: {single_queue.dequeue()}")
    print(f" Is queue empty after removal? {single_queue.is_empty()}")


    # ===================================================
    # 6. REAL-WORLD SCENARIO: The Personal Shopper
    # ===================================================
    print("\n=== REAL-WORLD SCENARIO: Luxury Personal Shopper System ===")
    print("Scenario: A personal shopper manages client appointments in a strict timeline (Queue).")
    print("          Meanwhile, they stack selected clothing items in a physical cart (Stack).")
    
    appointment_line = Queue()
    shopping_cart = Stack()
    
    # FIFO Component: Clients booking consultations
    print("\n[Booking System: Clients join the waiting line chronologically]")
    clients = ["Alice (VIP)", "Bob", "Charlie", "Diana"]
    for client in clients:
        appointment_line.enqueue(client)
        print(f" Booking Appt -> {client} is waiting for their custom shopping session.")
        
    print("\n[Shopper Floor: Starting day's consultations]")
    print(f" The first client scheduled to be seen is: {appointment_line.front()}")
    
    # Shopper helps the first client by selecting garments
    current_client = appointment_line.dequeue()
    print(f" Now serving: {current_client}")
    
    # LIFO Component: Piling items neatly in the apparel container
    print(f"\n[Boutique Showroom: Gathering garments for {current_client}]")
    garments = ["Silk Blouse (Bottom of stack)", "Designer Denim (Middle)", "Velvet Blazer (Top of stack)"]
    for garment in garments:
        shopping_cart.push(garment)
        print(f" Placed in physical cart -> {garment}")
        
    # Fitting Room: Removing items from the top of the physical pile
    print(f"\n[Fitting Room: Unloading the cart for {current_client} to try on (LIFO)]")
    print(f" Quick check: What is on top of the pile right now? -> {shopping_cart.peek()}")
    
    while not shopping_cart.is_empty():
        print(f" Pulled off top of pile to try on <- {shopping_cart.pop()}")
        
    # Shopper moves to the next client in line chronologically
    print(f"\n[Shopper Floor: Next Appointment]")
    print(f" Finished with {current_client}. Now serving next in line: {appointment_line.dequeue()}")


if __name__ == "__main__":
    main()
