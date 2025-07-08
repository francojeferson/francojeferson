# Progress

This file documents the project's progress, including what works, what's left to build, current status, known issues,
and the evolution of project decisions.

## What Works

- A Python script (`scripts/scrape_explosm.py`) successfully scrapes the latest cartoon from Explosm.net and saves it as
  `latest_explosm_cartoon.jpg`.
- Additional scripts (`scripts/scrape_pbfcomics.py` and `scripts/scrape_workchronicles.py`) successfully scrape cartoons
  from PBF Comics and Work Chronicles, saving them as `latest_pbf_cartoon.jpg` and `latest_workchronicles_comic.png`
  respectively.
- The `README.md` file has been updated to display the latest cartoon with a humorous caption, enhancing project
  documentation.

## What's Left to Build

- Automation mechanism to periodically run the scraping script to keep the cartoon updated in the README.md.
- Additional error handling or logging in the script to notify if the website structure changes significantly,
  preventing successful scraping.

## Current Status

- The cartoon scraping features for Explosm.net, PBF Comics, and Work Chronicles are fully functional and integrated
  into the project's main documentation.
- The project is in a stable state with the recent addition of multiple cartoon displays in `README.md`.

## Known Issues

- The script may fail if Explosm.net changes its website structure significantly; current fallback logic mitigates this
  but may not cover all future changes.
- No automated scheduling is in place yet to update the cartoon regularly.

## Evolution of Project Decisions

- Initially focused on creating a functional scraper for the latest Explosm cartoon, which was achieved using `requests`
  and `BeautifulSoup` with robust fallback logic.
- Decision to integrate the scraped image into `README.md` to enhance project visibility and engagement.
- Added a humorous caption to the cartoon display in `README.md` to improve user experience, reflecting a focus on
  presentation quality.
