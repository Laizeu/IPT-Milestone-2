# Connectly Django API
Connectly is a backend REST API built with Django and Django REST Framework for managing users and posts. 

It demonstrates core backend concepts such as CRUD operations, validation, relational data handling, API security, and design patterns. The API also supports social features like likes, comments, Google OAuth authentication, and a personalized news feed with sorting and pagination. All endpoints were tested using Postman.

## Project Branch
The **final and latest tested version** of this project is located in the branch:
**Milestone-2**

All features for Milestone 2 (Likes, Comments, Google OAuth integration, and News Feed with sorting and pagination) were consolidated, merged, committed, and pushed to this branch.

To use the latest version of the project:
```bash
git checkout Milestone-2
```
# AI Disclosure Statement
AI tools (such as ChatGPT) were used to assist with documentation formatting, explanation of concepts, and guidance for testing API endpoints.  

All system design, implementation, testing, and integration of features (CRUD operations, validation, relationships, security, design patterns, likes, comments, Google OAuth, and news feed functionality) were implemented and verified by the project team.


## Project Overview

Connectly is a simplified social media backend API that allows users to create posts, interact through likes and comments, authenticate using Google OAuth, and view a personalized news feed.

The project demonstrates key backend engineering concepts including REST API design, database relationships, authentication, security, pagination, and scalable architecture patterns.


## Features
### Core API Features
- CRUD operations for Users and Posts
- Input validation for API requests
- Relational data integrity using Django models
- Secure authentication
- Password encryption
- HTTPS support
- Role-based access control
### Design Improvements
- Singleton Pattern for shared resources
- Factory Pattern for modular object creation
- Improved scalability and maintainability
### Social Interaction Features
- Users can like posts
- Users can comment on posts
- Retrieve comments for a specific post
- Post details include like count and comment count
###  Authentication
- Google OAuth login integration
- Secure login using Google accounts
### News Feed System
- Personalized news feed endpoint
- Sorting posts by date
- Pagination support for efficient data retrieval


## Tech Stack
Backend Framework
- Django

API Framework
- Django REST Framework

Authentication
- Google OAuth
- Django authentication system
  
Database
- SQLite (development)

Tools
- Postman (API testing)


## Setup & Run
1. Clone the repo 
   `https://github.com/Laizeu/Integrative-Programming-and-Technologies---connectly-django-api.git`
2. Navigate to the folder
   `cd connectly_project`
3. Switch to the Final Project Branch
   `git checkout Milestone-2`
2. Create & activate virtual environment
   `python3 -m venv env`
   Mac
   `source env/bin/activate`
   Windows
   `.venv\Scripts\activate`
3. Install dependencies
   `pip install -r requirements.txt`
4. Run migrations
   `python manage.py migrate`
5. Create a Superuser (for authentication testing)
   `python manage.py createsuperuser`
5. Start server
   Standard server
   `python3 manage.py runserver`
   HTTPS server
   `python3 manage.py runserver_plus --cert-file cert.pem --key-file key.pem`
   Server will run to:
   `http://127.0.0.1:8000/`


## API Endpoints

### Base URL
`http://127.0.0.1:8000`

### Users
```text
- GET /posts/users/            # Retrieve all users
- POST /posts/users/create/    # Create a new user
```
Sample Request Body
```json
{"username":"laizallanto","email":"laiza@gmail.com"}
```
Sample Response
```json

{
  "id": 1,
  "username": "laiza",
  "email": "laiza@example.com"
}
```
### Posts
```text
- GET /posts/posts/              # Retrieve all posts
- POST /posts/posts/create       # Create a new post
```
Sample Request Body
```json
{"content":"Hello this is Laiza's first post!","author":1}
```
Sample Response
```json
{
  "id": 1,
  "content": "Hello this is Laiza's first post!",
  "author": 1
}
```
### Likes
```text
- POST  /posts/{id}/like/          # Like a post
```
Sample Response
```json
{
  "message": "Post liked successfully"
}
```
### Comments
```text
- POST /posts/{id}/comment/         # Add comment to a post
- GET /posts/{id}/comments/         # Retrieve comments for a post
```
Sample Request Body
```json
{
  "text": "This is a comment by Laiza",
  "author": 1,
  "post": 1
}
```
Sample Response
```json
{
  "id": 1,
  "text": "This is a comment by Laiza",
  "author": 1,
  "post": 1
}
```
### Authentication
```text
- POST  /api/token/                          # Request authentication token
- POST  /auth/google/login/                  # Google OAuth login
- GET   /accounts/google/login/              # Start Google OAuth login
- GET   /accounts/google/login/callback/     # Google OAuth callback
```
### Example Token Request
POST /api/token/

Request Body
```json
{
  "username": "laiza",
  "password": "yourpassword"
}
```
Response
```json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
```
Authenticated requests must include the token in the header:
Authorization: Bearer <access_token>

### News Feed
```text
- GET   /posts/feed/                         # Retrieve personalized news feed
- GET   /posts/feed/?ordering=-created_at    # Sort posts by newest
- GET   /posts/feed/?page=1                  # Pagination (page 1)
- GET   /posts/feed/?page=2                  # Pagination (page 2)
```
### Example News Feed Request
`GET /posts/feed/?page=1&ordering=-created_at`
Returns a paginated list of posts ordered by newest first.
```
Example Feed Response
```json
{
  "count": 5,
  "next": "http://127.0.0.1:8000/posts/feed/?page=2",
  "previous": null,
  "results": [
    {
      "id": 7,
      "content": "Hello this is Laiza's first post!",
      "author": "laiza",
      "created_at": "2026-03-05T10:30:00Z",
      "like_count": 2,
      "comment_count": 1
    }
  ]
}
```

## Testing

All API endpoints were tested using **Postman**.

The following features were tested:

- Token authentication
- News feed retrieval
- Post sorting
- Pagination
- Personalized feed filtering
- Like interactions
- Comment interactions
- Error handling
- Google OAuth authentication

Both successful and error scenarios were verified.

### Test Evidence

Screenshots and exported Postman collections for the tests can be found here:

Testing Documentation:
`https://drive.google.com/drive/folders/15M2JXmP4iMxHy9ockM1mgprdcnJslNAh?usp=sharing`

Contents include:
- Postman API request/response screenshots
- Exported JSON Postman Collention file

## File Structure
```text
connectly_project/
├── connectly_project/        # Django project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── posts/                    # Core API logic (posts, likes, comments, feed)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── factories/                # Factory Design Pattern for creating objects
│   ├── __init__.py
│   ├── comment_factory.py
│   └── post_factory.py
│
├── singletons/               # Singleton Design Pattern implementations
│   ├── config_manager.py
│   └── logger_singleton.py
│
├── tests/                    # Unit tests for design patterns
│   ├── __init__.py
│   ├── test_post_factory.py
│   └── test_singleton.py
│
├── manage.py                 # Django management script
├── requirements.txt          # Python project dependencies
└── .gitignore                # Ignored files and folders
```
## Updated Diagrams
`https://drive.google.com/drive/folders/19loZ9dVJfG5qvpoIXgrr7_g7wR5TU5t-?usp=sharing`

## Requirements

- Python 3.10+
- Django
- Django REST Framework
- django-allauth (Google OAuth)
- SQLite (development database)

## Project Status

Milestone 2 – Completed  
Includes Likes, Comments, Google OAuth authentication, and News Feed with sorting and pagination.

### Author
```md
IPT Group 10
