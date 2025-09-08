import requests
import os

print("Welcome to the Ubuntu Image Fetcher")

url = input("Enter image URL: ")

os.makedirs("Fetched_Images", exist_ok=True)

try:
    response = requests.get(url)
    response.raise_for_status()
    
    filename = url.split("/")[-1] or "image.jpg"
    path = os.path.join("Fetched_Images", filename)
    
    with open(path, "wb") as file:
        file.write(response.content)
    
    print(f"✓ Successfully saved {filename} in Fetched_Images")
except Exception as e:
    print(f"Error: {e}")
