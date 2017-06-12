
def show_notes(ep_no):
    filename = "core/show_notes/" + str(ep_no) + ".md"
    with open(filename) as f:
        return f.read()


def get_last_4episode_num(ep_count):
    # python needs +1
    ep_count += 1
    return reversed(range(ep_count)[-4:])


def episode_title(episode_num):
    """Episode title for the respective episode

    :episode_num: int
    :returns: str
        title of the episode taken from the markdown

    """
    with open('core/show_notes/{}.md'.format(str(episode_num))) as f:
        title_line = f.readline().rstrip()
    title_line = title_line.replace("# ", "")
    title_line = title_line.replace("## ", "")
    title_line = title_line.replace("#", "")
    return title_line


def get_archives_content(ep_count):
    """The list of past urls that will go to the archive section.

    :ep_count: int
        The present count of the total number of episodes present.
    :returns: str
        html string with the list of the episodes.

    """
    return [(i, episode_title(i)) for i in reversed(range(1, ep_count - 3))]

