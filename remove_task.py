import sys

class RemoveTask(object):

    def __init__(self):
        pass
    
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