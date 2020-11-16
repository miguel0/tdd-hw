import unittest
from my_list import MyList

class TestMyList(unittest.TestCase):

	def test_size(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.size(), 4)
	
	def test_clear(self):
		list = MyList(1, 2, 3, 4)
		list.clear()
		self.assertEqual(list.size(), 0)
	
	def test_add(self):
		list = MyList(1, 2, 3, 4)
		list.add(5, 6, 7, 8)
		self.assertEqual(list.size(), 8)
	
	def test_exists(self):
		return
	
	def test_getAt(self):
		return
	
	def test_get(self):
		return
	
	def test_remove(self):
		return

if __name__ == '__main__':
	unittest.main()