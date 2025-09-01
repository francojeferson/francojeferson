# System Patterns: TELOS about Jeff

## System Architecture Overview

"TELOS about Jeff" encompasses multiple projects with distinct technical requirements. The system architecture is
designed to be modular, allowing each project to evolve independently while maintaining alignment with the overall
mission. The primary focus has shifted from initial cartoon scraping functionality to building a comprehensive
full-stack web development portfolio (PJT1), with future plans for digital hygiene tools (PJT2) and personal curriculum
content (PJT3).

### Full-Stack Web Development Portfolio (PJT1)

The full-stack web development portfolio represents the core technical initiative, designed to showcase development
skills while providing value to aspiring developers, particularly older or undereducated individuals. The architecture
emphasizes simplicity, scalability, and maintainability.

#### Current Architecture

- **Frontend**:

  - Framework: React.js
  - State Management: Redux or Context API
  - Styling: Material-UI or Bootstrap
  - Rationale: React offers widespread industry adoption, a vast community for support, and component-based development
    suitable for beginners. Using JavaScript across the stack reduces the learning curve.
  - Key Features: Responsive design, project showcase, about page, contact form

- **Backend**:

  - Framework: Node.js with Express.js
  - Authentication: JWT-based
  - Rationale: Node.js provides JavaScript consistency, while Express offers lightweight API development. This
    combination is ideal for creating RESTful services.
  - Key Features: REST API endpoints, project data management, contact form handling

- **Database**:

  - Type: MongoDB (NoSQL)
  - ODM: Mongoose
  - Rationale: MongoDB's flexible schema evolution supports varied portfolio content, while Mongoose simplifies data
    modeling and relationships.
  - Key Features: Projects collection, user profiles (if applicable), contact submissions

- **Deployment**:
  - Frontend: Vercel or Netlify
  - Backend: Heroku or AWS
  - Rationale: These platforms offer free tiers, easy integration with Git, and CI/CD capabilities, making them ideal
    for learning and showcasing projects.
  - Key Features: Automated deployments, custom domains, HTTPS

#### Component Relationships

- React components communicate with Express endpoints via REST API calls
- Express uses Mongoose to interact with MongoDB for data persistence
- User interface components trigger state updates, which may interact with backend services
- Authentication flows verify user credentials for protected portfolio sections
- Contact form submissions use backend APIs to send notifications or store inquiries

#### Critical Implementation Paths

1. **Initialization Phase**:

   - Set up React frontend with Create React App
   - Initialize Express backend with npm
   - Configure MongoDB Atlas or local instance
   - Set up environment variables for configuration

2. **Core Development Phase**:

   - Implement project showcase components
   - Create about page with professional information
   - Build contact form with submission handling
   - Set up basic CRUD operations for project data

3. **Enhancement Phase**:

   - Implement authentication if user accounts are needed
   - Add image upload capabilities for project screenshots
   - Create filtering or search for project portfolio
   - Implement dark mode or theme switching

4. **Deployment Phase**:
   - Deploy frontend to Vercel/Netlify
   - Deploy backend to Heroku/AWS
   - Configure environment-specific settings
   - Set up custom domain if desired

### Cartoon Scraping System

A separate but integrated system handles the cartoon scraping functionality:

- **Architecture**: Custom Python scripts using requests and BeautifulSoup
- **Modularity**: Each source (Explosm.net, PBF Comics, Work Chronicles) has its own script
- **Integration**: Results are saved as static images and displayed in README.md
- **Failure Handling**: Robust fallback logic for website structure changes

### Digital Hygiene System (PJT2 - Future)

- **Architecture**: Likely a combination of documented processes and simple tools
- **Components**: Privacy audit checklists, automated monitoring scripts (where appropriate)
- **Integration**: Results will be documented and shared as part of the portfolio

### Personal Curriculum System (PJT3 - Future)

- **Architecture**: Content-focused system (potentially static site or PDF)
- **Components**: Structured curriculum materials, examples, exercises
- **Integration**: Will be presented as a shareable resource through the portfolio

## Key Technical Decisions

### Technology Stack Rationale

- **JavaScript/Node.js Ecosystem**: Chosen for consistency across the stack to minimize learning complexity for aspiring
  developers
- **React.js for Frontend**: Industry standard with strong community support and components suitable for beginners
- **Express.js for Backend**: Minimalist framework that provides maximum flexibility
- **MongoDB for Database**: Flexible document model that supports evolving portfolio content
- **Cloud-Native Deployment**: Prioritizing managed services to focus on development rather than infrastructure

### System Design Principles

- **Modularity**: Each project operates as a distinct system with clear interfaces
- **Scalability**: Architectures designed to handle growth from prototype to production
- **Maintainability**: Code organization follows established patterns and best practices
- **Accessibility**: Technologies chosen to minimize barriers for undereducated individuals
- **Security**: Basic security practices will be implemented (HTTPS, input validation, etc.)

## Design Patterns in Use

### Frontend Patterns

- **Component-Based Architecture**: UI elements broken into reusable components
- **Container/Presentational Pattern**: Separating logic from display
- **Higher-Order Components (HOC)**: For cross-cutting concerns like authentication
- **Custom Hooks**: For state management and side effects

### Backend Patterns

- **MVC Pattern**: Model-View-Controller structure for API development
- **Repository Pattern**: Abstracting data access logic
- **Middleware Pattern**: For authentication, logging, and request processing
- **RESTful API Design**: Consistent endpoint structure and HTTP methods

### Database Patterns

- **Document Schema Design**: Flexible data modeling for evolving content
- **Reference-Based Relationships**: For connecting related data in MongoDB
- **Embedded Documents**: For simple, contained related data

## System Integration Points

- **Portfolio Cartoons**: Cartoon scraping results displayed in portfolio README
- **Version Control**: Git repository hosts all projects and documentation
- **CI/CD**: Automated testing and deployment pipelines for portfolio components
- **Static Asset Management**: Images and documents stored in repository and deployed with frontend

## Future Considerations

- **Monorepo Structure**: Potential consolidation of related projects as the portfolio grows
- **Microservices**: Breaking backend into services if complexity increases
- **Serverless Functions**: For specific tasks like contact form submission
- **Containerization**: Docker containers for consistent deployment environments

This system architecture document will evolve as projects progress and technologies mature. Each project under "TELOS
about Jeff" will follow these patterns while adapting to specific requirements and constraints.
