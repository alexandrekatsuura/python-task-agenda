import pytest
import os
import json
import tempfile
from datetime import datetime
from src.task_manager import TaskManager


class TestTaskManager:
    """Test class for TaskManager functionality."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.task_manager = TaskManager(filename=self.temp_file.name)

    def teardown_method(self):
        """Clean up after each test method."""
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_init_with_new_file(self):
        """Test TaskManager initialization with a new file."""
        assert self.task_manager.tasks == []
        assert self.task_manager.filename == self.temp_file.name

    def test_add_task(self):
        """Test adding a new task."""
        self.task_manager.add_task("Test task")
        
        assert len(self.task_manager.tasks) == 1
        assert self.task_manager.tasks[0]["description"] == "Test task"
        assert self.task_manager.tasks[0]["completed"] is False
        assert self.task_manager.tasks[0]["created_at"] is not None
        assert self.task_manager.tasks[0]["completed_at"] is None

    def test_add_empty_task(self):
        """Test adding an empty task should raise ValueError."""
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            self.task_manager.add_task("")
        
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            self.task_manager.add_task("   ")
        
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            self.task_manager.add_task(None)

    def test_list_tasks(self):
        """Test listing tasks."""
        # Initially empty
        assert self.task_manager.list_tasks() == []
        
        # Add tasks and test
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        
        tasks = self.task_manager.list_tasks()
        assert len(tasks) == 2
        assert tasks[0]["description"] == "Task 1"
        assert tasks[1]["description"] == "Task 2"

    def test_complete_task(self):
        """Test completing a task."""
        self.task_manager.add_task("Test task")
        
        # Complete the task
        self.task_manager.complete_task(0)
        
        assert self.task_manager.tasks[0]["completed"] is True
        assert self.task_manager.tasks[0]["completed_at"] is not None

    def test_complete_task_invalid_index(self):
        """Test completing a task with invalid index."""
        self.task_manager.add_task("Test task")
        
        with pytest.raises(IndexError, match="Task index out of range"):
            self.task_manager.complete_task(1)
        
        with pytest.raises(IndexError, match="Task index out of range"):
            self.task_manager.complete_task(-1)

    def test_complete_already_completed_task(self):
        """Test completing an already completed task."""
        self.task_manager.add_task("Test task")
        self.task_manager.complete_task(0)
        
        with pytest.raises(ValueError, match="Task is already completed"):
            self.task_manager.complete_task(0)

    def test_remove_task(self):
        """Test removing a task."""
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        
        # Remove first task
        self.task_manager.remove_task(0)
        
        assert len(self.task_manager.tasks) == 1
        assert self.task_manager.tasks[0]["description"] == "Task 2"

    def test_remove_task_invalid_index(self):
        """Test removing a task with invalid index."""
        self.task_manager.add_task("Test task")
        
        with pytest.raises(IndexError, match="Task index out of range"):
            self.task_manager.remove_task(1)
        
        with pytest.raises(IndexError, match="Task index out of range"):
            self.task_manager.remove_task(-1)

    def test_get_pending_tasks(self):
        """Test getting pending tasks."""
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.complete_task(0)
        
        pending_tasks = self.task_manager.get_pending_tasks()
        assert len(pending_tasks) == 1
        assert pending_tasks[0]["description"] == "Task 2"

    def test_get_completed_tasks(self):
        """Test getting completed tasks."""
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.complete_task(0)
        
        completed_tasks = self.task_manager.get_completed_tasks()
        assert len(completed_tasks) == 1
        assert completed_tasks[0]["description"] == "Task 1"

    def test_clear_all_tasks(self):
        """Test clearing all tasks."""
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        
        self.task_manager.clear_all_tasks()
        
        assert len(self.task_manager.tasks) == 0

    def test_get_task_count(self):
        """Test getting task counts."""
        # Initially empty
        counts = self.task_manager.get_task_count()
        assert counts == {"total": 0, "pending": 0, "completed": 0}
        
        # Add tasks
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2")
        self.task_manager.add_task("Task 3")
        self.task_manager.complete_task(0)
        
        counts = self.task_manager.get_task_count()
        assert counts == {"total": 3, "pending": 2, "completed": 1}

    def test_persistence(self):
        """Test that tasks are persisted to file."""
        self.task_manager.add_task("Persistent task")
        
        # Create a new TaskManager instance with the same file
        new_manager = TaskManager(filename=self.temp_file.name)
        
        assert len(new_manager.tasks) == 1
        assert new_manager.tasks[0]["description"] == "Persistent task"

    def test_load_corrupted_file(self):
        """Test loading from a corrupted JSON file."""
        # Write invalid JSON to the file
        with open(self.temp_file.name, 'w') as f:
            f.write("invalid json content")
        
        # Should handle gracefully and start with empty list
        manager = TaskManager(filename=self.temp_file.name)
        assert manager.tasks == []

