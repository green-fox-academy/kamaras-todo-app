import sys
from usage_information import Usage

class Todo():

    def __init__(self):
        pass

    def eat_userinput(self):
        if sys.argv[-1] == 'main_modul.py':
            Usage.print_usage_information(self)
        elif sys.argv[1] == '-l':
            self.print_list()
        elif sys.argv[-1] == '-a' and len(sys.argv) == 2:
            print('Unable to add: no task provided')
        elif sys.argv[1] == '-a' and len(sys.argv) > 2:
            self.add_task()
        elif sys.argv[-1] == '-r' and len(sys.argv) == 2:
            print('Unable to remove: no index provided')
        elif sys.argv[1] == '-r' and len(sys.argv) > 2 and sys.argv[2].isalpha():
            print('Unable to remove: index is not a number')
        elif sys.argv[1] == '-r' and len(sys.argv) > 2:
            self.remove_task()
        elif sys.argv[1] == '-c':
            print('Completes a task')
        else:
            print('\nType a valid argument!')
            print_usage_information()

    def print_list(self):
        temp = open('list.txt', 'r')
        tasks = temp.readlines()
        if len(tasks) < 1:
            print('No todos for today!')
        for i in range(len(tasks)):
            print(str(i + 1) + ' - ' + tasks[i], end = '')
        temp.close()

    def add_task(self):
        temp = open('list.txt', 'a')
        temp.write('\n')    
        temp.write(sys.argv[2])
        temp.close()

    def remove_task(self):
        temp = open('list.txt', 'r')
        tasks = temp.readlines()
        to_remove = tasks[int(sys.argv[2]) - 1]
        temp.close()
        temp = open('list.txt', 'w')
        for line in tasks:
            if line != to_remove:
                temp.write(line)
        temp.close()

todo = Todo()
todo.eat_userinput()
