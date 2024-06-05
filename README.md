# User Management System

User Management System is a Django application for managing user data through REST APIs. It allows you to perform CRUD operations on user data, including listing users, creating new users, updating existing users, and deleting users.

## Setup

1. Clone the repository:


2. Navigate to the project directory:


3. Create a virtual environment (optional but recommended):


5. Install the dependencies-- install requirement.txt file


6. Run the migrations to set up the database:


## Usage

1. Run the Django development server:


2. Access the API endpoints:

   - List all users: `http://127.0.0.1:8000/api/userdetails?page=1&name=Josephine&sort=-age`
   - Create a new user: `http://localhost:8000/api/users/`
   - Get details of a user: `http://localhost:8000/api/usersdetails/{id}/
   - Update details of a user: `http://localhost:8000/api/usersdetails/{id}/
   - Delete a user: `http://localhost:8000/api/usersdetails/{id}/

## API Documentation

### List all users


Optional query parameters:

- `page`: Number for pagination (default: 1)
- `limit`: Number of items to be returned (default: 5)
- `name`: Search user by name (substring matching)
- `sort`: Name of attribute to sort by (default: 'id', use '-' prefix for descending order)

Sample query: `/api/users?page=1&limit=10&name=John&sort=-age`

### Create a new user

Request Payload (JSON format):

```json
{
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Test Company",
    "age": 30,
    "city": "New York",
    "state": "NY",
    "zip": 12345,
    "email": "john@example.com",
    "web": "http://www.example.com"
} 
```
GET /api/users/1/
PUT /api/users/3/
{
    "first_name": "First Name",
    "last_name": "Updated Last Name",
    "age": 40,
    "company_name": "Updated Company Name",
    "city": "Updated City",
    "state": "Updated State",
    "zip": 12345,
    "email": "updated@example.com",
    "web": "http://www.updated.com"
}




