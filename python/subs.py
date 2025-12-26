# 1. This is a FUNCTION
# It takes a list (variable) and a name, then returns a greeting
def create_greeting(name):
    # .upper() is a STRING METHOD that makes text all caps
    shouting_name = name.upper()
    return f"Welcome to the party, {shouting_name}!"

def main():
    # 2. These are VARIABLES
    # 'guests' is a list (array-like)
    guests = ["Alice", "Bob", "Charlie"]
    
    print("--- Party Guest List ---")

    # 3. Using a LOOP to process the list
    for person in guests:
        # We call our function and store the result in a variable
        message = create_greeting(person)
        print(message)

    # 4. Using a LIST METHOD
    # .append() adds a new item to the end of the list
    guests.append("Daisy")
    
    print(f"\nUpdate: We added a new guest. Total guests: {len(guests)}")
    print(f"The last person added was: {guests[-1]}")

# Run the program
main()