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






# --- 3. ADD MEMBER (4 Marks) ---
def add_member(names, ranks, divs, ids):
    print("\n--- Add New Officer ---")
    new_id = input("Enter new ID: ")
    
    # Validation: Check if ID is unique
    if new_id in ids:
        print("Error: That ID already exists.")
        return # Stop the function here
        
    new_name = input("Enter Name: ")
    new_rank = input("Enter Rank: ")
    
    # Validation: Check for valid TNG rank
    valid_ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Ensign"]
    if new_rank not in valid_ranks:
        print("Error: Invalid Rank. Must be standard Starfleet rank.")
        return

    new_div = input("Enter Division: ")

    # Append to ALL 4 lists to keep them parallel
    ids.append(new_id)
    names.append(new_name)
    ranks.append(new_rank)
    divs.append(new_div)
    print("Officer added to database.")


# --- 4. REMOVE MEMBER (4 Marks) ---
def remove_member(names, ranks, divs, ids):
    print("\n--- Remove Officer ---")
    target_id = input("Enter ID to remove: ")
    
    if target_id in ids:
        # Find the index where this ID lives
        idx = ids.index(target_id)
        
        # Remove that index from ALL lists
        ids.pop(idx)
        names.pop(idx)
        ranks.pop(idx)
        divs.pop(idx)
        print("Officer removed.")
    else:
        print("Error: ID not found.")


# --- 5. UPDATE RANK (4 Marks) ---
def update_rank(names, ranks, ids):
    print("\n--- Update Rank ---")
    target_id = input("Enter ID to update: ")
    
    if target_id in ids:
        idx = ids.index(target_id)
        print(f"Current Rank for {names[idx]}: {ranks[idx]}")
        
        new_rank = input("Enter new rank: ")
        ranks[idx] = new_rank # Update only the rank list
        print("Rank updated.")
    else:
        print("Error: ID not found.")


        # --- 7. SEARCH CREW (4 Marks) ---
def search_crew(names, ranks, divs, ids):
    term = input("Enter search term (name): ").lower()
    print("\n--- Search Results ---")
    found = False
    
    for i in range(len(names)):
        if term in names[i].lower():
            print(f"Found: {names[i]} | Rank: {ranks[i]} | ID: {ids[i]}")
            found = True
            
    if not found:
        print("No matches found.")

# --- 8. FILTER BY DIVISION (4 Marks) ---
def filter_by_division(names, divs):
    target_div = input("Enter Division (Command, Operations, Security): ")
    print(f"\n--- {target_div} Division ---")
    
    found = False
    for i in range(len(divs)):
        if divs[i] == target_div:
            print(f"- {names[i]}")
            found = True
            
    if not found:
        print("No officers found in that division.")

# --- 9. CALCULATE PAYROLL (4 Marks) ---
def calculate_payroll(ranks):
    total_cost = 0
    
    for rank in ranks:
        if rank == "Captain":
            total_cost += 1000
        elif rank == "Commander":
            total_cost += 800
        elif rank == "Lt. Commander":
            total_cost += 600
        elif rank == "Lieutenant":
            total_cost += 400
        elif rank == "Ensign":
            total_cost += 200
            
    return total_cost

# --- 10. COUNT OFFICERS (4 Marks) ---
def count_officers(ranks):
    count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander":
            count += 1
    return count

def main():
    # 1. Initialize the parallel lists
    names, ranks, divs, ids = init_database()
    
    print("System Booting...")

    

    while True:
        choice = display_menu()

        if choice == "1":
            display_roster(names, ranks, divs, ids)
            
        elif choice == "2":
            add_member(names, ranks, divs, ids)
            
        elif choice == "3":
            remove_member(names, ranks, divs, ids)
            
        elif choice == "4":
            update_rank(names, ranks, ids)
            
        elif choice == "5":
            search_crew(names, ranks, divs, ids)
            
        elif choice == "6":
            filter_by_division(names, divs)
            
        elif choice == "7":
            # Call the analysis functions
            cost = calculate_payroll(ranks)
            officers = count_officers(ranks)
            
            print(f"\n--- Fleet Analysis ---")
            print(f"Total Monthly Payroll: {cost} Credits")
            print(f"High-Ranking Officers (Capt/Cmdr): {officers}")

        elif choice == "8":
            print("Exiting System.")
            break
            
        else:
            print("Invalid Option.")

# Run the program
if __name__ == "__main__":
    main()