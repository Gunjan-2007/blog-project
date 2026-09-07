# Basic Blog Backend

A basic Blog Backend API built using FastAPI and JSON files for data storage.

# Features

The API provides functionality for:

- Creating and retrieving users
- Creating and retrieving posts
- Adding comments to posts
- Retrieving data using API endpoints
- Basic request validation
- Error handling for invalid or unavailable resources

# Tech Stack

- Python
- FastAPI
- JSON – used for storing application data
- Uvicorn – used to run the FastAPI application

# Project Structure

blog-backend/
│
├── main.py
├── users.py
├── posts.py
├── comments.py
├── likes.py
│
├── users.json
├── posts.json
├── comments.json
├── likes.json
│
└── README.md

# How It Works

The project is divided into different APIs based on the resources of a blog application.

Users API

Handles user-related operations such as creating and retrieving users.

User data is stored in "users.json".

Posts API

Handles operations related to blog posts, such as creating and retrieving posts and sorting them.

Post data is stored in "posts.json".

Comments API

Allows users to add comments to posts and retrieve comments.

Comment data is stored in "comments.json".

Likes API

Handles adding likes to posts and retrieving like information.

Like data is stored in "likes.json".

# Data Storage

This project uses JSON files instead of a database.

Whenever data is created or updated through the API, the corresponding JSON file is used to store the data.

Example:

User → users.json
Post → posts.json
Comment → comments.json
Like → likes.json

# Running the Project

1. Create a virtual environment

python -m venv env

2. Activate the virtual environment

For Git Bash:

source env/Scripts/activate

3. Install FastAPI and Uvicorn

pip install fastapi uvicorn

4. Run the application

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000/

# API Documentation

FastAPI provides interactive API documentation automatically.

Open:

http://127.0.0.1:8000/docs

From Swagger UI, all available endpoints can be tested directly.

Project Objective

The purpose of this project is to understand the fundamentals of FastAPI, REST APIs, CRUD operations, JSON-based data storage, API routing, request validation, and error handling.
