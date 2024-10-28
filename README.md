# Medicine Index Application

A web application built with Django to manage a searchable index of medicines. The application allows users to view and search for medicines and gives admins full CRUD capabilities.

## Features

- **Medicine Listing**: View a list of all medicines with description including name, generic name, manufacturer, price, and batch number.
- **Search Functionality**: Search medicines by name or generic name as keywords, with highlighted results.
- **User Roles and Permissions**:
  - **Public Users**: Can view and search medicines.
  - **Admins**: Can add, edit, delete, and update medicines.
- **Authentication**: Login and logout functionality for user sessions.

## Technologies Used

## Tech Stack

- **Backend**:Python, Django, SQLite
- **Frontend**: HTML, CSS, Bootstrap, Django Crispy Forms
- **Authentication**: Django's built-in authentication system


## Requirements

- **Python**: 3.x
- **Django**: 5.x
- **SQLite**: (default database for Django projects)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fahadfoysal/employee_management.git
    cd employee_management
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (optional, for accessing the admin interface):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application in your web browser:**

    Open your browser and navigate to: [http://localhost:8000](http://localhost:8000)

## URL Endpoints

- **Medicine List Page:** `/`
  - Displays a list of all medicines with search functionality.

- **Login Page:** `/login/`
  - Login page to CRUD operations on medicines

- **Register Page:** `/register/`
  - Register to page create account.

- **Add Medicine Page:** `/create/`
  - Add medicine page to add new medicine.

- **Update Medicine Page:** `/update/<pk>/`
  - Form to edit an existing medicine's information.

- **Delete Medicine Action:** `/delete/<pk>/`
  - Action to delete an medicine after confirmation.

- **Admin Dashboard:** `/admin/`
  - Django's built-in admin interface for managing models and data.

- **Demo account:**
  - username: test3
  - password: 123456@test


For any inquiries or support, please contact [fahadfoysal16@gmail.com](mailto:fahadfoysal16@gmail.com).

