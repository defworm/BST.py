#Part 1: Create a BSTNode class
class BSTNode:
  def __init__(self, data=None):
    self.data=data
    self.left = None
    self.right = None 

  def __str__(self):
    return str(self.data)

  def __repr__(self):
    return str(self.data)



#Part 2: Create a BST class

class BST:
  def __init__(self, root=None):
    self.root = root
    self.contents = []

  def __str__(self):
    if self.root == None:
      return "The tree is empty"
    else:
      self.output = ''
      self.print_tree(node=self.root)
      return self.output


  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + '\n'
      self.print_tree(node.left, level + 1)

  #Part 3: Add functionality to your BST class

  def add(self, node):
    if type(node) != int and type(node) != BSTNode:
      raise ValueError("Argument must be an integer or a BSTNode")

    if type(node) == int:
      node = BSTNode(node)

    if node.data in self.contents:
      return

    if self.root == None:
      self.root = node
      self.contents.append(node.data)
      return

    self.add_node(self.root, node)

  def add_node(self, cur_node, new_node):
    #bigger, go right
    if new_node.data > cur_node.data:
      if cur_node.right == None:
        cur_node.right = new_node
        self.contents.append(new_node.data)
        return
      else:
        self.add_node(cur_node.right)

      #smaller, go left
      if new_node.data < cur_node.data:
        if cur_node.left == None:
           cur_node.left = new_node
           self.contents.append(new_node.data)
           return
    else:
        self.add_node(cur_node.left, new_node)






if __name__ == "__main__":
  node1 = BSTNode(10)
  node2 = BSTNode(5)
  node3 = BSTNode(20)
  # print(node1)
  bst= BST()
  print(bst)
  bst.add = (node1)
  print(bst)
  bst.add = (node2)
  bst.add = (node3)
  print(bst)
  