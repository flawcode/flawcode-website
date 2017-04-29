from core.helpers import show_notes
from core.helpers import get_last_4episode_num


def test_show_notes():
    res = show_notes(4)
    assert len(list(res)) == 5446


def test_directly_linked_old():
    res = list(get_last_4episode_num(10))
    assert res == [10, 9, 8, 7]
