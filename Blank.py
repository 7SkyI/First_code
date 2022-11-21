import time
import random
from colorama import Fore, Back, Style

HELP = ''''
help - print command list.
add - add command and date (request for a command, date from the user).
show - display command added by user in (input) date.
show_all - display all commands added by user per date.
random - add a random task for today's date.
random_date - add a random date and task.
'''


RANDOM_TASKS = ['food and drink Preparation', 'eating and drinking', 'relaxing and leisure', 'working',
'do your homework', 'sports, exercise, and recreation', 'education']
RANDOM_DATE = random.randint(1, 30), random.randint(1, 12), random.randint(2022, 2100)

tasks = {

}

run = True


def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)

    else:
        tasks[date] = []
        tasks[date].append(task)

    print(Style.DIM + Fore.GREEN + 'Task', task, 'was added to the date', date)


while run:
    command = input(Fore.RED + 'Input command: ')
    if command == 'help':
        print(HELP)

    elif command == 'show':
        date = input(Fore.CYAN + 'Input date for display: ')
        if date in tasks:
            for task in tasks[date]:
                print(Fore.BLUE + '- ', task)

        else:
            print(Fore.BLACK + 'No date')

    elif command == 'show_all':
        print(Fore.GREEN, tasks)

    elif command == 'add':
        date: int | str = input(Fore.CYAN + 'Input date for adding task: ')
        task: int | str = input(Fore.CYAN + 'Input task name: ')
        add_todo(date, task)

    elif command == 'exit':
        run = False
        print(Fore.BLUE + 'Good bye')
        time.sleep(3)
        break

    elif command == 'random':
        task = random.choice(RANDOM_TASKS)
        add_todo('Today', task)

    elif command == 'random_date':
        task = random.choice(RANDOM_TASKS)
        add_todo(RANDOM_DATE, task)

    else:
        print(Fore.BLACK + Back.RED + 'Unknown command')
