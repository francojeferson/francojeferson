# Tech Context: TELOS about Jeff

## Technologies Used

"TELOS about Jeff" utilizes multiple technologies across its various projects. The primary focus is on the full-stack
web development portfolio (PJT1), with supporting technologies for cartoon scraping and future projects. The technology
stack is selected to balance accessibility for aspiring developers with robust functionality for professional
deployment.

### Active Projects

#### Full-Stack Web Development Portfolio (PJT1)

- **Frontend Technologies**:

  - **React.js**: Core JavaScript library for building user interfaces

    - Installation: `npx create-react-app portfolio-frontend`
    - Key Features: Component-based architecture, hooks, virtual DOM
    - Purpose: Create dynamic, interactive portfolio pages

  - **Material-UI or Bootstrap**: UI component library for consistent design

    - Material-UI: `@mui/material`, `@emotion/react`, `@emotion/styled`
    - Bootstrap: `bootstrap`, `react-bootstrap`
    - Purpose: Provide pre-built, responsive UI components

  - **State Management**:

    - Redux: For complex state management needs
    - Context API: For simpler state requirements
    - Installation: `npm install react-redux redux` or built into React

  - **Testing Framework**:
    - **React Testing Library**: For component testing
    - **Jest**: For unit and integration tests
    - Installation: `npm install --save-dev @testing-library/react @testing-library/jest-dom jest`

- **Backend Technologies**:

  - **Node.js**: JavaScript runtime environment

    - Requirement: Version 16.x or higher
    - Purpose: Execute server-side JavaScript code

  - **Express.js**: Web application framework for Node.js

    - Installation: `npm init -y && npm install express`
    - Key Features: Routing, middleware integration, REST API creation

  - **MongoDB & Mongoose**: Database and ODM

    - MongoDB: NoSQL database for flexible data storage
    - Mongoose: Object Data Modeling for MongoDB
    - Installation: `npm install mongoose`
    - Purpose: Store portfolio data, user information, and contact submissions

  - **Authentication**:

    - **JSON Web Tokens (JWT)**: For user authentication
    - Installation: `npm install jsonwebtoken bcryptjs`
    - Purpose: Secure API endpoints and user sessions

  - **Environment Management**:
    - **dotenv**: For managing environment variables
    - Installation: `npm install dotenv`
    - Purpose: Separate configuration from code

- **Development & DevOps Tools**:

  - **Git & GitHub**: Version control and repository hosting

    - Purpose: Track changes, collaborate, and deploy from repository

  - **ESLint & Prettier**: Code linting and formatting

    - Installation: `npm install --save-dev eslint prettier eslint-config-prettier`
    - Purpose: Maintain code quality and consistency

  - **Nodemon**: For development server auto-restart
    - Installation: `npm install --save-dev nodemon`
    - Purpose: Streamline development workflow

- **Deployment Technologies**:

  - **Frontend Hosting**:

    - **Vercel**: Serverless deployment platform
    - **Netlify**: Static site hosting
    - Purpose: Deploy React application with automatic builds and custom domains

  - **Backend Hosting**:
    - **Heroku**: Cloud platform for applications
    - **AWS (Elastic Beanstalk)**: Scalable cloud hosting
    - Purpose: Deploy Node.js/Express backend with environment variables

#### Cartoon Scraping System

- **Python**: Programming language for scraping scripts

  - Version: Python 3.7+
  - Purpose: Create web scrapers for cartoon content

- **Requests HTTP Library**:

  - Installation: `pip install requests`
  - Purpose: Send HTTP requests to websites

- **BeautifulSoup HTML Parser**:

  - Installation: `pip install beautifulsoup4`
  - Purpose: Parse and extract data from HTML

- **Standard Libraries**:
  - `os`: File and path operations
  - Purpose: Save downloaded images to filesystem

#### Future Projects (Planned)

- **Digital Hygiene Checklist (PJT2)**:

  - Technologies to be determined
  - Potential: Google Sheets, Notion, static HTML, or simple mobile app

- **Jiu-Jitsu Curriculum (PJT3)**:
  - Technologies to be determined
  - Potential: Static site generators, PDF tools, or content management systems

## Development Setup

### Local Development Environment

1. **Prerequisites**:

   - Node.js (16.x or higher)
   - npm (comes with Node.js)
   - Python 3.7+
   - Git
   - MongoDB (local installation or Atlas cloud account)

