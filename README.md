# Flask Task Manager Demo

## Framework Information
- **Name:** Flask
- **Version:** 2.3.x
- **Creator:** Armin Ronacher (2010)
- **Official Documentation:** https://flask.palletsprojects.com/
- **GitHub:** https://github.com/pallets/flask

## What is Flask?
Flask is a lightweight, open-source Python web framework used for building web applications. It provides the essential tools needed to create web servers and handle HTTP requests without forcing unnecessary dependencies on developers. Flask follows a "micro-framework" philosophy, meaning it provides core functionality while remaining flexible and extensible.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CISC375-web-framework
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Features Implemented
- [x] Display a list of tasks
- [x] Add a new task
- [x] Mark a task as complete
- [x] Delete a task

## Architecture Overview

### Backend (app.py)
- **Framework:** Flask
- **Routes:**
  - `GET /` - Serves the main HTML page
  - `GET /api/tasks` - Returns all tasks in JSON format
  - `POST /api/tasks` - Creates a new task
  - `PUT /api/tasks/<id>` - Updates task completion status
  - `DELETE /api/tasks/<id>` - Removes a task

### Frontend (templates/index.html)
- **HTML/CSS:** Responsive, modern UI with gradient background
- **JavaScript:** Vanilla JS for API communication and DOM manipulation
- **Styling:** CSS flexbox for layout, smooth transitions and hover effects

## What We Learned
- **Routing in Flask:** Understanding how to map URLs to Python functions using decorators
- **RESTful API Design:** Creating endpoints that follow HTTP conventions (GET, POST, PUT, DELETE)
- **Request/Response Handling:** Processing JSON data from the frontend and returning appropriate responses
- **Frontend-Backend Communication:** Using fetch API to communicate with Flask backend asynchronously
- **In-Memory Data Storage:** How data persists during a session but resets on server restart
- **Error Handling:** Validating user input and returning appropriate HTTP status codes
- **Development Workflow:** Using Flask's debug mode for rapid development and testing

## Group Contributions
- **Khue Vo:** Repo set up, README, Core Concepts, Demo Video Recording
- **John Mezeritski:** Code Implementation, Update README, Pros and Cons
- **Nate Agbemadon:** Code Set up, Industry Adoption
- **Ethan Lukandwa:** Overview, Creator, Problem Solved by Flask

## Resources Used

[1] Pallets Projects, "Flask Documentation," 2024. [Online]. Available: https://flask.palletsprojects.com/. [Accessed: May 13, 2026].

[2] Pallets Projects, "Flask by Example," 2024. [Online]. Available: https://flask.palletsprojects.com/tutorial/. [Accessed: May 13, 2026].

[3] M. Kennedy, "Building Web Applications with Flask," Real Python, 2023. [Online]. Available: https://realpython.com/flask-by-example/. [Accessed: May 13, 2026].

[4] Pallets Projects, "Flask API Reference," 2024. [Online]. Available: https://flask.palletsprojects.com/api/. [Accessed: May 13, 2026].
