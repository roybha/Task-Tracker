from datetime import datetime

class Task:
    id: int
    description: str
    status: str
    created_at: str
    updated_at: str

    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat(sep=' ', timespec='seconds')
        self.updated_at = datetime.now().isoformat(sep=' ', timespec='seconds')

    def update_task(self):
        self.updated_at =datetime.now().isoformat(sep=' ', timespec='seconds')

    def update_field(self, field_name, value):
        if hasattr(self, field_name):
            setattr(self, field_name, value)
            self.update_task()