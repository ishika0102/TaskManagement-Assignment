# import hashlib
import time


def generate_task_id() -> int:
    """Generate a unique 6-digit task ID based on the timestamp."""
    # Get the current timestamp in milliseconds
    timestamp = int(time.time() * 1000)

    # Take the last 6 digits of the timestamp
    task_id = timestamp % 1000000

    # If the ID is less than 6 digits, pad with leading zeros insuring always 6 digits
    return task_id if task_id >= 100000 else task_id + 1000000
