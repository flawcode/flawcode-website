
def show_notes(ep_no):
    filename = "core/show_notes/" + str(ep_no) + ".md"
    with open(filename) as f:
        return f.read()


def get_last_4episode_num(ep_count):
    # python needs +1
    ep_count += 1
    return reversed(range(ep_count)[-4:])


def get_archives_content(ep_count):
    """The list of past urls that will go to the archive section.

    :ep_count: int
        The present count of the total number of episodes present.
    :returns: str
        html string with the list of the episodes.

    """
    x = []
    for i in range(1, ep_count - 3):
        x.append((i, 'episode 1'))
    return x

