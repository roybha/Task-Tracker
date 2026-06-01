import json
from random import randint
from task_cli.task import Task
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
    if MAJOR_COMMAND == splitted_command[0] and MID_COMMANDS[0] == splitted_command[1]:
        new_task_name = " ".join(splitted_command[2:])
        data.append(Task(randint(1,10), new_task_name, "done").__dict__)
    elif (data is not None and len(splitted_command) >= 3 and splitted_command[1] == MID_COMMANDS[1]
          and splitted_command[2].isdigit() and any(task['id'] == int(splitted_command[2]) for task in data)):
        match_index = next(index for index, task in enumerate(data) if task['id'] == int(splitted_command[2]))
        data[match_index]['description'] = " ".join(splitted_command[3:])
    process_file_with_mode(FILE_NAME, data)

def process_file_with_mode(file_name,data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        print(json.dumps(data, indent=4))