class PrintList():

    def __init__():
        pass

    def print_list(self):
        temp = open('list.txt', 'r')
        tasks = temp.readlines()
        if len(tasks) < 1:
            print('No todos for today!')
        for i in range(len(tasks)):
            print(str(i + 1) + ' - ' + tasks[i], end = '')
        temp.close()