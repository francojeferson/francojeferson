#!/usr/bin/env python3
"""
Script to scrape the latest comic from Work Chronicles on Substack
and save it with a static filename. This script is designed to be educational
and easy to understand for beginners learning web scraping with Python.
"""

import requests
from bs4 import BeautifulSoup
import os
import re


def get_article_urls(max_articles=10):
    """
    Fetch the Work Chronicles Substack archive page and extract article URLs.
    Comic articles have '/p/comic-' in the URL path.
    Returns a list of article URLs.
    """
    url = "https://workchronicles.substack.com/archive"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch archive. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        article_urls = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            if "/p/" in href and href not in article_urls:
                full_url = href
                if not href.startswith("http"):
                    full_url = f"https://workchronicles.substack.com{href}"
                article_urls.append(full_url)

        return article_urls[:max_articles]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching archive: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error while parsing archive: {e}")
        return []


def get_comic_image_url(article_url):
    """
    Fetch the article page and extract the URL of the comic image.
    Returns the image URL as a string or None if the article has no comic image.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"  Failed to fetch article. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        # Check JSON-LD for the image first (most reliable)
        for script in re.findall(
            r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
            response.text,
            re.DOTALL,
        ):
            import json
            try:
                data = json.loads(script)
                images = data.get("image", [])
                if images:
                    if isinstance(images, list) and len(images) > 0:
                        if isinstance(images[0], dict):
                            img_url = images[0].get("url", "")
                            if img_url and "substackcdn.com/image/fetch" in img_url:
                                return img_url
            except json.JSONDecodeError:
                pass

        # Fallback: look for the first image in the body content
        body = soup.find("div", class_="body")
        if not body:
            for cls in ["post-body", "available-content", "entry-content"]:
                body = soup.find("div", class_=cls)
                if body:
                    break

        if body:
            comic_img = body.find("img")
            if comic_img and "src" in comic_img.attrs:
                img_url = comic_img["src"]
                if "substackcdn.com/image/fetch" in img_url:
                    return img_url

            # Check picture elements too (Substack often wraps images in <picture>)
            picture = body.find("picture")
            if picture:
                img = picture.find("img")
                if img and "src" in img.attrs and "substackcdn.com/image/fetch" in img["src"]:
                    return img["src"]

        return None

    except requests.exceptions.RequestException as e:
        print(f"  Error fetching article: {e}")
        return None
    except Exception as e:
        print(f"  Unexpected error while parsing article: {e}")
        return None


def download_image(img_url, output_filename):
    """
    Download the image from the given URL and save it with the specified filename.
    Returns True if successful, False otherwise.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(img_url, headers=headers, timeout=10)

        if response.status_code == 200:
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
    Iterates through archive articles until finding one with a comic image.
    """
    print("Starting script to scrape the latest Work Chronicles comic...")

    article_urls = get_article_urls(max_articles=15)
    if not article_urls:
        print("Failed to find any articles on the archive page.")
        return

    print(f"Found {len(article_urls)} articles. Searching for a comic...")

    for i, article_url in enumerate(article_urls):
        print(f"  [{i+1}/{len(article_urls)}] Checking: {article_url}")
        img_url = get_comic_image_url(article_url)
        if img_url:
            print(f"Found comic image URL: {img_url}")
            output_filename = "latest_workchronicles_comic.png"
            success = download_image(img_url, output_filename)
            if success:
                print("Comic updated successfully.")
                return
            else:
                print("Failed to download or save the image.")
                return
        else:
            print(f"  -> No comic image found in this article.")

    print("Could not find any article with a comic image.")

    print("Script execution completed.")


if __name__ == "__main__":
    main()
