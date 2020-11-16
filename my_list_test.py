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
	
	def test_get_at(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.get_at(3), 4)
		self.assertIs(list.get_at(6), None)
		with self.assertRaises(TypeError):
			list.get_at('not an int')
	
	def test_get_index_of(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.get_index_of(3), 2)
		self.assertEqual(list.get_index_of(6), -1)
	
	def test_remove(self):
		list = MyList(1, 2, 3, 4)
		self.assertEqual(list.remove(3), 4)
		self.assertIs(list.remove(6), None)
		self.assertEqual(list.size(), 3)
		with self.assertRaises(TypeError):
			list.remove('not an int')

if __name__ == '__main__':
	unittest.main()