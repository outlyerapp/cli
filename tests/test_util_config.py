import unittest

from outlyer import util


class TestSubprocess(unittest.TestCase):

    def test_merge_config(self):
        base = {'a': 123, 'b': '456'}
        update = {'c': '789', 'd': 0}
        m = util.merge_config(base, update)
        self.assertEqual(m, {'a': 123, 'b': '456', 'c': '789', 'd': 0})

    def test_merge_config_overrides(self):
        base = {'a': 123, 'b': '456'}
        update = {'b': 'two', 'c': '789'}
        m = util.merge_config(base, update)
        self.assertEqual(m, {'a': 123, 'b': 'two', 'c': '789'})

    def test_merge_config_ignore_missing_overrides(self):
        base = {'a': 123, 'b': '456'}
        update = {'b': None, 'c': '789'}
        m = util.merge_config(base, update)
        self.assertEqual(m, {'a': 123, 'b': '456', 'c': '789'})

    def test_merge_config_dont_update_originals(self):
        base = {'a': 123, 'b': '456'}
        update = {'c': '789', 'd': 0}
        _ = util.merge_config(base, update)
        self.assertEqual(base, {'a': 123, 'b': '456'})
        self.assertEqual(update, {'c': '789', 'd': 0})