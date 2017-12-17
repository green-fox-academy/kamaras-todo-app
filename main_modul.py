import sys
import print_list
from usage_information import Usage

class Todo():

    def __init__(self):
        list = open('list.txt', 'a')
        list.close()

    def eat_userinput(self):
        if sys.argv[-1] == 'main_modul.py':
            print(Usage.print_usage_information(self))
        elif sys.argv[1] == '-l':
            PrintList.print_list()

        elif sys.argv[-1] == '-a' and len(sys.argv) == 2:
            print('Unable to add: no task provided')
        elif sys.argv[1] == '-a' and len(sys.argv) > 2:
            self.add_task()

        elif sys.argv[-1] == '-r' and len(sys.argv) == 2:
            print('Unable to remove: no index provided')
        elif sys.argv[1] == '-r' and len(sys.argv) > 2 and sys.argv[2].isalpha():
            print('Unable to remove: index is not a number')
        try:
            if sys.argv[1] == '-r' and len(sys.argv) > 2:
                self.remove_task()
        except IndexError:
            return print('Unable to remove: index is out of bound')

        if sys.argv[1] == '-c':
            print('Completes a task')
        else:
            print('\nType a valid argument!')
            Usage.print_usage_information(self)

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
