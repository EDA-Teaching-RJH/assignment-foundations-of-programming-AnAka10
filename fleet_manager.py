# fleet_manager.py

# --- 1. INITIALIZE DATABASE (4 Marks) ---
def init_database():
    """
    Returns 4 parallel lists pre-populated with 5 Star Trek characters.
    """
    names = ["Jean-Luc Picard", "William Riker", "Data", "Geordi La Forge", "Worf"]
    ranks = ["Captain", "Commander", "Lt. Commander", "Lt. Commander", "Lieutenant"]
    divs  = ["Command", "Command", "Operations", "Operations", "Security"]
    ids   = ["1001", "1002", "1003", "1004", "1005"]
    
    return names, ranks, divs, ids

# --- 2. DISPLAY MENU (4 Marks) ---
def display_menu():
    """
    Prints the options and returns the user's choice.
    """
    print("\n--- FLEET MANAGEMENT SYSTEM ---")
    print("1. View Crew Roster")
    print("2. Add Crew Member")
    print("3. Remove Crew Member")
    print("4. Update Rank")
    print("5. Search Crew")
    print("6. Filter by Division")
    print("7. Payroll Analysis")
    print("8. Exit")
    
    choice = input("Select an option: ")
    return choice

# --- 6. DISPLAY ROSTER (4 Marks) ---
def display_roster(names, ranks, divs, ids):
    """
    Iterates through the lists and prints a formatted table.
    """
    print(f"{'ID':<8} | {'Name':<20} | {'Rank':<15} | {'Division'}")
    print("-" * 60)
    
    for i in range(len(names)):
        print(f"{ids[i]:<8} | {names[i]:<20} | {ranks[i]:<15} | {divs[i]}")

# --- MAIN PROGRAM LOOP ---
def main():
    # 1. Initialize the parallel lists
    names, ranks, divs, ids = init_database()
    
    print("System Booting...")

    while True:
        # 2. Show menu and get choice
        choice = display_menu()

        if choice == "1":
            display_roster(names, ranks, divs, ids)
            
        elif choice == "8":
            print("Exiting System.")
            break
            
        else:
            print("Feature coming soon...")

# Run the program
if __name__ == "__main__":
    main()