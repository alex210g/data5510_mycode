class Node: 
	def __init__(self, key):
		self.key = key 
		self.left = None 
		self.right = None 

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

def search(root, search_item): 
	# If you reach none, the tree is empty or doesn't exist. 
	if root == None:
		return False
	# determine if item is larger or smaller than the root, then finds the node
	elif search_item < root.key: 
		return search(root.left, search_item)
	elif search_item > root.key: 
		return search(root.right, search_item)
	#hits else if the node is equal to the search item. 
	else:
		return True 


if __name__ == "__main__":
	tree_list = [1,5,10,35, 10, 22, 2, 8, 39, 3000]
	root = None
	for item in tree_list:
		root = insert(root, item)
	#multiple test values, change this list to search for other nodes. 
	test_values = [22, 9, 1, 3000, 10]
	for value in test_values: 
		if search(root, value):
			print(f"{value} was found")
		else: 
			print(f"{value} was not found")



# AI Prompts (Claude):
# 1. "Should I copy the full code from easy.py to build a tree to search?"
# 2. "Should search return False on the first two cases and True on the third,
#     and print found / not found in main?"
# 3. I had claud fix an indentatino error in the whole file, it was saying I used inconsisten spaced when all I did was use tab. It cleaned that up. 

