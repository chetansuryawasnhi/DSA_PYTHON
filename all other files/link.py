class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insertbeg(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            return
        itr=self.head
        list=''
        while itr:
            list+=str(itr.data)+'-->'
            itr=itr.next
        print(list)
if __name__=="__main__":
    l1=LinkedList()
    l1.insertbeg(5)
    l1.insertbeg(8)
    l1.print()