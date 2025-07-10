from datetime import datetime

def generate_log(data):
    # Raise ValueError if input is not a list
    if not isinstance(data, list):
        raise ValueError("Input must be a list of strings.")

    # Generate the filename in log_YYYYMMDD.txt format
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Write each entry on its own line
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # Return the filename for testing and grading
    return filename
