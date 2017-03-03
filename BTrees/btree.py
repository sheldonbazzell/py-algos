class BTNode(object):
	"""BTNode Class"""

	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None


	def get_min(self):
		if self.leftChild:
			return self.leftChild.get_min()
		else:
			return self.data


	def add(self, data):
		if data < self.data:
			if self.leftChild:
				self.leftChild.add(data)
			else:
				self.leftChild = BTNode(data)
		else:
			if self.rightChild:
				self.rightChild.add(data)
			else:
				self.rightChild = BTNode(data)
		return self


	def in_order_traversal(self):
		if self.leftChild:
			self.leftChild.in_order_traversal()
		print self.data
		if self.rightChild:
			self.rightChild.in_order_traversal()


	def pre_order_traversal(self):
		print self.data
		if self.leftChild:
			self.leftChild.pre_order_traversal()
		if self.rightChild:
			self.rightChild.pre_order_traversal()


	def post_order_traversal(self):
		if self.leftChild:
			self.leftChild.post_order_traversal()
		if self.rightChild:
			self.rightChild.post_order_traversal()
		print self.data


	def contains(self, target):
		if self.data == target:
			return True
		if target < self.data:
			if self.leftChild:
				return self.leftChild.contains(target)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.contains(target)
			else:
				return False


	def remove(self, target, parent):
		if target < self.data:
			if self.leftChild:
				return self.leftChild.remove(target, self)
			else:
				return False
		elif target > self.data:
			if self.rightChild:
				return self.rightChild.remove(target, self)
			else:
				return False
		else:
			if self.leftChild and self.rightChild:
				self.data = self.rightChild.get_min()
				self.rightChild.remove(self.data, self)
			elif parent.rightChild == self:
				if self.leftChild:
					parent.leftChild = self.leftChild
				else:
					parent.leftChild = self.rightChild
			elif parent.leftChild == self:
				if self.leftChild:
					parent.leftChild = self.leftChild
				else:
					parent.leftChild = self.leftChild


	def get_height(self, node):
		if not node:
			return -1
		left = self.get_height(node.leftChild)
		right = self.get_height(node.rightChild)
		return left + 1 if left > right else right + 1


	def is_balanced(self):
		if self.leftChild:
			if not self.rightChild:
				if self.leftChild.leftChild or self.leftChild.rightChild:
					return False
			return self.leftChild.is_balanced()
		if self.rightChild:
			if not self.leftChild:
				if self.leftChild.leftChild or self.leftChild.rightChild:
					return False
			return self.rightChild.is_balanced()
		return True



class BinaryTree(object):
	"""BinaryTree Class"""
	def __init__(self):
		self.root = None


	def add(self, data):
		if self.root:
			return self.root.add(data)
		self.root = BTNode(data)
		return self


	def in_order_traversal(self):
		if self.root:
			return self.root.in_order_traversal()
		return self


myBT = BinaryTree()
myBT.add(5).add(3).add(2).add(4).add(7).add(6).add(9)
# myBT.root.remove(2, None)g
# myBT.root.in_order_traversal()
# print myBT.root.is_balanced()
print myBT.__doc__