# Active Context

This file captures the current focus of work, recent changes, next steps, and active decisions for the project.

## Current Work Focus

- Developing Python scripts to scrape the latest cartoons from multiple sources including Explosm.net, PBF Comics, and
  Work Chronicles, and integrating them into the project's documentation.
- Planning and preparing for the full-stack web development portfolio (PJT1), which is the primary project under Mission
  1 (M1).

## Recent Changes

- Created and executed `scripts/scrape_explosm.py` to download the latest Explosm cartoon and save it as
  `latest_explosm_cartoon.jpg`.
- Created and executed `scripts/scrape_pbfcomics.py` to download the latest PBF Comics cartoon and save it as
  `latest_pbf_cartoon.jpg`.
- Created and executed `scripts/scrape_workchronicles.py` to download the latest Work Chronicles comic and save it as
  `latest_workchronicles_comic.png`.
- Updated `README.md` to display the latest cartoons with humorous captions.

## Next Steps

1. **Short-term (0-2 weeks)**:

   - Implement automation for the scraping scripts to run periodically
   - Add error handling and logging to notify of website structure changes
   - Update memory bank with current project state

2. **Medium-term (2-4 weeks)**:

   - Begin development of the full-stack portfolio (PJT1)
   - Set up React frontend using `npx create-react-app`
   - Initialize Node.js/Express backend
   - Configure MongoDB connection

3. **Long-term (Ongoing)**:
   - Develop full-stack portfolio features
   - Implement quarterly digital hygiene checklist (PJT2)
   - Create jiu-jitsu and emotional intelligence curriculum (PJT3)

## Active Decisions and Considerations

- The cartoon scraping scripts use fallback logic to handle dynamic website structures, ensuring robustness in scraping
  tasks.
- Images are saved with static filenames to maintain consistency in the README.md embedding.
- The full-stack portfolio will use React.js for the frontend, Node.js/Express for the backend, and MongoDB for the
  database.
- Technologies are chosen to minimize complexity for aspiring developers, with JavaScript used across the stack.

## Important Patterns and Preferences

- Use of `requests` and `BeautifulSoup` for web scraping tasks due to their simplicity and effectiveness.
- Emphasis on clear documentation and presentation in README.md to enhance project visibility.
- Component-based architecture for the portfolio project to improve maintainability and scalability.
- Iterative development approach for the portfolio, starting with basic features and gradually enhancing functionality.

## Learnings and Project Insights

- Implementing robust fallback mechanisms is crucial for web scraping to handle unexpected changes in website HTML
  structure.
- Adding engaging content like humorous captions can improve the user experience in project documentation.
- Consistent file naming conventions simplify integration of scraped content into documentation.
- Modular design in scraping scripts allows for easier updates and debugging when expanding to new sources.
