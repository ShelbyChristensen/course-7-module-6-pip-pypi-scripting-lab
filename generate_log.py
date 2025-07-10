from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input must be a list of strings.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename
