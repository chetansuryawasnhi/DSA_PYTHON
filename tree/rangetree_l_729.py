class Node():
    def __init__(self,start,end):
        self.start=start
        self.end=end
        self.l,self.r=None,None
    def insert(self,s,e):
            if s>=self.end:
                if not self.r:
                    self.r=Node(s,e)
                    return True
                return self.r.insert(s,e)  
            elif e<=self.start:
                if not self.l:
                    self.l=Node(s,e)
                    return True
                return self.l.insert(s,e)
            else:
                return False
class Tree():
    def __init__(self) :
        self.root=None
    def book(self, start, end) -> bool:
      if not self.root: 
        self.root = Node(start,end)
        return True
      else:
        return self.root.insert(start, end)
        