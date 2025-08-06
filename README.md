# Scope:
This project is to develop a full-stack web application which is encompasses a simple to-do application. The functionality of the web app is to be able to add, delete and edit tasks as well as check them as complete or have them unchecked inferring still needing attention. 

# Purpose:
The objective of this process is to give me a better understanding of the way that web tech stacks are set up and how different technologies communicate with each other. On top of this there is a desire to enable deployment of new updates to be automated and seamless through what currently seems to be GitHub Actions and to be secured via some authorisation method. 

# Technologies used:
- FastAPI
- Vue
- MongoDB

# Minimum Viable Product
The minimum viable product for this project is to have a website hosted on a external hosting provider and meet the following FRs and NFRs. Core features include CI/CD, automatic API documentation. The final product should be a simple ToDo application. 

# Requirements 

## Functional Requirements
These describe what the system should do — the core features and functions.

### User Registration and Login

- Users can sign up with an email and password.

- Users can log in and log out securely.

### Task CRUD Operations

- Users can create new tasks.

- Users can read/view their list of tasks.

- Users can update task details (e.g. description, completion status).

- Users can delete individual or all tasks.

### Task Status Management

- Users can mark tasks as complete or incomplete.

- Users can filter tasks by status (All / Complete / Incomplete).

- Authentication and Authorization

- Only logged-in users can access their tasks.

### API Documentation

- Auto-generated API docs using OpenAPI/Swagger **Potentially using scaler as well**

- Frontend Integration

## Non-Functional Requirements (NFR)
These define how the system performs rather than what it does.

### Performance

- API response time should be less than 500ms for 95% of requests.

- Frontend should load within 2 seconds on standard connections.

### Security

- Passwords must be hashed 

- Authentication must be present for securing endpoints.

- Reliability & Availability

- 99.9% uptime with minimal outages.

- Proper error handling and logging in place.

### Usability

- Clean and responsive UI that works on desktop, not responsive for this pupose.

- Simple and intuitive user experience.

### Maintainability

- Code should follow standard best practices

- Well-documented API and components.

- The project must have CI/CD capabilities via github actions 


### Testability

- Unit and integration tests should cover major components.
