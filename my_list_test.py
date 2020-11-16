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
		list = MyList(1, 2, 3, 4)
		self.assertTrue(list.exists(2), True)
		self.assertFalse(list.exists(8), False)
	
	def test_getAt(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.getAt(3), 4)
		self.assertIs(list.getAt(6), None)
	
	def test_getIndexOf(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.getIndexOf(3), 2)
		self.assertEqual(list.getIndexOf(6), -1)
	
	def test_remove(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.remove(3), 4)
		self.assertIs(list.remove(6), None)
		self.assertEqual(list.size(), 3)

if __name__ == '__main__':
	unittest.main()