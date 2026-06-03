import json
from task_cli.task import Task, update_task
FILE_NAME = "task_list.json"
MAJOR_COMMAND = "task-cli"
MID_COMMANDS = ["add", "update", "delete", "list", "mark"]
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
    command_line_length = len(splitted_command)
    if command_line_length >= 3:
        if MAJOR_COMMAND == splitted_command[0] and MID_COMMANDS[0] == splitted_command[1]:
            new_task_name = " ".join(splitted_command[2:])
            new_id = 1 if not data else max(some_task['id'] for some_task in data) + 1
            data.append(Task(new_id, new_task_name, MINOR_COMMANDS[2]).__dict__)
        elif (data is not None and splitted_command[1] in MID_COMMANDS[1:3] and splitted_command[2].isdigit() and any(task['id'] == int(splitted_command[2]) for task in data)):
            match_index = next(index for index, task in enumerate(data) if task['id'] == int(splitted_command[2]))
            if (splitted_command[1] == MID_COMMANDS[1]):
                data[match_index]['description'] = " ".join(splitted_command[3:])
                data[match_index]['updated_at'] = update_task()
            elif (splitted_command[1] == MID_COMMANDS[2]):
                del data[match_index]
        elif (data is not None and MAJOR_COMMAND == splitted_command[0] and MID_COMMANDS[3] == splitted_command[1]
            and any(task['status'] == splitted_command[2] for task in data)):
                for task in data:
                    if(task['status'] == splitted_command[2]):
                        print(task)
    elif command_line_length == 2:
        if MAJOR_COMMAND == splitted_command[0] and MID_COMMANDS[3] == splitted_command[1]:
            for task in data:
                print(task)

    process_file_with_mode(FILE_NAME, data)

def process_file_with_mode(file_name,data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)