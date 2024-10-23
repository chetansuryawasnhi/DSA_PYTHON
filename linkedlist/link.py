class Link:
    def __init__(self,val,next=None):
        self.val=val
        self.next=None
arr=[1,2,3,4]
head=Link(arr[0])
n=head
for i in arr[1:]:
    n.next=Link(i)
    n=n.next

while head:
    print(b.val)
    b=b.next