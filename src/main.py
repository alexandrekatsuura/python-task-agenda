import click
import json
from datetime import datetime
import os

from task_manager import TaskManager


@click.group()
def cli():
    """A simple CLI for managing tasks."""
    pass


@cli.command()
@click.option('--task', prompt='Enter task description', help='The description of the task.')
def add(task):
    """Adds a new task."""
    manager = TaskManager()
    manager.add_task(task)
    click.echo(f'Task "{task}" added.')


@cli.command()
def list():
    """Lists all tasks."""
    manager = TaskManager()
    tasks = manager.list_tasks()
    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo("\nYour Tasks:")
    click.echo("--------------------------------------------------")
    for i, task in enumerate(tasks):
        status = "[X]" if task['completed'] else "[ ]"
        completed_date = f" (Completed: {task['completed_at']})" if task['completed_at'] else ""
        click.echo(f"{i + 1}. {status} {task['description']}{completed_date} (Added: {task['created_at']})")
    click.echo("--------------------------------------------------")


@cli.command()
@click.option('--index', type=int, prompt='Enter the task number to complete', help='The number of the task to mark as complete.')
def complete(index):
    """Marks a task as complete."""
    manager = TaskManager()
    try:
        manager.complete_task(index - 1)  # Adjust for 0-based index
        click.echo(f'Task {index} marked as complete.')
    except IndexError:
        click.echo("Invalid task number.")


@cli.command()
@click.option('--index', type=int, prompt='Enter the task number to remove', help='The number of the task to remove.')
def remove(index):
    """Removes a task."""
    manager = TaskManager()
    try:
        manager.remove_task(index - 1)  # Adjust for 0-based index
        click.echo(f'Task {index} removed.')
    except IndexError:
        click.echo("Invalid task number.")


if __name__ == '__main__':
    cli()

