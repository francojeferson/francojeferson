#!/usr/bin/env python3
"""
Script to scrape the latest comic from Work Chronicles on Substack
and save it with a static filename. This script is designed to be educational
and easy to understand for beginners learning web scraping with Python.
"""

import requests
from bs4 import BeautifulSoup
import os


def get_latest_article_url():
    """
    Fetch the Work Chronicles Substack homepage and extract the URL of the latest article.
    Returns the article URL as a string or None if extraction fails.
    """
    url = "https://workchronicles.substack.com/archive"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch homepage. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        # Look for the first article link in various possible sections
        posts_section = None
        for class_name in ["posts", "post-list", "content", "main-content", "archive"]:
            posts_section = soup.find("div", class_=class_name)
            if posts_section:
                break

        if not posts_section:
            # Try finding any div containing links with 'post' or 'comic' in the class or href
            for div in soup.find_all("div"):
                if any(
                    "post" in c.lower() or "comic" in c.lower()
                    for c in div.get("class", [])
                ):
                    posts_section = div
                    break
                links = div.find_all("a")
                for link in links:
                    if "href" in link.attrs and (
                        "post" in link["href"].lower()
                        or "comic" in link["href"].lower()
                    ):
                        posts_section = div
                        break
                if posts_section:
                    break

        if not posts_section:
            print("Could not find posts section on homepage.")
            # Debug: Print potential sections for diagnosis
            divs = soup.find_all("div")[:5]  # Limit to first 5 for brevity
            if divs:
                print("Debug - Potential sections found:")
                for i, div in enumerate(divs, 1):
                    div_id = div.get("id", "No id")
                    div_class = div.get("class", "No class")
                    print(f"  {i}. id: {div_id}, class: {div_class}")
            return None

        # Try various class names for the post title/link
        latest_post = None
        for class_name in [
            "post-preview-title",
            "post-title",
            "title",
            "post-link",
            "post",
        ]:
            latest_post = posts_section.find("a", class_=class_name)
            if latest_post:
                break

        if not latest_post:
            # Fallback to the first 'a' tag in the section that looks like a post link
            links = posts_section.find_all("a")
            for link in links:
                if "href" in link.attrs and "/p/" in link["href"]:
                    latest_post = link
                    break

        if latest_post and "href" in latest_post.attrs:
            article_url = latest_post["href"]
            if not article_url.startswith("http"):
                article_url = f"https://workchronicles.substack.com{article_url}"
            return article_url
        else:
            print("Could not find the latest article link on the homepage.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching homepage: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while parsing homepage: {e}")
        return None


def get_comic_image_url(article_url):
    """
    Fetch the article page and extract the URL of the comic image.
    Returns the image URL as a string or None if extraction fails.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch article page. Status code: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        # Look for the comic image in the article content
        content = soup.find("div", class_="body")
        if not content:
            print("Could not find article content.")
            return None

        comic_img = content.find("img")
        if comic_img and "src" in comic_img.attrs:
            img_url = comic_img["src"]
            if "substackcdn.com" in img_url:
                return img_url
            else:
                print("Found an image, but it doesn't seem to be the comic.")
                return None
        else:
            print("Could not find the comic image in the article.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching article page: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error while parsing article page: {e}")
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
    """
    print("Starting script to scrape the latest Work Chronicles comic...")

    article_url = get_latest_article_url()
    if article_url:
        print(f"Found latest article URL: {article_url}")
        img_url = get_comic_image_url(article_url)
        if img_url:
            print(f"Found comic image URL: {img_url}")
            output_filename = "latest_workchronicles_comic.png"
            success = download_image(img_url, output_filename)
            if not success:
                print("Failed to download or save the image.")
        else:
            print("Failed to extract the comic image URL from the article.")
    else:
        print("Failed to extract the latest article URL.")

    print("Script execution completed.")


if __name__ == "__main__":
    main()
