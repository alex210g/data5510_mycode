class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None #changes from none to another node when they get a child.
		self.right = None

# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	# Else will insert duplicate nodes to the right as well. 
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key, end=" ")
		inorder(root.right)
		#returns at the end

# Task 4. Write a pre-order print
def preOrder(root): 
	if root is not None: 
		print(root.key, end=" ")
		inorder(root.left)
		inorder(root.right)

# Task 5. Write a post-order print
def postOrder(root): 
		inorder(root.left)
		inorder(root.right)
		print(root.key, end=" ")
		

if __name__ == "__main__":
	tree_list = [1,5,10,35, 10, 22, 2, 8, 39, 3000]
	root = None
	for item in tree_list:
		root = insert(root, item)
	inorder(root)
	print()
		



 # AI Prompts (Claude):
# 1. "Would I just need the node class and the insert function?"
# 2. "How do I insert a single item and the root at the same time in a for loop?"
# 3. "How is this a tree? What code is making this a BST?"
# 4.  "Is a node class and insert function all that I need to be able to do this" 
# AI: Confirmed I had the correct components.
