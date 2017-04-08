
def show_notes(ep_no):
    filename = "core/show_notes/" + str(ep_no) + ".md"
    with open(filename) as f:
        return f.read()


def get_last_4episode_num(ep_count):
    # python needs +1
    ep_count += 1
    return reversed(range(ep_count)[-4:])
