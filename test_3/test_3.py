from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):

    def test_hello_world(self):
        actual = fit_transform('hello, world')
        expected = [('hello, world', [1])]
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_many_args(self):
        actual = fit_transform('foo', 'bar', 'baz')
        expected = [
            ('foo', [0, 0, 1]),
            ('bar', [0, 1, 0]),
            ('baz', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)

    def test_meow(self):
        actual = fit_transform('a', 'd', 'c')
        expected = [
            ('a', [0, 0, 1]),
            ('d', [0, 1, 0]),
            ('c', [1, 0, 0])
        ]
        self.assertEqual(actual, expected)
        self.assertNotIn(('j', [0, 0, 0]), expected)


if __name__ == '__main__':
    unittest.main()
