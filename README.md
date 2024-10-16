# NoteAppBackend

NoteAppBackend is a backend project for a note-taking application built with Django. This project provides a set of APIs for user authentication, note management, and other functionalities related to note-taking.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [User Registration](#user-registration)
  - [Note Management](#note-management)

## Installation

To get started with NoteAppBackend, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/drowsyzen/markdown-Note-taking-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd noteappbackend
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- **Token Obtain Pair**
  - **URL:** `/api/token/`
  - **Method:** `POST`
  - **Description:** Obtain a new JWT token pair (access and refresh tokens) by providing valid user credentials.

- **Token Refresh**
  - **URL:** `/api/token/refresh/`
  - **Method:** `POST`
  - **Description:** Refresh the access token using a valid refresh token.

### User Registration

- **Register User**
  - **URL:** `/register/`
  - **Method:** `POST`
  - **Description:** Register a new user by providing necessary user details.

### Note Management

- **Check Grammar of Note**
  - **URL:** `/checkgrammer/`
  - **Method:** `POST`
  - **Description:** Check the grammar of a provided note.

- **Render Markdown to HTML**
  - **URL:** `/rendermdtohtml/`
  - **Method:** `POST`
  - **Description:** Render a provided Markdown note to HTML format.

- **Create New Note**
  - **URL:** `/createnote/`
  - **Method:** `POST`
  - **Description:** Create a new note by providing the note details.

- **Delete Current Note**
  - **URL:** `/deletenote/<int:id>/`
  - **Method:** `DELETE`
  - **Description:** Delete an existing note identified by its ID.

- **Update Current Note**
  - **URL:** `/updatenote/<int:note_id>/`
  - **Method:** `POST`
  - **Description:** Update an existing note identified by its note ID.

- **Get All User Notes**
  - **URL:** `/getallnotes/<int:user_id>/`
  - **Method:** `GET`
  - **Description:** Retrieve all notes belonging to a specific user identified by their user ID.

<!-- finished Version 1 , date - 3 july 2024  -->

##### version 1(end date) - 3 july 2024