import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download images from a URL
def download_images(url, output_dir, start_num=100):
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Send a request to the webpage
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print("Connected! Yippee!")
    if response.status_code != 200:
        print(f"Failed to access {url}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Uncomment this for every image
    # for i, img_tag in enumerate(img_tags, start=start_num):
    #     img_url = img_tag.get('src')
    #     if not img_url:
    #         continue

    # Specify the indices of the images you want to download (not 0 index backed)
    indices_to_download = [5, 7]
    # uniqlo: 5, 7

    # Iterate through the specified indices and download the corresponding images
    # Comment this out if you want to download every image
    for index in indices_to_download:
        if index < len(img_tags):  # Check if the index is within bounds
            img_tag = img_tags[index]
            img_url = img_tag.get('src')
            if not img_url:
                print(f"No src attribute found for image at index {index}. Skipping.")
                continue

        # Handle relative URLs by converting them to absolute URLs
        img_url = urljoin(url, img_url)

        # Download the image
        # Comment this out to download every image
        try:
                img_data = requests.get(img_url, headers=headers).content
                img_filename = f"{start_num + index}.jpg"  # Use start_num for filenames
                img_filepath = os.path.join(output_dir, img_filename)

                # Save the image
                with open(img_filepath, 'wb') as img_file:
                    img_file.write(img_data)

                print(f"Downloaded {img_url} as {img_filename}")
        except Exception as e:
                print(f"Failed to download {img_url}: {e}")
        else:
            print(f"Index {index} is out of range for the number of images found.")

        # Uncomment this to download everything 
        # try:
        #     img_data = requests.get(img_url, headers=headers).content
        #     img_filename = f"{i}.jpg"
        #     img_filepath = os.path.join(output_dir, img_filename)

        #     # Save the image
        #     with open(img_filepath, 'wb') as img_file:
        #         img_file.write(img_data)

        #     print(f"Downloaded {img_url} as {img_filename}")
        # except Exception as e:
        #     print(f"Failed to download {img_url}: {e}")

# Example usage
url = 'https://www.uniqlo.com/us/en/products/E465755-000/01?colorDisplayCode=40&sizeDisplayCode=003'  # Replace with the website URL you want to scrape
output_dir = 'downloaded_images'  # Directory to save the images
download_images(url, output_dir)