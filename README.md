Here's a comprehensive README file for your QuizApp. This includes a project description, setup instructions, usage details, and more.

---

# QuizApp

QuizApp is a Flask-based web application that allows users to take quizzes, track scores, and authenticate with login and registration. This app fetches quiz questions from the Open Trivia API and offers a simple UI with essential features like password visibility toggle and "Remember Me" functionality for login.

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup and Installation](#setup-and-installation)
4. [File Structure](#file-structure)
5. [Usage](#usage)
6. [APIs](#apis)
7. [License](#license)

---

### Features

- **User Authentication**: Register, login, and logout functionality.
- **Remember Me**: Option to keep users logged in on their devices.
- **Password Visibility Toggle**: An eye icon on the login page to show/hide passwords.
- **Quiz Page**: Fetches questions from the Open Trivia API, enabling dynamic quizzes.
- **Score Tracking**: Tracks user scores at the end of each quiz.
- **Responsive Design**: Ensures usability on both desktop and mobile devices.

---

### Technologies Used

- **Python** and **Flask**: For backend server and routing.
- **Flask-SQLAlchemy**: To manage the SQLite database.
- **HTML/CSS/JavaScript**: For frontend design and interactivity.
- **Open Trivia API**: To fetch quiz questions.

---

### Setup and Installation

#### Prerequisites

- Python 3.x
- A virtual environment (optional, but recommended)

#### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/uchexz0977/quizapp.git
   cd quizapp
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r config/requirements.txt
   ```

4. **Set up the database**:
   Initialize the database with the following command:

   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the application**:

   ```bash
   python app.py
   ```

6. **Access the app**:
   Open a web browser and go to `http://127.0.0.1:5000`.

---

### File Structure

```
quizapp/
│
├── config/
│   └── config class(represensting .env)  # Contains project dependencies
|
│
├── app.py                          # Main application file
├── models.py                       # Database models (User model defined here)
├── README.md                       # Project documentation
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template with navbar
│   ├── index.html                  # Landing page
│   ├── login.html                  # Login page with Remember Me and eye icon for password
│   ├── signup.html                 # Signup page
│   ├── home.html                   # Home page after login
│   ├── quiz.html                   # Quiz page that fetches questions from API
│   ├── quiz_completed.html         # Page shown after quiz completion with score
│   ├── password_reset_request.html # Page to request password reset
│   └── error.html                  # Error page for handling 404 or other errors
│
└── static/                         # Static files (CSS, JS, images)
    ├── css/
    │   └── style.css               # Custom CSS styling
    └── js/
        └── script.js               # JavaScript for dynamic functionalities (e.g., password toggle)
```

---

### Usage

#### Authentication

- **Sign Up**: Register a new account by visiting `/signup`.
- **Login**: Log in with email and password. The **"Remember Me"** checkbox keeps users logged in on their device.
- **Logout**: End the session by clicking the **Logout** link in the navbar.

#### Quiz

1. After logging in, users can access the **Quiz** page from the homepage or navbar.
2. Questions are fetched from the **Open Trivia API** (you can replace `https://opentdb.com/api.php?amount=4` in `app.py` with specific categories or parameters).
3. After answering the questions, the app shows a **Quiz Completed** page with the user's score.

#### Password Visibility Toggle

On the login page, click the eye icon next to the password field to toggle password visibility.

### APIs

#### Open Trivia API

Quiz questions are fetched from [Open Trivia API](https://opentdb.com/). The API URL in `app.py` is:

```python
api_url = 'https://opentdb.com/api.php?amount=10'
```

Feel free to adjust the API URL for specific categories, difficulties, or question types.

---

### License

This project is open-source and free to use.
