from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        print("Error: Provided data is not a list.")
        return

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    try:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    # STEP 4: Print a confirmation message with the filename
    print(f"✅ Log successfully written to {filename}")

# Example usage to confirm functionality
if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_data)
