# User Account Creation Microservice

This project is a Python-based microservice responsible for handling user account creation. It uses Flask to expose a RESTful API endpoint and SQLAlchemy to interact with MySQL databases. The service is designed to be containerized using Docker.

## Folder Structure

Here's a breakdown of the main folders and their purpose:

*   `.github/workflows/`: Contains GitHub Actions workflow files. For example, `docker-publish.yml` likely handles building and publishing the Docker image.
*   `conections/`: Manages connections to the different databases used by the application. `mysql.py` within this folder likely contains functions to establish connections to MySQL databases.
*   `models/`: Defines the database schemas using SQLAlchemy ORM. `models.py` includes class definitions that map to database tables (e.g., `User`, `Profile`).
*   `services/`: Contains the business logic of the application. `functions.py` in this folder includes core functionalities like `create_user`.
*   `tests/`: Includes various tests for the application.
    *   `routetest.py`: Appears to be a script for manual integration testing of API endpoints.
    *   `test_create_account.py`: Contains automated unit tests for the account creation functionality, using `pytest` and `unittest.mock`.
*   `__pycache__/`: Directory for Python bytecode cache files (automatically generated).
*   `dockerfile`: Instructions for building the Docker image for this service.
*   `main.py`: The main entry point of the Flask application. It defines API routes (e.g., `/create_account`) and starts the development server.
*   `requirements.txt`: Lists the Python dependencies required for this project.

## Backend Design and Communication

### Architectural Pattern

This service is built as a **Microservice**. Its primary responsibility is focused on user account creation. Internally, the service follows a **Layered Architecture**:

*   **Presentation Layer (`main.py`)**: Handles incoming HTTP requests (routing) using Flask.
*   **Service Layer (`services/functions.py`)**: Contains the core business logic for creating users, including validation and coordination with database operations and external services.
*   **Data Access Layer (`conections/mysql.py`, `models/models.py`)**: Manages database interactions. `models.py` defines the data structures (ORM models), and `mysql.py` handles the database connection setup.

### Communication Architecture

*   **RESTful API**: The service exposes a RESTful API for clients to interact with. The primary endpoint is `POST /create_account`.
*   **Database Communication**:
    *   It connects to two separate MySQL databases: one for `accounts` and another for `userprofile`.
    *   SQLAlchemy is used as the ORM for database interactions.
*   **Inter-service Communication**:
    *   The service communicates with an external `default-photo` microservice. After successfully creating a user and their profile, it makes an HTTP POST request to the `DEFAULT_PHOTO_URL` (environment variable, e.g., `http://your ip:8080/default-photo`) to assign a default photo to the new user.

## Folder Pattern

The project primarily utilizes a **Layer-based** folder organization pattern. This is evident in the separation of concerns into distinct directories:

*   `conections/`: Handles the data access layer's connection aspects.
*   `models/`: Contains data structures (ORM models), also part of the data access layer.
*   `services/`: Encompasses the business logic (service layer).
*   `main.py`: Acts as the presentation layer (controller/routes).
*   `tests/`: Groups all tests, which can be further organized by the layer or feature they test.


### Environment Variables

The application requires several environment variables to be set for database connections and other configurations. It uses `python-dotenv`, so you can create a `.env` file in the project root.

Create a `.env` file with the following variables:

```env
# Database 'Accounts' Connection
DBA_HOSTIP=your_accounts_db_host
DBA_PORT=your_accounts_db_port
DBA_USER=your_accounts_db_user
DBA_PASSWORD=your_accounts_db_password
DBA_NAME=your_accounts_db_name

# Database 'UserProfile' Connection
DBU_HOSTIP=your_userprofile_db_host
DBU_PORT=your_userprofile_db_port
DBU_USER=your_userprofile_db_user
DBU_PASSWORD=your_userprofile_db_password
DBU_NAME=your_userprofile_db_name

# Default Photo Microservice URL
DEFAULT_PHOTO_URL=http://your direcction:8080/default-photo
```
## API Endpoint: Create Account

### `POST /create_account`

This endpoint is used to create a new user account and associated profile.

**Request Body (JSON):**

```json
{
    "Name": "YourName",
    "Lastname": "YourLastName",
    "User_mail": "user@example.com",
    "Password": "yoursecurepassword",
    "Id_type": 1,
    "Id_preferences": 1
}
```

**Fields:**

*   `Name` (string, required): First name of the user.
*   `Lastname` (string, required): Last name of the user.
*   `User_mail` (string, required, unique): Email address of the user. This will be used as the unique identifier.
*   `Password` (string, required): Password for the user account.
*   `Id_type` (integer, required): Identifier for the user type (maps to `Types.Id_type` in the database).
*   `Id_preferences` (integer, required): Identifier for user preferences (maps to `Preferences.Id_preferences` in the database).

**Responses:**

*   **201 Created - Success:**
    ```json
    {
        "message": "User created successfully",
        "user_id": 123,
        "user_mail": "user@example.com"
    }
    ```
    *   `user_id`: The ID of the newly created user in the `users` table.

*   **400 Bad Request - Missing Fields:**
    ```json
    {
        "error": "Missing field(s): Password, Id_type"
    }
    ```

*   **400 Bad Request - No JSON Payload:**
    ```json
    {
        "error": "No JSON payload received"
    }
    ```

*   **409 Conflict - Email Exists or Integrity Error:**
    ```json
    {
        "error": "Email already exists or database integrity error."
    }
    ```

*   **500 Internal Server Error - Unexpected Error:**
    ```json
    {
        "error": "Unexpected error: <description of error>"
    }
    ```
