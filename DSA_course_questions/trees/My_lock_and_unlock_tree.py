class Node:
    def __init__(self,value,parent=None):
        self.value = value
        self.LDC = 0
        self.locked = False
        self.child = []
        self.parent = parent

def Dolock(node):
    x = node
    while x.parent != None:
        x.LDC += 1
        x = x.parent
    node.locked = True
#lock a node only if all the ancestors and descendents are unlock
#increase the LDC to 1 for all the ancestors by 1
def lock(node):
    x = node
    if node.LDC > 0 or node.locked == True  :
        return False
    else:
        while x.parent != None:
            if x.locked == True:  # not check LockedDescndentCount as sibling doesnt have any effect
                return False
            x = x.parent
        if x.parent == None:
            Dolock(node)
            return True


def Dounlock(node):
    x = node
    while x.parent != None:
        x.LDC -=1
        x = x.parent
    node.locked = False

def unlock(node):
    x = node
    if node.locked == False:
        return False
    else:
        Dounlock(node)
        return True

def upgrade(node):
    x = node
    count = 0
    for i in x.child:
        if i.locked == True:
            count += 1
    if count != len(x.child):
        return False
    else:
        for i in x.child:
            Dounlock(i)
        Dolock(node)
        return True

def preorder(root):
    print(root.value , end = " ") #for inorder
    if len(root.child) == 0:
        # print(root.value , end = " ")   for postorder
        return 0
    for i in root.child:
        preorder(i)
    #print(root.value , end = " ")  #for postorder
    return 0

# Creating a generic tree
root = Node("World")
(root.child).append(Node("Asia",root))
(root.child).append(Node("Africa",root))
(root.child[0].child).append(Node("China",root.child[0]))
(root.child[0].child).append(Node("India",root.child[0]))
(root.child[1].child).append(Node("SA",root.child[1]))
(root.child[1].child).append(Node("Egypt",root.child[1]))
print("yes")
preorder(root)
print(lock(root.child[0]))  #locking asia 
print(lock(root.child[0].child[1]))  # locking India 
print(lock(root.child[1].child[1]))  #locking Egpyt
print(unlock(root.child[0]))  #unlocking asia
print(lock(root.child[0].child[1]))  # locking India 
print(lock(root.child[0])) # locking Asia
#print(lock(root.child[0].child[0]))  # lock china
print(upgrade(root.child[0])) #upgrade Asia