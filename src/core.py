# src/core.py
from typing import List, Dict, Any

def create_task(name: str, due: str) -> Dict[str, Any]:
    """
    Create a new task dictionary with a name and due date.

    Args:
        name (str): Title of the task (e.g., "Write essay").
        due  (str): Due date (e.g., "2025-09-15").

    Returns:
        Dict[str, Any]: Task data with completion flag.
    """
    # Trim extra spaces just in case
    name = name.strip()
    due = due.strip()
    # Basic task structure
    return {"name": name, "due": due, "done": False}

def mark_done(task: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mark a task as completed.

    Args:
        task (Dict[str, Any]): A task from create_task().

    Returns:
        Dict[str, Any]: The same task with "done" set to True.
    """
    # Flip the finished flag
    task["done"] = True
    # Return the updated task
    return task

def list_tasks(tasks: List[Dict[str, Any]]) -> List[str]:
    """
    Convert tasks into human-readable strings.

    Args:
        tasks (List[Dict[str, Any]]): Task dictionaries.

    Returns:
        List[str]: One line per task, with status and due date.
    """
    lines: List[str] = []
    for t in tasks:
        status = "✅" if t.get("done") else "❌"   # checkmark or cross
        lines.append(f"{status} {t.get('name')} (Due: {t.get('due')})")
    return lines
