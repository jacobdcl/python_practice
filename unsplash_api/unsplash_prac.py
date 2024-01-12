import requests
import os

def fetch_images(query, api_key, folder, number_of_images=10):
    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={api_key}&per_page={number_of_images}"
    response = requests.get(url)

    if response.status_code == 200:
        photos = response.json()['results']
        for i, photo in enumerate(photos):
            image_url = photo['urls']['regular']
            download_image(image_url, os.path.join(folder, f"{query}_{i}.jpg"))
    else:
        print("Failed to fetch images:", response.status_code)

def download_image(image_url, file_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

################### CODE ########################

def main():
    API_KEY = 'chca0uYYLHbo9-HS9aN3iJIyrLXwg6yURuT72uQtBYc'
    query = 'staten island, westerleigh' #keywords to search
    folder = 'unsplash_api/downloaded_images'
    num_imgs = 5

    if not os.path.exists(folder):
        os.makedirs(folder)

    fetch_images(query, API_KEY, folder, num_imgs)

if __name__ == '__main__':
    main()
