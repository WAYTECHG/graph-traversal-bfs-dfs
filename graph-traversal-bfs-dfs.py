"""When running the code, minimize display is needed to see the proper adjacency matrix representation"""

# Import necessary libraries
from collections import deque  # For implementing BFS using a queue
import pandas as pd  # For handling adjacency matrix and tabular data
from tabulate import tabulate  # For pretty printing the adjacency matrix

# Define the connections as an adjacency list (with costs)
connections = {
    "KLIA": [["TBS", 10], ["KLCC", 12], ["Melaka", 50]],
    "TBS": [["KLIA", 10], ["KLCC", 5], ["Melaka", 60]],
    "KLCC": [["KLIA", 12], ["TBS", 5], ["Aquaria KLCC", 2], ["Batu Caves", 30]],
    "Aquaria KLCC": [["KLCC", 2]],
    "Batu Caves": [["KLCC", 30], ["Colmar Malaysia", 10], ["Genting Highland", 15]],
    "Colmar Malaysia": [["Batu Caves", 10], ["Fraser's Hill", 13]],
    "Fraser's Hill": [["Colmar Malaysia", 13], ["Genting Highland", 15]],
    "Genting Highland": [["Fraser's Hill", 15], ["Cameron Highland", 40], ["Lost World of Tambun", 60], ["Batu Caves", 15]],
    "Cameron Highland": [["Genting Highland", 40], ["Lost World of Tambun", 15]],
    "Lost World of Tambun": [["Genting Highland", 60], ["Cameron Highland", 15], ["Penang", 10]],
    "Penang": [["Lost World of Tambun", 10]],
    "Melaka": [["KLIA", 50], ["TBS", 60], ["Legoland", 50]],
    "Legoland": [["Melaka", 50]]
}

