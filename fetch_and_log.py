import requests
from lib.generate_log import generate_log

def fetch_data():
    """
    Fetch sample post data from jsonplaceholder.typicode.com.
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Data fetched successfully.")
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

if __name__ == "__main__":
    # Fetch data from the API
    post_data = fetch_data()

    if post_data:
        # Convert dictionary values to a list of formatted strings
        log_entries = [f"{key}: {value}" for key, value in post_data.items()]

        # Use your reusable generate_log to log this data
        generate_log(log_entries)
