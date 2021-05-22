class TreeNode:
    def __init__(self, value = None, parent = None, left = None, right = None):
        self.value = value  
        self.parent = parent    
        self.left = left   
        self.right = right  
      
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        
    def delete_tree(self):
        if self.root:
            self.root.delete()
            del self.root
            self.root = None
        
    def loading_tree(self, file_name):
        string = ''
        with open(file_name,'r') as f:
            string = f.readline()
            
        self.delete_tree()
        blocks = string.split()
        current_parent = None
        is_left = True
        for block in blocks:
            if not self.root:
                self.root = TreeNode(int(block))
                current_parent = self.root
            else:
                if block=="0":
                    if is_left:
                        is_left = False
                    else:
                        while current_parent.parent and current_parent.parent.right==current_parent:
                            current_parent = current_parent.parent
                        current_parent = current_parent.parent
                else:
                    new_node = TreeNode(int(block), current_parent)
                    if is_left:
                        current_parent.left = new_node
                    else:
                        current_parent.right = new_node
                    current_parent = new_node
                    is_left = True
                if not current_parent:
                    break


def InOrderTreeWalk(x):
    if x!= None:
       InOrderTreeWalk(x.left)
       InOrderTreeWalk(x.right)
    return 0


def InOrderGetArray(array, x):
    if x!= None:
       InOrderGetArray(array, x.left)
       array.append(x.value)
       InOrderGetArray(array, x.right)
    return array


position = -1


def InOrderShearchTree(array, x):
    global position
    if x!= None:       
       InOrderShearchTree(array, x.left)
       position += 1
       x.value = array[position]
       InOrderShearchTree(array, x.right)
    return x


def ListSum(array):
    s = 0
    for i in array:
        s+=i
    return s


def SearchSum(x, tmp, s):
    if x!= None:
        tmp.append(x.value)
        SearchSum(x.left, tmp, s)
        if ListSum(tmp) == s: 
            return None
        SearchSum(x.right, tmp, s)
        if ListSum(tmp) == s: 
            return None
        tmp.pop()


def GetSum(x, summ, s):
    if x!=None:  
      GetSum(x.left, summ, s)
      tmp=[]
      SearchSum(x, tmp, s)
      if tmp:
              summ.append(tmp)
      GetSum(x.right, summ, s)
    
def main():
    print ("s:")
    s = int(input())
    tree = BinaryTree()
    tree.loading_tree('MyInput.txt')
    c=[] 
    InOrderGetArray(c, tree.root)
    c.sort()
    tree.root = InOrderShearchTree(c,tree.root)
    InOrderTreeWalk(tree.root)
    summ = []
    GetSum(tree.root, summ, s)

    file_res = open('MyOutput.txt', 'w')
    for i in range(len(summ)):
        file_res.write(str(summ[i])+"\n")
    file_res.close()
if __name__ == "__main__":
    main()

