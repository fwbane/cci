import unittest
from Frashmap import Frashmap, KV_pair

class Test(unittest.TestCase):
	def test_default_size(self):
		myMap = Frashmap()
		self.assertEqual(myMap.size, 128)
		myMap = Frashmap(64)
		self.assertEqual(myMap.size, 64)
	
	def test_get_size_method(self):
		myMap = Frashmap()
		self.assertEqual(myMap.get_size(), 0)
		myMap.table[0] = [KV_pair(6, "six")]
		self.assertEqual(myMap.get_size(), 1)

	def test_put_method(self):
		myMap = Frashmap()
		myMap.put(4, "four")
		self.assertEqual(myMap.get_size(), 1)

	def test_update_put_method(self):
		myMap = Frashmap()
		myMap.put(4, "four")
		myMap.put("4", "four-string")
		self.assertEqual(myMap.get_size(), 1)

	def test_get_method(self):
		myMap = Frashmap()
		myMap.put(4, "four")
		kv = myMap.get("4")
		self.assertEqual(kv.key, "4")
		self.assertEqual(kv.value, "four")
		kv = myMap.get(4)
		self.assertEqual(kv.key, "4")
		self.assertEqual(kv.value, "four")
	
	def test_get_method_for_absent_entry(self):
		myMap = Frashmap()
		self.assertEqual(myMap.get("missing"), None)
		
	def test_delete_method(self):
		myMap = Frashmap()
		myMap.put(4, "four")	
		self.assertEqual(myMap.get_size(), 1)
		myMap.delete(4)
		self.assertEqual(myMap.get_size(), 0)
	
	def test_kv_pair_hash(self):
		kv = KV_pair(1, "one")
		self.assertEqual(kv.hash, (1+(ord("1")*17)))
		

if __name__ == "__main__":
	unittest.main()