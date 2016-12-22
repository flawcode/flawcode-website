import markdown

def show_notes(ep_no):
    filename = "flawcode/show_notes/" + str(ep_no) + ".txt"
    with open(filename) as f:
        #content = f.readlines()
        # return f.readlines()
        return f.read()
    #return (markdown.markdown(c) for c in content)


def directly_linked_old(ep_count):
    return reversed(range(ep_count + 1)[ep_count-3:])
