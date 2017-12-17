class UndirectedGraph :

    name = ""

    def __init__(self, name):
        print('inside init')
        self.name = name
        print(self.name)

def do_main():
    udg = UndirectedGraph("Calling graph from do_main")

if __name__ == '__main__':
    print('name to call main')
    do_main()


