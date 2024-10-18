# NoteApp

NoteApp is a full-stack note-taking application built with Django for the backend, and vanilla HTML, JavaScript, and Tailwind CSS for the frontend. This project provides a user-friendly interface for user authentication, note creation, editing, and management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- User authentication (signup and login)
- Create and edit notes
- View all user notes
- Markdown support for note content
- Responsive design using Tailwind CSS

## Installation

To get started with NoteApp, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/noteapp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd noteapp
    ```

3. Set up the backend:

    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    python manage.py migrate
    ```

4. Set up the frontend:

    ```bash
    cd ../frontend
    npm install
    ```

5. Create a `.env` file in the root directory and add the following environment variables:

    ```
    DJANGO_SECRET_KEY=your_secret_key_here
    DEBUG=True
    ```

6. Start the Django development server:

    ```bash
    cd ../backend
    python manage.py runserver
    ```

7. In a new terminal, start the frontend development server:

    ```bash
    cd ../frontend
    npm run start
    ```

The application should now be running. The backend will be available at `http://localhost:8000`, and the frontend will be served at `http://localhost:3000`.

## Usage

1. Open your web browser and navigate to `http://localhost:3000`.

2. If you're a new user, click on the "Sign Up" button and create an account.

3. If you already have an account, click on the "Login" button and enter your credentials.

4. Once logged in, you'll be taken to your dashboard where you can view your existing notes or create new ones.

5. To create a new note, click on the "New Note" button and start writing. You can use Markdown syntax for formatting.

6. To edit an existing note, click on the note title in your dashboard.

7. Your notes are automatically saved as you type.

8. To log out, click on the "Logout" button in the navigation bar.

Enjoy using NoteApp for all your note-taking needs!