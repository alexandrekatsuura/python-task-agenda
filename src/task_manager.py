import json
import os
from datetime import datetime
from typing import List, Dict, Any


class TaskManager:
    """
    A class to manage tasks with JSON storage.
    
    This class provides functionality to add, list, complete, and remove tasks.
    All tasks are stored in a JSON file for persistence.
    """

    def __init__(self, filename: str = "tasks.json"):
        """
        Initialize the TaskManager with a specified filename.
        
        Args:
            filename (str): The name of the JSON file to store tasks. Defaults to "tasks.json".
        """
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> List[Dict[str, Any]]:
        """
        Load tasks from the JSON file.
        
        Returns:
            List[Dict[str, Any]]: A list of task dictionaries.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []

    def _save_tasks(self) -> None:
        """
        Save tasks to the JSON file.
        """
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, indent=2, ensure_ascii=False)

    def add_task(self, description: str) -> None:
        """
        Add a new task to the task list.
        
        Args:
            description (str): The description of the task to add.
        
        Raises:
            ValueError: If the description is empty or None.
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        
        task = {
            "description": description.strip(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "completed_at": None
        }
        self.tasks.append(task)
        self._save_tasks()

    def list_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all tasks.
        
        Returns:
            List[Dict[str, Any]]: A list of all tasks.
        """
        return self.tasks

    def complete_task(self, index: int) -> None:
        """
        Mark a task as completed.
        
        Args:
            index (int): The index of the task to complete.
        
        Raises:
            IndexError: If the index is out of range.
            ValueError: If the task is already completed.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        
        if self.tasks[index]["completed"]:
            raise ValueError("Task is already completed")
        
        self.tasks[index]["completed"] = True
        self.tasks[index]["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._save_tasks()

    def remove_task(self, index: int) -> None:
        """
        Remove a task from the task list.
        
        Args:
            index (int): The index of the task to remove.
        
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task index out of range")
        
        self.tasks.pop(index)
        self._save_tasks()

    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all pending (not completed) tasks.
        
        Returns:
            List[Dict[str, Any]]: A list of pending tasks.
        """
        return [task for task in self.tasks if not task["completed"]]

    def get_completed_tasks(self) -> List[Dict[str, Any]]:
        """
        Get all completed tasks.
        
        Returns:
            List[Dict[str, Any]]: A list of completed tasks.
        """
        return [task for task in self.tasks if task["completed"]]

    def clear_all_tasks(self) -> None:
        """
        Remove all tasks from the task list.
        """
        self.tasks = []
        self._save_tasks()

    def get_task_count(self) -> Dict[str, int]:
        """
        Get the count of total, pending, and completed tasks.
        
        Returns:
            Dict[str, int]: A dictionary with task counts.
        """
        total = len(self.tasks)
        completed = len(self.get_completed_tasks())
        pending = total - completed
        
        return {
            "total": total,
            "pending": pending,
            "completed": completed
        }