2. **Portfolio Frontend Setup**:

   ```bash
   # Create new React app
   npx create-react-app portfolio-frontend

   # Navigate to project directory
   cd portfolio-frontend

   # Install dependencies
   npm install
   npm install material-ui @mui/icons-emotion @emotion/react @emotion/styled
   npm install --save-dev nodemon eslint prettier

   # Start development server
   npm start
   ```

3. **Portfolio Backend Setup**:

   ```bash
   # Create backend directory
   mkdir portfolio-backend
   cd portfolio-backend

   # Initialize npm project
   npm init -y

   # Install dependencies
   npm install express mongoose dotenv jsonwebtoken bcryptjs cors
   npm install --save-dev nodemon jest

   # Create basic express server
   # (code implementation needed here)
   ```

4. **Database Setup**:

   - Option 1: Local MongoDB installation
   - Option 2: MongoDB Atlas (cloud)
     - Create account at mongodb.com
     - Create new cluster
     - Add IP to access list
     - Create database user
     - Get connection string

5. **Environment Configuration**:
   - Create `.env` file in root of each project
   - Add variables like database connection strings, API keys, etc.

### Project Structure

```
TELOS-about-Jeff/
├── memory-bank/
│   ├── projectbrief.md
│   ├── productContext.md
│   ├── activeContext.md
│   ├── systemPatterns.md
│   ├── techContext.md
│   ├── progress.md
│   ├── consolidated_learnings.md
│   └── raw_reflection_log.md
├── scripts/
│   ├── scrape_explosm.py
│   ├── scrape_pbfcomics.py
│   └── scrape_workchronicles.py
├── portfolio-frontend/        (to be created)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles/
│   │   └── index.js
│   ├── public/
│   └── package.json
├── portfolio-backend/         (to be created)
│   ├── src/
│   │   ├── routes/
│   │   ├── models/
│   │   ├── controllers/
│   │   └── app.js
│   ├── .env
│   └── package.json
├── latest_explosm_cartoon.jpg
├── latest_pbf_cartoon.jpg
├── latest_workchronicles_comic.png
└── README.md
```

## Technical Constraints

- **Learning Curve**: Technologies chosen minimize complexity for beginners while providing professional capabilities
- **Cost Solutions**: Emphasis on free tiers (Vercel, Netlify, MongoDB Atlas, Heroku)
- **Time Constraints**: Development organized into manageable phases to fit within personal time limits
- **Resource Limitations**: Maximum utilization of free and open-source tools
- **Scalability**: Architecture supports growth from small projects to more complex applications

## Dependencies Management

- **Frontend**: `package.json` with npm for dependency management
- **Backend**: `package.json` with npm for dependency management
- **Scraping Scripts**: `requirements.txt` for Python dependencies (to be added)
- **Version Consistency**: Semantic versioning approach across all projects

## Tool Usage Patterns

### Git Workflow

- Feature branch development: `git checkout -b feature/new-feature`
- Regular commits: `git commit -m "feat: add new component"`
- Push to remote: `git push origin feature/new-feature`
- Merge requests for review

### Development Workflow

- **Frontend**: Component development with React Testing Library tests
- **Backend**: API endpoint development with Jest tests
- **Integration**: End-to-end testing of frontend-backend communication
- **Documentation**: JSDoc comments for API endpoints

### Deployment Process

1. Test locally: `npm test`
2. Build frontend: `npm run build`
3. Push to Git repository
4. Deploy to Vercel/Netlify (frontend) and Heroku/AWS (backend)

## Security Considerations

- **HTTPS**: Automatic HTTPS on deployment platforms
- **Input Validation**: Implement for all form submissions and API inputs
- **Helmet.js**: Security middleware for Express (to be added)
- **Environmental Variables**: Store sensitive data in environment variables
- **CORS**: Configure for cross-origin requests

## Future Technology Considerations

- **Containerization**: Docker for consistent environments
- **CI/CD**: GitHub Actions for automated testing and deployment
- **Monitoring**: Application performance tools (to be added)
- **Analytics**: Usage tracking features (to be added)

This tech context provides a comprehensive overview of the technologies used in "TELOS about Jeff" and will be updated
as projects evolve and technologies mature.
