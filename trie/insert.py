class Node:
    def __init__(self) :
        self.links=[None]*26
        self.flag=False
    def containskey(self,ch):
        return self.links[ord(ch)-ord("a")] is not None
    def put(self,ch,node):
        self.links[ord(ch)-ord("a")]=node
    def get(self,ch):
        return self.links[ord(ch)-ord("a")]
    def setend(self):
        self.flag=True
    def isend(self):
        return self.flag
    
class Trie:
    def __init__(self) :
        self.root=Node()
        
    def insert(self,word):
        node = self.root
        for ch in word:
            if not node.containskey(ch):
                node.put(ch,Node())
            node = node.get(ch)
        node.setend()
    def search(self,word):
        node=self.root
        for ch in word:
            if not node.containskey(ch):
                return False
            node=node.get(ch)
        return node.isend()
    def stratwith(self,word):
        node=self.root
        for ch in word:
            if not node.containskey(ch):
                return False
            node=node.get(ch)
        return True