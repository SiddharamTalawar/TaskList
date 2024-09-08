# Django Task Management Project
# Demo Vedio 
https://drive.google.com/file/d/1CAo1N4ozIuIiiFJWfHZothmVx7FW3TKF/view?usp=sharing

## Description
This is a Django-based task management application that allows users to create, update, and delete tasks. The application includes features such as filtering, sorting, searching and notifications.

## Table of Contents
- Installation
- Usage
- Contributing
- License
- Contact

## Installation

### Prerequisites
- Python 3.x
- Django 3.x
- Bootstrap 5.x

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/SiddharamTalawar/TaskList.git
    
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### Creating a Task
1. use django admin or Navigate to the task creation page by clicking Plus symbol on top right corner of the home screen.
2. Fill in the task details and click "Create".

### Updating a Task
1. Click on a task in the task list to open the update page.
2. Modify the task details and click "Update".

### Deleting a Task
1. Click the "Delete" button next to a task in the task list.
2. Confirm the deletion.

### Filtering and Sorting and searching
- Use the filter and sort options to organize tasks based on status, priority, and due date.
- we can also agument the search along with above mentioned filters to look for specific tasks.


### Notifications
- alert Notifications will appear at the top of the page for important updates like tasks due today or whenever a new task is created or update or deleted.

## Contributing
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Siddharam Talawar - siddhu.dev822@gmail.com

Project Link: https://github.com/SiddharamTalawar/TaskList.git
