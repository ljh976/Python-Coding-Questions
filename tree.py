class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()       
        print(self.data)
        if self.right:
            self.right.PrintTree()
        
            
    def insert(self, data):
        if data < self.data: #if new value small than root, put left
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
                
        elif data > self.data: #if new value bigger than root, put right
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
            
root = Node(10)
root.insert(5)
root.insert(15)
root.insert(3)

root.PrintTree()