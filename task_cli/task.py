from datetime import datetime

class Task:
    id: int
    description: str
    status: str
    created_at: str
    updated_at: str

    def __init__(self, id, description, status, created_at = datetime.now().isoformat(sep=' ', timespec='seconds'), updated_at = datetime.now().isoformat(sep=' ', timespec='seconds')):
        Task.id += 1
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

def update_task():
        return datetime.now().isoformat(sep=' ', timespec='seconds')
