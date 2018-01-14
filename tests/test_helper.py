import unittest

from core.helpers import show_notes
from core.helpers import get_last_4episode_num
from core.helpers import get_archives_content
from core.helpers import episode_title
from core.helpers import mp3_file_sizes


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

    def test_episode_title(self):
        """TODO: Docstring for test_episode_title."""
        res = episode_title(7)
        self.assertEqual(res, 'DataScience with S Anand')

    def test_mp3_file_sizes(self):
        """TODO: Docstring for test_mp3_file_sizes.

        :f: TODO
        :returns: TODO

        """
        res = mp3_file_sizes()
        self.assertEqual(res['1.mp3'], '38.32')

if __name__ == '__main__':
    unittest.main()
