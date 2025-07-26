# 📝 Task Agenda CLI with JSON Storage

![GitHub repo size](https://img.shields.io/github/repo-size/alexandrekatsuura/python-task-agenda?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/alexandrekatsuura/python-task-agenda?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/alexandrekatsuura/python-task-agenda?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/alexandrekatsuura/python-task-agenda?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/alexandrekatsuura/python-task-agenda?style=for-the-badge)

## 📚 Academic Use Disclaimer

> ⚠️ This is an academic project created for learning purposes only.
> It is not intended for production use.

## ℹ️ About

This project is a command-line task agenda application built in Python. It allows users to manage their daily tasks through a simple CLI interface, with all data stored in JSON format for persistence. The application provides essential task management features including adding, listing, completing, and removing tasks, all designed with a clean, object-oriented structure that makes it easy to understand, extend, and test.

## 🚀 Features

*   **Add Tasks**: Create new tasks with descriptions and automatic timestamps.
*   **List Tasks**: View all tasks with their status (pending/completed) and creation dates.
*   **Complete Tasks**: Mark tasks as completed with completion timestamps.
*   **Remove Tasks**: Delete tasks from the agenda.
*   **JSON Storage**: Persistent data storage using JSON format.
*   **Command-Line Interface (CLI)**: Interactive menu-driven interface.
*   **Data Validation**: Input validation and error handling.
*   **Unit Tested**: Comprehensive test suite using `pytest`.
*   **Clean Project Structure**: Organized into `src` and `tests` directories for maintainability.

## 🛠️ Technologies Used

*   **Python 3.x**
*   **Click**: For enhanced CLI functionality
*   **JSON**: For data persistence
*   **`pytest`**: For creating and running unit tests

## ⚙️ How to Run the Project

### Prerequisites

*   Python 3.x installed on your system

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/alexandrekatsuura/python-task-agenda
    cd python-task-agenda
    ```

2.  (Recommended) Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate      # On Linux/macOS
    # .venv\Scripts\activate       # On Windows
    ```

3.  Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To start the task agenda, run the following command from the project root:

```bash
python src/main.py
```

The application will display an interactive menu with the following options:

1. **Add Task**: Create a new task
2. **List Tasks**: Display all tasks with their status
3. **Complete Task**: Mark a task as completed
4. **Remove Task**: Delete a task
5. **Exit**: Close the application

## ✅ Running the Tests

To run the unit tests, execute the following command from the project root directory:

```bash
pytest -v
```

This command will discover and run all tests located in the `tests/` directory.

## 📁 Project Structure

```bash
python-task-agenda/
├── src/
│   ├── __init__.py
│   ├── task_manager.py         # Contains the TaskManager class
│   └── main.py                 # Contains main execution logic and CLI
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py    # Unit tests for the TaskManager class
├── .gitignore                  # Standard Python .gitignore
├── README.md                   # This documentation file
├── requirements.txt            # Project dependencies
└── tasks.json                  # JSON file for task storage (created automatically)
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

