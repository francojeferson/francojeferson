#!/usr/bin/env python3
"""
Script to scrape the latest comic from Work Chronicles on Substack
and save it with a static filename. This script is designed to be educational
and easy to understand for beginners learning web scraping with Python.
"""

import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET

BASE_URL = "https://www.workchronicles.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def get_article_urls(max_articles=10):
    """
    Fetch the Work Chronicles RSS feed and extract article URLs.
    RSS feeds are less likely to be IP-blocked by Substack than
    the archive page (which returns HTTP 403 from datacenter IPs).
    Returns a list of article URLs.
    """
    rss_url = f"{BASE_URL}/feed"
    try:
        response = requests.get(rss_url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            print(f"Failed to fetch RSS feed. Status code: {response.status_code}")
            return []

        root = ET.fromstring(response.text)
        article_urls = []
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        for item in root.iter("item"):
            link = item.find("link")
            if link is not None and link.text:
                url = link.text.strip()
                if "/p/" in url and url not in article_urls:
                    article_urls.append(url)
                    if len(article_urls) >= max_articles:
                        break
        # Also check Atom-style links (Substack uses <atom:link>)
        if not article_urls:
            for entry in root.iter("entry"):
                link = entry.find("link")
                if link is not None:
                    href = link.get("href", "")
                    if "/p/" in href and href not in article_urls:
                        article_urls.append(href)
                        if len(article_urls) >= max_articles:
                            break

        return article_urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return []
    except ET.ParseError as e:
        print(f"Error parsing RSS XML: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error while parsing RSS: {e}")
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
