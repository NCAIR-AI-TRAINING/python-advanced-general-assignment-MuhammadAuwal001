from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    """Create the file if it does not exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            pass  # create empty file

def get_last_visitor():
    """Return the last visitor's name and timestamp, or (None, None)."""
    if not os.path.exists(FILENAME):
        return None, None
    
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        if not lines:
            return None, None
        
        last_line = lines[-1].strip()
        name, timestamp = last_line.split(" | ")
        return name, datetime.fromisoformat(timestamp)

def add_visitor(visitor_name):
    """Add a visitor unless duplicate of previous visitor."""
    last_visitor, last_time = get_last_visitor()

    # Rule 1: No duplicate consecutive visitors
    if visitor_name == last_visitor:
        raise DuplicateVisitorError("Duplicate consecutive visitor not allowed.")

    # (5-minute rule will be added later in the branch)

    # Log visitor
    now = datetime.now().isoformat()
    with open(FILENAME, "a") as f:
        f.write(f"{visitor_name} | {now}\n")


def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
