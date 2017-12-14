import sys
from usage_information import *

def eat_userinput():
    if sys.argv[-1] == 'main_modul.py':
        print_usage_information()
    elif sys.argv[1] == '-l':
        print_list()
    elif sys.argv[-1] == '-a' and len(sys.argv) == 2:
        print('Unable to add: no task provided')
    elif sys.argv[1] == '-a' and len(sys.argv) > 2:
        add_task()
    elif sys.argv[1] == '-r':
        remove_task()
    elif sys.argv[1] == '-c':
        print('Completes a task')
    else:
        print('\nType a valid argument!')
        print_usage_information()

def print_list():
    temp = open('list.txt', 'r')
    tasks = temp.readlines()
    if len(tasks) < 1:
        print('No todos for today!')
    for i in range(len(tasks)):
        print(str(i + 1) + ' - ' + tasks[i], end = '')
    temp.close()

def add_task():
    temp = open('list.txt', 'a')
    temp.write('\n')    
    temp.write(sys.argv[2])
    temp.close()

def remove_task():
    temp = open('list.txt', 'r')
    tasks = temp.readlines()
    to_remove = tasks[int(sys.argv[2]) - 1]
    temp.close()

    temp = open('list.txt', 'w')
    for line in tasks:
        if line != to_remove:
            temp.write(line)
    temp.close()
            
eat_userinput()
