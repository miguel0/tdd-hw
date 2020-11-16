class MyNode:

	def __init__(self, value):
		self.value = value
		self.next = None

class MyList:

	def __init__(self, *values):
		if len(values) == 0:
			self.head = None
		else:
			self.head = MyNode(values[0])
			current = self.head
			for value in values[1:]:
				temp = MyNode(value)
				current.next = temp
				current = temp
	
	def size(self):
		if self.head is None:
			return 0
		
		size = 1
		current = self.head
		while current.next is not None:
			size += 1
			current = current.next

		return size
	
	def clear(self):
		self.head = None
	
	def add(self, *values):
		return None
	
	def exists(self, value):
		return None
	
	def getAt(self, index):
		return None
	
	def get(self, value):
		return None
	
	def remove(self, index):
		return None
