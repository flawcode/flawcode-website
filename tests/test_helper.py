import unittest

from core.helpers import show_notes
from core.helpers import get_last_4episode_num
from core.helpers import get_archives_content


class TestHelpers(unittest.TestCase):

    """Docstring for TestHelpers. """

    def setUp(self):
        """TODO: to be defined1. """
        pass

    def tearDown(self):
        pass

    def test_show_notes():
        res = show_notes(4)
        assert len(list(res)) == 5446


    def test_directly_linked_old():
        res = list(get_last_4episode_num(10))
        assert res == [10, 9, 8, 7]


    def test_get_archives_content(self):
        """TODO: Docstring for test_get_archives_content."""
        res = get_archives_content(7)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
