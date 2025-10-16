# Walmart LLM Application with BLU Chatbot

A Flask-based web application featuring user authentication and an intelligent chatbot assistant named BLU.

## Features

- **User Authentication**: Secure login system with static credentials
- **BLU Chatbot**: Interactive chatbot with predefined responses for common queries
- **Consistent Navigation**: Navbar present on all pages
- **User Profile Management**: View user details and roles
- **JSON Visualization**: Display structured data

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python ashu.py
```

The application will be available at `http://localhost:5000`

## Login Credentials

### Admin Account
- Username: `admin`
- Password: `admin123`

### User Account
- Username: `user`
- Password: `user123`

## Application Structure

```
├── ashu.py              # Flask application with routes
├── templates/           # HTML templates
│   ├── base.html       # Base template with navbar
│   ├── index.html      # Home page
│   ├── login.html      # Login page
│   ├── chatbot.html    # BLU chatbot interface
│   ├── user_details.html  # User profile page
│   └── json_page.html  # JSON visualization
├── static/
│   ├── css/
│   │   └── style.css   # Application styles
│   └── js/
│       └── chatbot.js  # Chatbot functionality
└── requirements.txt     # Python dependencies
```

## Features Details

### BLU Chatbot
BLU (Walmart Assistant) can help with:
- Product information
- Store locations and hours
- Return policies
- Customer service inquiries
- General Walmart queries

The chatbot uses predefined responses to handle common questions about Walmart services.

### UI Fixes
- **Fixed message positioning**: Messages now scroll properly within the chat container
- **Visible input box**: Chat input is always visible at the bottom of the chat interface
- **Responsive design**: Works on both desktop and mobile devices

## Routes

- `/` - Home page
- `/login` - User login
- `/logout` - User logout
- `/chatbot` - BLU chatbot interface (requires login)
- `/user-details` - User profile (requires login)
- `/json` - JSON data visualization
- `/chat` - API endpoint for chatbot (POST, requires login)
