import requests

# Function to find the longest movie watched by a user
def find_longest_movie(user_id, url):
    try:
        # Make a request to the URL to fetch the JSON data
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
            return
        
        # Parse the JSON data
        data = response.json()

        # Find the user by ID
        user = next((viewer for viewer in data["viewers"] if viewer["id"] == user_id), None)
        
        if user is None:
            print(f"User with ID {user_id} not found.")
            return
        
        # Filter movies in the user's viewing history
        movies = [entry for entry in user["viewingHistory"] if entry["type"] == "movie"]
        
        if not movies:
            print(f"User {user_id} has not watched any movies.")
            return
        
        # Find the longest movie based on duration
        longest_movie = max(movies, key=lambda x: x["duration"])
        
        print(f"The longest movie watched by user {user_id} is '{longest_movie['title']}' with a duration of {longest_movie['duration']} minutes.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while requesting data: {e}")

# URL to the JSON data
url = "https://cv-public-interview-assets.s3.us-east-1.amazonaws.com/entertainment/entertainment.json"

# Find the longest movie for user with ID 15
find_longest_movie(15, url)