# Django Task Manager Project

## Description
A Django-based task management system that allows users to create, track, and manage tasks with additional functionality like weather information based on the task's city.

## Features
- CRUD operations for tasks
- Filter tasks based on completion status
- Integration with OpenWeatherMap API to fetch weather data for a task's city
- Django Admin interface for managing tasks
- Unit tests for task management

## Installation

### Prerequisites
Ensure you have Python and pip installed.

### Clone the repository
```bash
git clone https://github.com/agarciactg/task_manager
cd task-manager
```

### Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up the database
```bash
python manage.py migrate
```

### Run the development server
```bash
python manage.py runserver
```

## Usage
- Visit `http://127.0.0.1:8000/tasks/` to view all tasks.
- Create a task at `http://127.0.0.1:8000/tasks/create/`.
- View task details and mark as completed.

## API Integration
This project integrates with OpenWeatherMap API to fetch weather details based on the city.

## Running Tests
Run unit tests with:
```bash
python manage.py test
```

## Technologies Used
- Django
- Python
- SQLite (default, can be switched to PostgreSQL/MySQL)
- Bootstrap (for styling)

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.
