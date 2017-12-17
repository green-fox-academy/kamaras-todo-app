import sys

class AddTask():

    def __init__(self):
        pass
    
    def add_task(self):
        temp = open('list.txt', 'a')
        temp.write('\n')    
        temp.write(sys.argv[2])
        temp.close()