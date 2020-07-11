class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

class SLL:
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        """Check if the list is empty"""
        return self.head is None

    def add(self,data):
        new_node=Node(data)
        new_node.setNext(self.head)
        self.head=new_node
    
    def size(self):
        count=0
        current=self.head
        while current is not None:
            count+=1
            current=current.getNext()
        return count
    
    def search(self,data):
        current=self.head
        found=False
        while current is not None and not found:
            if current.getData() is data:
                found =True
            else:
                current=current.getNext()
    
    def remove(self,data):
        current=self.head
        previous=None
        found=False
        while current is not None and not found:
            if current.getData() is data:
                found=True
            else:
                current=current.getNext()
        if found:
            if previous is None:
                self.head=current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
        print('value not found')
    
    def insert(self,position,data):
        if position > self.size()-1:
            print('Index out of bounds')
        current=self.head
        previous=None
        pos=0
        if position is 0:
            self.add(data)
        else:
            new_node=Node(data)
            while pos<position:
                pos+=1
                previous=current
                current=current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)
    
    def index(self,data):
        current=self.head
        pos=0
        found=False
        while current is not None and not found:
            if current.getData() is data:
                found=True
            else:
                current=current.getNext()
                pos+=1
        if found:
            pass
        else:
            pos=None
        return pos
    
    def printlist(self):
        current=self.head
        while current is not None:
            print(current.getData())
            current=current.getNext()


ll = SLL()
ll.add('l')
ll.add('H')
ll.insert(1,'e')
ll.add('l')
ll.add('o')
ll.printlist()
            
