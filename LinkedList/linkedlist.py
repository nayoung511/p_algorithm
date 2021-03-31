class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.next = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def traverse(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


    def delete(self, data):
        if self.head == "":
            print("삭제할 노드가 없습니다.")
            return

        if self.head == data:
            temp = self.head
            self.head = self.next
            del temp

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next



def main():
    linkedlist1 = NodeMgmt(0)
    #linkedlist1.traverse()

    for i in range(1, 10):
        linkedlist1.add(i)
    #linkedlist1.traverse()

    linkedlist1.delete(4)
    linkedlist1.traverse()
main()