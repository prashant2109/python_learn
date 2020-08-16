class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_empty_list(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.nref = self.head
        self.head.pref = new_node
        self.head = new_node
        return
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        cur_node = self.head
        while cur_node:
            if cur_node.nref is None:
                cur_node.nref = new_node
                new_node.pref = cur_node
                return 
            cur_node = cur_node.nref

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.nref
        return

if __name__ == '__main__':
    dll = DoubleLinkedList()
    # dll.insert_at_empty_list('A')
    dll.insert_at_start('B')
    dll.insert_at_start('C')
    dll.insert_at_start('D')
    dll.insert_at_start('E')
    dll.print_list()