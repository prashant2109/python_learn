class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = Node(data)
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def my_insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous not is not in list") 
            return 

        new_node = Node(data)
        last_node = self.head
        while last_node.next:
            if last_node.data == prev_node:
                new_node.next = last_node.next
                last_node.next = new_node
                break
            
            last_node = last_node.next
        return

    def my_delete_node(self, del_elem):
        last_node = self.head
        prev_node = None
        while last_node.next:
            if last_node.data == del_elem:
                if prev_node is not None:
                    prev_node.next = last_node.next
                if prev_node is None:
                    self.head = last_node.next
                break
            prev_node = last_node
            last_node = last_node.next

    def node_swap(self, key_1, key_2):
        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev = cur_2
            cur_2 = cur_2.next

        if (not prev_1) and (prev_2):
            prev_2.next = cur_1
            cur_1 = cur_2

        if (prev_1) and (not prev_2):
            prev_1.next = cur_2 
            cur_2 = cur_1
        return 



if __name__ == '__main__':
    ll = LinkedList()
    ll.append('A')
    ll.append('B')
    ll.append('C')
    ll.append('D')
    ll.append('E')
    ll.print_list()

