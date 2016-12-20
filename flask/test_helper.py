from flawcode.helpers import show_notes
from flawcode.helpers import directly_linked_old


def test_show_notes():
    res = show_notes(4)
    assert len(res) == 40


def test_directly_linked_old():
    res = list(directly_linked_old(10))
    assert res == [10, 9, 8, 7]
