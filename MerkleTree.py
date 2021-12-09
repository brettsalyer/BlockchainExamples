
class MerkleNode:
    
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return self.data

    def setLeft(self, new_node):
        self.left = new_node
        new_node.parent = self

    def setRight(self, new_node):
        self.right = new_node
        new_node.parent = self


class MerkleTree:

    def __init__(self, data) -> None:
        self.data = data
    
    def generate(self):
        import hashlib

        for x in range(0, len(self.data), 2):
            h1 = hashlib.sha256(self.data[x].encode('utf-8')).hexdigest()
            h2 = None
            print("Hash for item ", x, "is ", h1)
            node_left = MerkleNode(h1)

            if self.data[x+1] is not None:
                h2 = hashlib.sha256(self.data[x+1].encode('utf-8')).hexdigest()
                print("Hash for item ", x+1, "is ", h2)
                node_right = MerkleNode(h2)
            
            concat = h3 = hashlib.sha3_256((h1 + h2).encode('utf-8')).hexdigest()
            print("Parent node hash ", h3)
            parent_node = MerkleNode(h3)
            parent_node.setLeft(node_left)
            parent_node.setRight(node_right)

            





a = ["5", "7", "11", "4", "5",]


mt = MerkleTree(a)
mt.generate()
