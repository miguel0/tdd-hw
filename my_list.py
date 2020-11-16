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
		if len(values) == 0:
			return
		
		if self.head is None:
			self.head = MyNode(values[0])
			values = values[1:]
		
		if len(values) == 0:
			return
		
		current = self.head
		while current.next is not None:
			current = current.next
		for value in values:
			temp = MyNode(value)
			current.next = temp
			current = temp
	
	def exists(self, value):
		if self.head is None:
			return False
		
		current = self.head
		while current.next is not None:
			if current.value == value:
				return True
			current = current.next
			
		if current.value == value:
			return True
		
		return False
	
	def getAt(self, index):
		if index < 0:
			return None
		elif self.head is None:
			return None
		
		current = self.head
		for i in range(index):
			if current.next is None:
				return None
			current = current.next
		
		return current.value
	
	def get(self, value):
		return None
	
	def remove(self, index):
		return None
