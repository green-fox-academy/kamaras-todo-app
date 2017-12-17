import sys
from remove_task import RemoveTask
from print_list import PrintList
from add_task import AddTask
from usage_information import Usage

class Todo():

    def __init__(self):
        list = open('list.txt', 'a')
        list.close()

    def eat_userinput(self):
        if sys.argv[-1] == 'main_modul.py':
            return print(Usage.print_usage_information(self))
        elif sys.argv[1] == '-l':
            PrintList.print_list(self)

        elif sys.argv[-1] == '-a' and len(sys.argv) == 2:
            return print('Unable to add: no task provided')
        elif sys.argv[1] == '-a' and len(sys.argv) > 2:
            AddTask.add_task(self)

        elif sys.argv[-1] == '-r' and len(sys.argv) == 2:
            return print('Unable to remove: no index provided')
        elif sys.argv[1] == '-r' and len(sys.argv) > 2 and sys.argv[2].isalpha():
            return print('Unable to remove: index is not a number')

        try:
            if sys.argv[1] == '-r' and len(sys.argv) > 2 and not sys.argv[2].isalpha():
                RemoveTask.remove_task(self)
        except IndexError:
            return print('Unable to remove: index is out of bound')

        if sys.argv[-1] == '-c':
            return print('Completes a task')

todo = Todo()
todo.eat_userinput()