# Define the adjacency matrix representation of the graph
graph = [
    ["INF", 10, 12, "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 50, "INF"],
    [10, "INF", 5, "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 60, "INF"],
    [12, 5, "INF", 2, 30, "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF"],
    ["INF", "INF", 2, "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF"],
    ["INF", "INF", 30, "INF", "INF", 10, "INF", 15, "INF", "INF", "INF", "INF", "INF"],
    ["INF", "INF", "INF", "INF", 10, "INF", 13, "INF", "INF", "INF", "INF", "INF", "INF"],
    ["INF", "INF", "INF", "INF", "INF", 13, "INF", 15, "INF", "INF", "INF", "INF", "INF"],
    ["INF", "INF", "INF", "INF", "INF", "INF", 15, "INF", 40, 60, "INF", "INF", "INF"],
    ["INF", "INF", "INF", "INF", "INF", "INF", "INF", 40, "INF", 15, "INF", "INF", "INF"],
    ["INF", "INF", "INF", "INF", "INF", "INF", "INF", 60, 15, "INF", 10, "INF", "INF"],
    ["INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 10, "INF", "INF", "INF"],
    [50, 60, "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 50],
    ["INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", "INF", 50, "INF"],
]

# Define the list of places corresponding to the graph's rows/columns
places = [
    "KLIA", "TBS", "KLCC", "Aquaria KLCC", "Batu Caves", "Colmar Malaysia", "Fraser's Hill", "Genting Highland",
    "Cameron Highland", "Lost World of Tambun", "Penang", "Melaka", "Legoland"
]

# Create a pandas DataFrame for the adjacency matrix
data = pd.DataFrame(graph, index=places, columns=places)

# Print the adjacency matrix in a formatted table
print("Adjacency Matrix:")
print(tabulate(data, headers="keys", tablefmt="grid", showindex=True))
print("\n")

# Function to perform Depth-First Search (DFS)
def dfs(start):
    visited = set()  # To track visited nodes
    sequence = []  # To record the DFS sequence

    # Helper function for recursive DFS
    def dfs_recursive(node):
        visited.add(node)  # Mark the current node as visited
        sequence.append(node)  # Add to sequence

        # Sort neighbors by weight (smallest to largest) before exploring
        neighbors = connections.get(node, [])
        sorted_neighbors = sorted(neighbors, key=lambda x: x[1])  # Sort by weight

        for neighbor, _ in sorted_neighbors:  # Explore sorted neighbors
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)  # Start DFS from the initial node
    print("\nDFS Traversal Sequence:")
    print(", ".join(sequence))  # Print the DFS traversal sequence


# Function to perform Breadth-First Search (BFS)
def bfs(start):
    visited = set()  # To track visited nodes
    queue = deque([start])  # Initialize queue with the start node
    visited.add(start)  # Mark the start node as visited
    sequence = []  # To record the BFS sequence

    while queue:  # Loop until the queue is empty
        current = queue.popleft()  # Dequeue the next node
        sequence.append(current)  # Add to sequence

        # Sort neighbors by weight (smallest to largest)
        neighbors = connections.get(current, [])
        sorted_neighbors = sorted(neighbors, key=lambda x: x[1])  # Sort by weight

        for neighbor, _ in sorted_neighbors:  # Explore sorted neighbors
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                queue.append(neighbor)  # Enqueue the neighbor

    print("\nBFS Traversal Sequence:")
    print(", ".join(sequence))  # Print the BFS traversal sequence

# Function to validate user input
def get_valid_input(prompt, options):
    while True:
        try:
            user_input = input(prompt)  # Get input from user
            if user_input.isdigit() and int(user_input) in options:  # Check validity
                return int(user_input)
            print("Invalid input. Please enter a valid option.")
        except Exception:
            print("Error in input. Try again.")

# DFS with user preference
def user_preference_dfs(start):
    visited = set()  # Track visited nodes
    print(f"You are at {start}.")  # Notify user of the current node
    visited.add(start)
    stack = [start]  # Use a stack for DFS
    sequence = [start]  # Record traversal sequence

    while stack:  # Loop until stack is empty
        current = stack[-1]  # Peek at the top of the stack
        options = [(neighbor, cost) for neighbor, cost in connections.get(current, []) if neighbor not in visited]

        if options:  # If there are unvisited neighbors
            print(f"\nAfter visiting {current}, choose your next destination:")
            for idx, (option, cost) in enumerate(options, 1):
                print(f"{idx}. {option} ({cost})")

            choice = get_valid_input("Input your choice: ", range(1, len(options) + 1)) - 1
            next_place, next_cost = options[choice]
            print(f"Visiting {next_place}.")  # Show user the selected path
            visited.add(next_place)
            stack.append(next_place)  # Push chosen node to stack
            sequence.append(next_place)
        else:  # Backtrack if no unvisited neighbors
            stack.pop()

    print("\nFinal DFS User Preference Sequence:")
    print(", ".join(sequence))

# BFS with user preference
def user_preference_bfs(start):
    visited = set()  # Track visited nodes
    queue = deque([start])  # Initialize BFS queue
    visited.add(start)
    traverse_sequence = []  # Record traversal sequence

    print(f"You are at {start}.")  # Notify user of the current node

    while queue:  # Loop until queue is empty
        current = queue[0]  # Get the current node without removing
        neighbors = [(neighbor, cost) for neighbor, cost in connections.get(current, []) if neighbor not in visited]

        if neighbors:  # If there are unvisited neighbors
            print(f"\nAfter visiting {current}, choose your next destination:")
            for idx, (neighbor, cost) in enumerate(neighbors, 1):
                print(f"{idx}. {neighbor} ({cost})")

            choice = get_valid_input("Enter your choice: ", range(1, len(neighbors) + 1)) - 1
            chosen_place, chosen_cost = neighbors.pop(choice)
            print(f"Visiting {chosen_place}.")  # Show user the selected path
            visited.add(chosen_place)
            queue.append(chosen_place)  # Enqueue chosen node
        else:  # Remove current node from the queue if no neighbors
            queue.popleft()
            traverse_sequence.append(current)

    print("\nFinal BFS Traverse Sequence:")
    print(", ".join(traverse_sequence))

# Main function to handle user interactions
def main():
    while True:  # Loop to keep the program running
        print("\nWhich method do you want to use:")
        print("1- DFS sequence (Basic)")
        print("2- BFS sequence (Basic)")
        print("3- DFS sequence (User preference)")
        print("4- BFS sequence (User preference)")
        print("5- Exit")

        choice = get_valid_input("User choice: ", range(1, 6))  # Get user choice

        if choice == 5:  # Exit condition
            print("Exiting the program...\nGoodbye!")
            break

        print("\nPlease select your start point:")
        for idx, place in enumerate(places):  # Display available starting points
            print(f"{idx}. {place}")

        start_choice = get_valid_input("User Choice: ", range(len(places)))  # Get start point
        start = places[start_choice]

        if choice == 1:
            print("\nDFS Basic Traversal:")
            dfs(start)
        elif choice == 2:
            print("\nBFS Basic Traversal:")
            bfs(start)
        elif choice == 3:
            print("\nDFS Traversal (User Preference):")
            user_preference_dfs(start)
        elif choice == 4:
            print("\nBFS Traversal (User Preference):")
            user_preference_bfs(start)

# Entry point of the program
if __name__ == "__main__":
    main()
