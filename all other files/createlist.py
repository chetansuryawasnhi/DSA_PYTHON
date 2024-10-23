class Node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        # print(self.data)
class Linklist():
    def __init__(self):
        self.head=None
    def insert(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            # print(self.head.data)
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def pr(self):
        n=self.head
        while n:
            print(n.data)
            n=n.next
s1=Linklist()
s1.insert(5)
s1.insert(6)
s1.insert(12)
s1.pr()


        
