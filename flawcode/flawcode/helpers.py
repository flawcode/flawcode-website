import markdown

def show_notes(ep_no):
    filename = "flawcode/show_notes/" + str(ep_no) + ".md"
    with open(filename) as f:
        return f.read()


def directly_linked_old(ep_count):
    return reversed(range(ep_count + 1)[ep_count-3:])