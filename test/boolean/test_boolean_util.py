import unittest;
from boolean_util import is_truelike;

class TestBooleanUtil(unittest.TestCase):
  def test_is_truelike(self):
    self.assertTrue(is_truelike(True))
    self.assertTrue(is_truelike("True"))
    self.assertTrue(is_truelike("t"))
    self.assertEqual(is_truelike("t"), True)
    self.assertNotEqual(is_truelike("f"), True)
    self.assertNotEqual(is_truelike(False), True)
    self.assertNotEqual(is_truelike("False"), True)
    self.assertNotEqual(is_truelike("0"), True)
    self.assertNotEqual(is_truelike(0), True)
    self.assertEqual(is_truelike(1), True)
    self.assertEqual(is_truelike("1"), True)
    self.assertEqual(is_truelike("T"), True)
    self.assertEqual(is_truelike("YES"), True)
    self.assertEqual(is_truelike("Y"), True)
    self.assertNotEqual(is_truelike("N"), True)

if __name__ == '__main__':
    unittest.main()