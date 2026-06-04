import json
from task_cli.task import Task, update_task
FILE_NAME = "task_list.json"
MAJOR_COMMAND = "task-cli"
MID_COMMANDS = ["add", "update", "delete", "mark", "list"]
MINOR_COMMANDS = ["done", "todo", "in-progress"]
def app():
    try:
        while True:
            user_input = input()
            main(user_input)
    except KeyboardInterrupt:
        print("Program interrupted")

def main(command: str):
    data = None
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data =  []
    splitted_command = command.split()
    if len(splitted_command) < 2 or splitted_command[0] != MAJOR_COMMAND:
        return
    action = splitted_command[1]
    if action == MID_COMMANDS[0]:
        if len(splitted_command) >= 3:
            new_task_name = " ".join(splitted_command[2:])
            new_id = 1 if not data else max(some_task['id'] for some_task in data) + 1
            data.append(Task(new_id, new_task_name, MINOR_COMMANDS[1]).__dict__)
    elif action == MID_COMMANDS[1] or action == MID_COMMANDS[2] or action.startswith(f"{MID_COMMANDS[3]}-"):
        if (len(splitted_command) >= 3 and splitted_command[2].isdigit()
                and any(task['id'] == int(splitted_command[2]) for task in data)):
            searched_index = next(index for index, task in enumerate(data) if task['id'] == int(splitted_command[2]))
            if action == MID_COMMANDS[2]:
                del data[searched_index]
            else:
                data[searched_index]['updated_at'] = update_task()
                if action == MID_COMMANDS[1]:
                    data[searched_index]['description'] = " ".join(splitted_command[3:])
                else:
                    new_status = splitted_command[1].split("-")[1]
                    data[searched_index]['status'] = new_status
    elif action == MID_COMMANDS[4]:
        for task in data:
            if len(splitted_command) == 3 and task['status'] != splitted_command[2]:
                continue
            print(task)
    process_file_with_mode(FILE_NAME, data)

def process_file_with_mode(file_name,data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)