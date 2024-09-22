# Function to check name length
def check_name_length():
    # Get first and last name input
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    # Check if both names are at least 2 characters long
    if len(first_name) < 2:
        print("Error: First name must be at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print(f"Name accepted: {first_name} {last_name}")

# Run the function
check_name_length()
