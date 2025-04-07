# Write your code here
class Node:
    def __init__(self, data,parent=None):
        self.data = data
        self.children = []
        self.parent = parent
        self.locked = False
        self.uid = None
        self.LDC = 0
    def __str__(self):
        return str(self.data)
class N_ary_Tree:
    def __init__(self):
        self.root = None
    
    def add(self,data,parent=None):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.find_node(self.root,parent)
            parent_node.children.append(new_node)
            new_node.parent = parent_node
    
    def Dolock(self,node,uid):
        x = node
        while x.parent != None:
            x.LDC += 1
            x = x.parent
        node.locked = True
        node.uid = uid
    
    def lock(self, val, uid):
        node = self.find_node(self.root, val)
        x = node
        if node.LDC > 0 or node.locked == True:
            return 'false'
        else:
            while x.parent != None:
                if x.locked == True:
                    return 'false'
                x = x.parent
            if x.parent == None:
                self.Dolock(node,uid)
                return 'true'
    def Dounlock(self,node):
        x = node
        while x.parent != None:
            x.LDC -=1
            x = x.parent
        node.locked = False
        node.uid = None
    def unlock(self,val,uid):
        node = self.find_node(self.root, val)
        x = node
        if node.locked == False:
            return 'false'
        else:
            if node.uid == uid:
                self.Dounlock(node)
                return 'true'
            else:
                return 'false'
    
    
    
    def upgrade(self, val, uid):
        node = self.find_node(self.root, val)
        for child in node.children:
            if child.locked == True and child.uid == uid:
                continue
            else:
                return 'false'
        self.Dolock(node,uid)
        for child in node.children:
            if child.uid == uid:
                self.Dounlock(child)
        return 'true'
    
    def find_node(self, node, key):
        if node is None or node.data == key:
            return node
        for child in node.children:
            return_node = self.find_node(child, key)
            if return_node:
                return return_node
        return None
    
    def print_tree(self, node, str_aux):
        if node is None:
            return ""
        str_aux += str(node) + " Locked=" +str(node.locked)+ "UID:"+ str(node.uid) + '('
        for i in range(len(node.children)):
            child = node.children[i]
            end = ',' if i < len(node.children) - 1 else ''
            str_aux = self.print_tree(child, str_aux) + end
        str_aux += ')'
        return str_aux
    
    def __str__(self):
        return self.print_tree(self.root, "")

# main method
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    que = int(input())
    lt = []
    for i in range(n):
        st = input()
        lt.append(st)
    tree = N_ary_Tree() #tree has root obj
    tree.add(lt[0])
    i = 1
    key = [lt[0]]
    while i < n:
        temp = []
        for ele in key:
            if i < n:
                j = 0
                for j in range(m):
                    tree.add(lt[i], ele)
                    temp.append(lt[i])
                    i += 1
            else:
                break
        key = temp
    #print(tree)
    for i in range(que):
        temp = input().split()
        op_type = int(temp[0])
        node = temp[1]
        user_id = int(temp[2])
        if op_type == 1:
            print(tree.lock(node,user_id))
        elif op_type == 2:
            print(tree.unlock(node, user_id))
        elif op_type == 3:
            print(tree.upgrade(node, user_id))

'''
7
2
5
world
Asia
Africa
China
India
SA
Egypt
1 China 9
1 India 9
3 Asia 9
2 India 9
2 Asia 9'''