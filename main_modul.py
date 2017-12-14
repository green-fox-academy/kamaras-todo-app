import sys
from usage_information import *

list_of_tasks = ['Walk the dog', 'Buy milk', 'Do homework']
# list_of_tasks = []

def eat_userinput():
    if sys.argv[-1] == 'main_modul.py':
        print_usage_information()
    elif sys.argv[1] == '-l' and list_of_tasks != []:
        print_list()
    elif sys.argv[1] == '-l' and list_of_tasks == []:
        print('No todos for today!')
    elif sys.argv[1] == '-a' and sys.argv[2] != []:
        print(add_task())
        print(list_of_tasks)
    elif sys.argv[-1] == '-a':
        print('Unable to add: no task provided')
    elif sys.argv[1] == '-r':
        print('Remove a task')
    elif sys.argv[1] == '-c':
        print('Completes a task')
    else:
        print('\nType a valid argument!')
        print_usage_information()

def print_list():
    for i in range(len(list_of_tasks)):
        print(str(i + 1) + ' - ' + list_of_tasks[i])

def add_task():
    list_of_tasks.append(sys.argv[2])
    return list_of_tasks

eat_userinput()
