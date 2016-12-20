from flawcode.helpers import show_notes

def test_show_notes():
    res = show_notes(4)
    assert res == ['this is the show notes for the fourth episode\n']
