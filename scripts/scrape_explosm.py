#!/usr/bin/env python3
"""
Script to scrape the latest cartoon from Explosm.net (Cyanide & Happiness)
and save it with a static filename. This script is designed to be educational
and easy to understand for beginners learning web scraping with Python.
"""

import requests
from bs4 import BeautifulSoup
import os


def get_latest_cartoon_url():
    """
    Fetch the Explosm.net homepage and extract the URL of the latest comic image.
    The site uses Next.js with lazy-loaded images. The comic is the first <img> element
    with a src matching 'static.explosm.net/<year>/' pattern.
    Returns the image URL as a string or None if extraction fails.
    """
    url = "http://explosm.net"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Explosm uses Next.js with lazy-loaded images.
        # The comic image URL starts with 'https://static.explosm.net/' followed by
        # a date path like '2026/05/17114109/backstabbed.png'.
        # Look for images with this pattern.
        for img in soup.find_all("img"):
            src = img.get("src", "")
            if "static.explosm.net" in src:
                # Match pattern: /YYYY/ in URL path (date-based comic images)
                # and ends with .png
                if any(f"/{year}/" in src for year in ["2022", "2023", "2024", "2025", "2026", "2027", "2028"]) and src.endswith(".png"):
                    return src

        print("Could not find the latest comic image on the page.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while parsing webpage: {e}")
        return None


def download_image(img_url, output_filename):
    """
    Download the image from the given URL and save it with the specified filename.
    Returns True if successful, False otherwise.
    """
    try:
        # Set user-agent for the image request as well
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send HTTP GET request to download the image
        response = requests.get(img_url, headers=headers, timeout=10)

        if response.status_code == 200:
            # Write the image content to a file, overwriting any existing file
            with open(output_filename, "wb") as f:
                f.write(response.content)
            print(f"Successfully downloaded and saved image as {output_filename}")
            return True
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error while saving image: {e}")
        return False


def main():
    """
    Main function to orchestrate the scraping and downloading process.
    """
    print("Starting script to scrape the latest Explosm cartoon...")

    # Get the URL of the latest cartoon image
    img_url = get_latest_cartoon_url()

    if img_url:
        print(f"Found latest cartoon image URL: {img_url}")
        # Define the static filename for the output image
        output_filename = "latest_explosm_cartoon.jpg"
        # Download and save the image
        success = download_image(img_url, output_filename)
        if not success:
            print("Failed to download or save the image.")
    else:
        print("Failed to extract the latest cartoon image URL.")

    print("Script execution completed.")


if __name__ == "__main__":
    main()
